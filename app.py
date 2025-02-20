import os
import pandas as pd
import numpy as np
import random
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def load_kiva_data(file_path):
    print(f"Loading Kiva data from {file_path}")
    try:
        df = pd.read_csv(file_path, low_memory=False)
        print(f"Loaded {len(df)} rows from {file_path}")
        return df
    except Exception as e:
        print(f"Error loading Kiva data: {e}")
        raise

def process_data_in_chunks(file_path, chunk_size=10000):
    """Process large CSV file in chunks"""
    X_chunks = []
    y_chunks = []
    
    # Columns to use
    features = ['loan_amount', 'term_in_months', 'lender_count']
    
    # Read CSV in chunks
    for chunk in pd.read_csv(file_path, chunksize=chunk_size, low_memory=False):
        try:
            # Ensure required columns exist
            if not all(col in chunk.columns for col in features + ['funded_amount']):
                print(f"Skipping chunk. Missing required columns. Available: {chunk.columns}")
                continue
            
            # Create binary target variable
            chunk['fully_funded'] = (chunk['funded_amount'] >= chunk['loan_amount']).astype(int)
            
            # Prepare features and target
            X_chunk = chunk[features].fillna(chunk[features].mean())
            y_chunk = chunk['fully_funded']
            
            X_chunks.append(X_chunk)
            y_chunks.append(y_chunk)
        
        except Exception as e:
            print(f"Error processing chunk: {e}")
    
    # Concatenate chunks
    X = pd.concat(X_chunks, ignore_index=True)
    y = pd.concat(y_chunks, ignore_index=True)
    
    return X, y

def train_kiva_model(kiva_file, model_output):
    """
    Train a Random Forest classifier on the Kiva Loans dataset.
    
    Adjustments based on the dataset columns:
      - Drops rows missing 'loan_amount' or 'funded_amount'.
      - Creates a binary 'status' column: 1 if funded_amount >= loan_amount, else 0.
      - Drops non-predictive columns: id, Loan Theme ID, Loan Theme Type, Partner ID, partner_id,
        posted_time, disbursed_time, funded_time, tags, borrower_genders, repayment_interval, and date.
      - One-hot encodes categorical columns: activity, sector, use, country_code, country, region, and currency.
    """
    X, y = process_data_in_chunks(kiva_file)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    with open(model_output, 'wb') as f:
        pickle.dump({
            'model': model,
            'scaler': scaler
        }, f)
    
    print(f"Kiva loan model trained and saved to {model_output}.")

def train_custom_ensemble_model_kiva(kiva_file, ensemble_model_output):
    """
    Trains a custom ensemble model on the Kiva dataset.
    It stacks a RandomForest and a GradientBoosting classifier, then trains a meta-model (Logistic Regression)
    on their prediction probabilities.
    """
    X, y = process_data_in_chunks(kiva_file)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train_scaled, y_train)
    gb.fit(X_train_scaled, y_train)
    
    rf_probs = rf.predict_proba(X_train_scaled)[:, 1].reshape(-1, 1)
    gb_probs = gb.predict_proba(X_train_scaled)[:, 1].reshape(-1, 1)
    meta_features = np.hstack((rf_probs, gb_probs))
    
    meta_model = LogisticRegression(max_iter=200)
    meta_model.fit(meta_features, y_train)
    
    rf_test_probs = rf.predict_proba(X_test_scaled)[:, 1].reshape(-1, 1)
    gb_test_probs = gb.predict_proba(X_test_scaled)[:, 1].reshape(-1, 1)
    meta_test_features = np.hstack((rf_test_probs, gb_test_probs))
    ensemble_preds = meta_model.predict(meta_test_features)
    
    metrics = calculate_kiva_custom_metrics(y_test, ensemble_preds)
    print("Custom Ensemble Model Kiva Metrics:", metrics)
    
    ensemble = {"rf_model": rf, "gb_model": gb, "meta_model": meta_model, "scaler": scaler}
    with open(ensemble_model_output, 'wb') as f:
        pickle.dump(ensemble, f)
    print(f"Custom ensemble model saved to {ensemble_model_output}.")

def calculate_kiva_custom_metrics(y_true, y_pred):
    """
    Computes custom composite risk metrics for the Kiva model.
    Composite Risk Metric (CRM): 0.4 * Precision + 0.4 * Recall + 0.2 * F1 score.
    """
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    crm = 0.4 * precision + 0.4 * recall + 0.2 * f1
    return {"precision": precision, "recall": recall, "f1": f1, "composite_risk_metric": crm}

def train_sentiment_model(sentiment_file, model_output, vectorizer_output, label_encoder_output):
    """
    Train a multinomial Logistic Regression classifier on the Social Media Sentiments Analysis dataset.
    
    Uses "Text" for content and "Sentiment" as the label. LabelEncoder converts string labels to numeric.
    """
    df = pd.read_csv(sentiment_file)
    df = df.dropna(subset=['Text', 'Sentiment'])
    unique_labels = df['Sentiment'].unique()
    print("Unique sentiment labels:", unique_labels)
    
    le = LabelEncoder()
    df['Sentiment_encoded'] = le.fit_transform(df['Sentiment'])
    
    vectorizer = TfidfVectorizer(max_features=5000)
    X_text = vectorizer.fit_transform(df['Text'])
    
    X_train, X_test, y_train, y_test = train_test_split(X_text, df['Sentiment_encoded'], test_size=0.2, random_state=42)
    
    clf = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=200)
    clf.fit(X_train, y_train)
    
    with open(model_output, 'wb') as f:
        pickle.dump(clf, f)
    with open(vectorizer_output, 'wb') as f:
        pickle.dump(vectorizer, f)
    with open(label_encoder_output, 'wb') as f:
        pickle.dump(le, f)
    
    print(f"Sentiment model trained and saved to {model_output}.")
    print(f"TF-IDF vectorizer saved to {vectorizer_output}.")
    print(f"Label encoder saved to {label_encoder_output}.")

def train_naive_bayes_sentiment_model(sentiment_file, nb_model_output, vectorizer_output, label_encoder_output):
    """
    Trains a sentiment model using Multinomial Naive Bayes.
    Uses the "Text" column and the "Sentiment" label.
    """
    df = pd.read_csv(sentiment_file)
    df = df.dropna(subset=['Text', 'Sentiment'])
    le = LabelEncoder()
    df['Sentiment_encoded'] = le.fit_transform(df['Sentiment'])
    
    vectorizer = TfidfVectorizer(max_features=5000)
    X_text = vectorizer.fit_transform(df['Text'])
    
    X_train, X_test, y_train, y_test = train_test_split(X_text, df['Sentiment_encoded'], test_size=0.2, random_state=42)
    
    nb_clf = MultinomialNB()
    nb_clf.fit(X_train, y_train)
    
    y_pred = nb_clf.predict(X_test)
    metrics = calculate_sentiment_custom_metrics(y_test, y_pred)
    print("Naive Bayes Sentiment Model Metrics:", metrics)
    
    with open(nb_model_output, 'wb') as f:
        pickle.dump(nb_clf, f)
    with open(vectorizer_output, 'wb') as f:
        pickle.dump(vectorizer, f)
    with open(label_encoder_output, 'wb') as f:
        pickle.dump(le, f)
    
    print(f"Naive Bayes sentiment model saved to {nb_model_output}.")
    print(f"TF-IDF vectorizer saved to {vectorizer_output}.")
    print(f"Label encoder saved to {label_encoder_output}.")

def calculate_sentiment_custom_metrics(y_true, y_pred):
    """
    Computes custom metrics for sentiment models.
    Sentiment Balance Score (SBS): Average of accuracy and macro F1 score.
    """
    acc = accuracy_score(y_true, y_pred)
    macro_f1 = f1_score(y_true, y_pred, average='macro', zero_division=0)
    sbs = (acc + macro_f1) / 2
    return {"accuracy": acc, "macro_f1": macro_f1, "sentiment_balance_score": sbs}

def expand_dataset_using_ga(df, num_augmented_samples=100, num_generations=10, mutation_rate=0.1):
    """
    Uses a genetic algorithm (GA) to generate augmented synthetic samples from the input DataFrame.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    original_means = df[numeric_cols].mean()
    original_stds = df[numeric_cols].std()

    def fitness(individual):
        diff = np.abs(individual - original_means)
        return -np.sum(diff)

    population = []
    for _ in range(num_augmented_samples):
        individual = np.random.normal(loc=original_means, scale=original_stds)
        population.append(individual)
    population = np.array(population)

    for generation in range(num_generations):
        fitness_scores = np.array([fitness(ind) for ind in population])
        num_selected = max(2, len(population) // 2)
        selected_indices = fitness_scores.argsort()[-num_selected:]
        selected = population[selected_indices]

        offspring = []
        for i in range(0, len(selected) - 1, 2):
            parent1, parent2 = selected[i], selected[i+1]
            child = np.array([random.choice([p1, p2]) for p1, p2 in zip(parent1, parent2)])
            offspring.append(child)
        offspring = np.array(offspring)

        mutations = np.random.normal(loc=0, scale=mutation_rate, size=offspring.shape)
        offspring = offspring + mutations

        population = np.vstack((selected, offspring))
    
    augmented_df = pd.DataFrame(population, columns=numeric_cols)
    return augmented_df

class MicrofinanceEnv:
    """
    A simulated reinforcement learning environment for dynamic lending policies.
    """
    def _init_(self):
        self.state = np.array([0.5, 1000])
        self.action_space = [0, 1, 2]
        self.penalty_factor = 10
        self.social_factor = 5
        self.base_performance = 100

    def reset(self):
        self.state = np.array([0.5, 1000])
        return self.state

    def step(self, action):
        risk_threshold, loan_volume = self.state
        if action == 0:
            risk_threshold = max(0, risk_threshold - 0.05)
        elif action == 2:
            risk_threshold = min(1, risk_threshold + 0.05)
        financial_performance = self.base_performance * (1 - risk_threshold)
        risk_penalty = risk_threshold * self.penalty_factor
        social_bonus = (1 - risk_threshold) * self.social_factor
        reward = (financial_performance - risk_penalty) + social_bonus
        loan_volume = loan_volume * (1 + (risk_threshold - 0.5) * 0.1)
        self.state = np.array([risk_threshold, loan_volume])
        done = False
        return self.state, reward, done, {}

def train_rl_model(num_episodes=1000, learning_rate=0.1, discount_factor=0.95, epsilon=0.1):
    """
    Trains a Q-learning agent in the MicrofinanceEnv.
    """
    env = MicrofinanceEnv()
    risk_bins = np.linspace(0, 1, 11)
    state_space_size = len(risk_bins)
    action_space_size = len(env.action_space)
    
    Q_table = np.zeros((state_space_size, action_space_size))
    
    def discretize_state(state):
        risk_threshold, _ = state
        index = np.digitize(risk_threshold, risk_bins) - 1
        return max(0, min(index, state_space_size - 1))
    
    for episode in range(num_episodes):
        state = env.reset()
        state_idx = discretize_state(state)
        total_reward = 0
        for step in range(50):
            if random.random() < epsilon:
                action = random.choice(env.action_space)
            else:
                action = np.argmax(Q_table[state_idx])
            next_state, reward, done, _ = env.step(action)
            next_state_idx = discretize_state(next_state)
            Q_table[state_idx, action] = Q_table[state_idx, action] + learning_rate * (
                reward + discount_factor * np.max(Q_table[next_state_idx]) - Q_table[state_idx, action]
            )
            state_idx = next_state_idx
            total_reward += reward
        if episode % 100 == 0:
            print(f"Episode {episode}: Total Reward: {total_reward}")
    
    rl_model_output = 'models/saved_models/rl_agent.pkl'
    with open(rl_model_output, 'wb') as f:
        pickle.dump(Q_table, f)
    print(f"RL agent trained and saved to {rl_model_output}.")

import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Concatenate, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

def create_ai_agent_model(kiva_file, sentiment_file, agent_model_output):
    """
    Create an advanced AI agent model using transfer learning and multi-task learning.
    
    This model aims to:
    1. Predict loan funding status
    2. Classify sentiment
    3. Provide risk assessment
    
    Args:
        kiva_file (str): Path to Kiva loans dataset
        sentiment_file (str): Path to sentiment dataset
        agent_model_output (str): Path to save the trained model
    """
    kiva_df = load_kiva_data(kiva_file)
    kiva_df = kiva_df.dropna(subset=['loan_amount', 'funded_amount'])
    kiva_df['loan_status'] = kiva_df.apply(lambda row: 1 if row['funded_amount'] >= row['loan_amount'] else 0, axis=1)
    
    sentiment_df = pd.read_csv(sentiment_file)
    sentiment_df = sentiment_df.dropna(subset=['Text', 'Sentiment'])
    
    categorical_cols = ['activity', 'sector', 'use', 'country_code', 'region']
    for col in categorical_cols:
        if col in kiva_df.columns:
            kiva_df = pd.get_dummies(kiva_df, columns=[col])
    
    loan_features = kiva_df.drop(columns=['loan_status'])
    loan_targets = kiva_df['loan_status']
    
    vectorizer = TfidfVectorizer(max_features=5000)
    sentiment_text_features = vectorizer.fit_transform(sentiment_df['Text']).toarray()
    
    le = LabelEncoder()
    sentiment_targets = le.fit_transform(sentiment_df['Sentiment'])
    
    X_loan_train, X_loan_test, y_loan_train, y_loan_test = train_test_split(
        loan_features, loan_targets, test_size=0.2, random_state=42
    )
    X_sentiment_train, X_sentiment_test, y_sentiment_train, y_sentiment_test = train_test_split(
        sentiment_text_features, sentiment_targets, test_size=0.2, random_state=42
    )

    loan_input = Input(shape=(X_loan_train.shape[1],), name='loan_input')
    sentiment_input = Input(shape=(X_sentiment_train.shape[1],), name='sentiment_input')
    
    shared_layer1 = Dense(128, activation='relu', name='shared_layer1')
    shared_layer2 = Dense(64, activation='relu', name='shared_layer2')
    
    loan_branch1 = Dense(64, activation='relu')(shared_layer1(loan_input))
    loan_branch2 = Dense(32, activation='relu')(loan_branch1)
    loan_output = Dense(1, activation='sigmoid', name='loan_status_output')(loan_branch2)
    
    sentiment_branch1 = Dense(64, activation='relu')(shared_layer1(sentiment_input))
    sentiment_branch2 = Dense(32, activation='relu')(sentiment_branch1)
    sentiment_output = Dense(len(le.classes_), activation='softmax', name='sentiment_output')(sentiment_branch2)
    
    risk_input = Concatenate()([loan_branch1, sentiment_branch1])
    risk_branch = Dense(32, activation='relu')(risk_input)
    risk_output = Dense(1, activation='linear', name='risk_assessment_output')(risk_branch)
    
    model = Model(
        inputs=[loan_input, sentiment_input],
        outputs=[loan_output, sentiment_output, risk_output]
    )
    
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss={
            'loan_status_output': 'binary_crossentropy',
            'sentiment_output': 'sparse_categorical_crossentropy',
            'risk_assessment_output': 'mean_squared_error'
        },
        loss_weights={
            'loan_status_output': 0.4,
            'sentiment_output': 0.4,
            'risk_assessment_output': 0.2
        },
        metrics={
            'loan_status_output': ['accuracy'],
            'sentiment_output': ['accuracy'],
            'risk_assessment_output': ['mae']
        }
    )
    
    early_stopping = EarlyStopping(
        monitor='val_loss', 
        patience=10, 
        restore_best_weights=True
    )
    
    model.fit(
        {
            'loan_input': X_loan_train,
            'sentiment_input': X_sentiment_train
        },
        {
            'loan_status_output': y_loan_train,
            'sentiment_output': y_sentiment_train,
            'risk_assessment_output': y_loan_train.values.reshape(-1, 1)  # Simple risk proxy
        },
        validation_split=0.2,
        epochs=50,
        batch_size=32,
        callbacks=[early_stopping],
        verbose=1
    )
    
    loan_pred, sentiment_pred, risk_pred = model.predict({
        'loan_input': X_loan_test,
        'sentiment_input': X_sentiment_test
    })
    
    print("Loan Status Prediction Metrics:")
    print(calculate_kiva_custom_metrics(y_loan_test, (loan_pred > 0.5).astype(int)))
    
    print("\nSentiment Classification Metrics:")
    print(calculate_sentiment_custom_metrics(y_sentiment_test, sentiment_pred.argmax(axis=1)))
    
    model.save(agent_model_output)
    print(f"Multi-task AI Agent Model saved to {agent_model_output}")
    
    return model, vectorizer, le

def main():
    print("Starting main function...")
    # Update file paths
    kiva_loans_path = 'data/kiva_loans.csv'
    loan_themes_path = 'data/loan_themes_by_region.csv'
    mpi_locations_path = 'data/kiva_mpi_region_locations.csv'
    
    kiva_file = kiva_loans_path
    sentiment_file = 'data/sentimentsdataset.csv'
    
    kiva_model_output = 'models/saved_models/kiva_rf_model.pkl'
    ensemble_model_output = 'models/saved_models/kiva_ensemble_model.pkl'
    sentiment_model_output = 'models/saved_models/financial_sentiment_model.pkl'
    nb_model_output = 'models/saved_models/sentiment_nb_model.pkl'
    vectorizer_output = 'models/saved_models/tfidf_vectorizer.pkl'
    label_encoder_output = 'models/saved_models/label_encoder.pkl'
    agent_model_output = 'models/ai_agent_model.h5'
    
    os.makedirs(os.path.dirname(kiva_model_output), exist_ok=True)
    os.makedirs(os.path.dirname(vectorizer_output), exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    
    try:
        print(f"Current working directory: {os.getcwd()}")
        print(f"Attempting to load file: {kiva_loans_path}")
        print(f"File exists: {os.path.exists(kiva_loans_path)}")
        
        # List files in the data directory
        print("Files in data directory:")
        print(os.listdir('data'))
        
        print("Training Kiva loan model...")
        train_kiva_model(kiva_file, kiva_model_output)
        
        print("Training custom ensemble model for Kiva loans...")
        train_custom_ensemble_model_kiva(kiva_file, ensemble_model_output)
        
        # Optional: Skip sentiment model training if dataset is missing
        if os.path.exists(sentiment_file):
            print("Training social media sentiment model (Logistic Regression)...")
            train_sentiment_model(sentiment_file, sentiment_model_output, vectorizer_output, label_encoder_output)
            
            print("Training Naive Bayes sentiment model...")
            train_naive_bayes_sentiment_model(sentiment_file, nb_model_output, vectorizer_output, label_encoder_output)
        else:
            print(f"Sentiment dataset {sentiment_file} not found. Skipping sentiment model training.")
        
        print("Expanding Kiva dataset using Genetic Algorithm...")
        df_kiva = load_kiva_data(kiva_file)
        augmented_df = expand_dataset_using_ga(df_kiva, num_augmented_samples=50, num_generations=5, mutation_rate=0.05)
        augmented_file = 'data/processed/augmented_kiva.csv'
        augmented_df.to_csv(augmented_file, index=False)
        print(f"Augmented dataset saved to {augmented_file}.")
        
        print("Training RL model for dynamic lending policies...")
        train_rl_model(num_episodes=500)
        
        # Optional: Skip AI agent model training if sentiment dataset is missing
        if os.path.exists('data/sentiment_data.csv'):
            print("Training Multi-task AI Agent Model...")
            create_ai_agent_model(
                kiva_file=kiva_file,
                sentiment_file='data/sentiment_data.csv',  
                agent_model_output=agent_model_output
            )
        else:
            print("Sentiment dataset for AI agent not found. Skipping AI agent model training.")

    except Exception as e:
        print(f"Error: {e}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()