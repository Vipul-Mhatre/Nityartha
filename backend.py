from flask import Flask, request, jsonify
from flask_cors import CORS
from typing import Any, Dict, List, Optional
from implementation import (
    AlternativeDataFusion, GraphNeuralNetwork, FederatedCreditScoring, DynamicCreditScoring,
    DecentralizedKYC, DocumentVerifier, AMLAnomalyDetector, BiometricKYC, ComplianceSmartContract,
    SentimentAnalyzer, LifestyleSegmenter, StabilityForecaster, EthicalAI, utility_function,
    ESGDataAggregator, ESGScorer, ImpactMeasurer, ESGPortfolioOptimizer, ESGVisualizer,
    LoanRecommender, LoanStructurer, LoanGuidanceChatbot, FinancialLiteracyGame, CrossSelling
)

# Initialize Flask app and enable CORS for cross-origin requests.
app = Flask(__name__)
CORS(app)


class MicroFinanceBackend:
    """
    MicroFinanceBackend integrates all AI components from the micro-finance platform.
    """
    def __init__(self) -> None:
        # Creditworthiness Assessment Components
        self.alt_data_fusion: AlternativeDataFusion = AlternativeDataFusion(input_size=5)
        self.gnn: GraphNeuralNetwork = GraphNeuralNetwork(size=5)
        self.federated_scoring: FederatedCreditScoring = FederatedCreditScoring(num_institutions=3)
        self.dynamic_scoring: DynamicCreditScoring = DynamicCreditScoring()

        # Compliance Automation Components
        self.kyc: DecentralizedKYC = DecentralizedKYC()
        self.doc_verifier: DocumentVerifier = DocumentVerifier()
        self.aml_detector: AMLAnomalyDetector = AMLAnomalyDetector(size=5)
        self.biometric_kyc: BiometricKYC = BiometricKYC()
        self.compliance_contract: ComplianceSmartContract = ComplianceSmartContract()

        # Behavioral Analysis Components
        self.sentiment_analyzer: SentimentAnalyzer = SentimentAnalyzer(size=3)
        self.lifestyle_segmenter: LifestyleSegmenter = LifestyleSegmenter(n_groups=3)
        self.stability_forecaster: StabilityForecaster = StabilityForecaster(size=3)
        self.ethical_ai: EthicalAI = EthicalAI(strength=1.0)

        # ESG Tracking and Scoring Components
        self.esg_aggregator: ESGDataAggregator = ESGDataAggregator()
        self.esg_scorer: ESGScorer = ESGScorer()
        self.impact_measurer: ImpactMeasurer = ImpactMeasurer(size=3)
        self.esg_optimizer: ESGPortfolioOptimizer = ESGPortfolioOptimizer()
        self.esg_visualizer: ESGVisualizer = ESGVisualizer()

        # Loan Recommendation System Components
        self.loan_recommender: LoanRecommender = LoanRecommender(users=5, items=5)
        self.loan_structurer: LoanStructurer = LoanStructurer()
        self.chatbot: LoanGuidanceChatbot = LoanGuidanceChatbot()
        self.game: FinancialLiteracyGame = FinancialLiteracyGame()
        self.cross_selling: CrossSelling = CrossSelling()

    def assess_creditworthiness(self, data: List[float], social_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Assess creditworthiness using alternative data and optional social network data.
        
        Args:
            data (List[float]): List of financial features.
            social_data (Optional[Dict[str, Any]]): Optional dict with 'nodes' and 'connections'.
        
        Returns:
            Dict[str, Any]: A dictionary containing various credit scores.
        """
        alt_score = self.alt_data_fusion.predict(data)
        if social_data:
            nodes: List[float] = social_data.get('nodes', [])
            connections: List[List[float]] = social_data.get('connections', [])
            gnn_score = self.gnn.predict(nodes, connections)
            final_score = (alt_score + sum(gnn_score) / len(gnn_score)) / 2
        else:
            final_score = alt_score
            gnn_score = None
        federated_score = self.federated_scoring.predict(data)
        self.dynamic_scoring.update(data, final_score)
        dynamic_score = self.dynamic_scoring.predict()
        return {
            'alternative_score': alt_score,
            'gnn_score': gnn_score,
            'final_score': final_score,
            'federated_score': federated_score,
            'dynamic_score': dynamic_score
        }

    def verify_compliance(self, user_data: Any, document_text: str, transaction_data: List[float],
                          bio_data: Optional[List[float]] = None, contract_id: Optional[str] = None,
                          conditions: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Verifies compliance including KYC, document verification, AML, biometric KYC, and smart contract compliance.
        
        Args:
            user_data (Any): Data for KYC verification.
            document_text (str): Document text to check.
            transaction_data (List[float]): Transaction features for AML detection.
            bio_data (Optional[List[float]]): Optional biometric data.
            contract_id (Optional[str]): Optional contract ID.
            conditions (Optional[Dict[str, Any]]): Optional compliance conditions.
        
        Returns:
            Dict[str, Any]: A dictionary with verification results.
        """
        kyc_verified = self.kyc.verify(user_data)
        doc_verified = self.doc_verifier.check(document_text)
        anomaly_detected = self.aml_detector.detect(transaction_data)
        bio_verified = self.biometric_kyc.verify(user_data, bio_data) if bio_data else True
        contract_compliance = self.compliance_contract.check(contract_id, conditions) if contract_id and conditions else True
        compliance_status = kyc_verified and doc_verified and not anomaly_detected and bio_verified and contract_compliance
        return {
            'kyc_verified': kyc_verified,
            'doc_verified': doc_verified,
            'anomaly_detected': anomaly_detected,
            'bio_verified': bio_verified,
            'contract_compliance': contract_compliance,
            'compliance_status': compliance_status
        }

    def analyze_behavior(self, features: List[float]) -> Dict[str, Any]:
        """
        Analyze user behavior including sentiment, lifestyle segmentation, stability forecast,
        privacy protection, and utility score.
        
        Args:
            features (List[float]): List of behavioral features.
        
        Returns:
            Dict[str, Any]: Analysis results.
        """
        sentiment = self.sentiment_analyzer.predict(features)
        lifestyle_group = self.lifestyle_segmenter.predict(features)
        stability = self.stability_forecaster.predict(features)
        private_features = self.ethical_ai.veil(features)
        util_score = utility_function(features[0])  # For simplicity, using the first feature; can be extended.
        return {
            'sentiment': sentiment,
            'lifestyle_group': lifestyle_group,
            'stability': stability,
            'private_features': private_features,
            'utility_score': util_score
        }

    def track_esg(self, source_data: Dict[str, List[float]], factors: List[float], impact_data: List[float],
                  risk: float = 0.5) -> Dict[str, Any]:
        """
        Tracks and scores ESG metrics, optimizes portfolio, and visualizes ESG data.
        
        Args:
            source_data (Dict[str, List[float]]): ESG data from multiple sources.
            factors (List[float]): ESG factors for scoring.
            impact_data (List[float]): Data for impact measurement.
            risk (float, optional): Risk level for optimization.
        
        Returns:
            Dict[str, Any]: Aggregated ESG information.
        """
        aggregated_data = self.esg_aggregator.blend(source_data)
        esg_score = self.esg_scorer.score(factors)
        impact = self.impact_measurer.ripple(impact_data)
        optimized_balance = self.esg_optimizer.balance(esg_score, risk)
        visualization = self.esg_visualizer.map(source_data)
        return {
            'aggregated_data': aggregated_data,
            'esg_score': esg_score,
            'impact': impact,
            'optimized_balance': optimized_balance,
            'visualization': visualization
        }

    def recommend_loans(self, user_id: int, score: float, risk: float,
                        query: Optional[str] = None, action: Optional[float] = None,
                        transactions: Optional[List[Any]] = None) -> Dict[str, Any]:
        """
        Recommends loans, structures loan terms, provides chatbot guidance, gamifies learning,
        and suggests cross-selling products.
        
        Args:
            user_id (int): User identifier.
            score (float): Credit score.
            risk (float): Risk level.
            query (Optional[str]): Optional chatbot query.
            action (Optional[float]): Optional action for gamification.
            transactions (Optional[List[Any]]): Optional list of transactions.
        
        Returns:
            Dict[str, Any]: Loan recommendation details.
        """
        recommendations = self.loan_recommender.flow(user_id)
        loan_terms = self.loan_structurer.terms(score, risk)
        chatbot_response = self.chatbot.match(query) if query else None
        game_reward = self.game.play(action) if action is not None else None
        if transactions:
            # Assuming transactions is a list of transaction items.
            self.cross_selling.pulse([transactions])
            cross_sell_recommendations = self.cross_selling.recommend(transactions[-1])
        else:
            cross_sell_recommendations = None
        return {
            'recommendations': recommendations,
            'loan_terms': loan_terms,
            'chatbot_response': chatbot_response,
            'game_reward': game_reward,
            'cross_sell_recommendations': cross_sell_recommendations
        }

    def train_models(self, training_data: Dict[str, Any]) -> None:
        """
        Trains models with provided training data.
        
        Args:
            training_data (Dict[str, Any]): Data for model training.
        """
        if 'alt_data' in training_data and 'targets' in training_data:
            self.alt_data_fusion.train(training_data['alt_data'], training_data['targets'])
        # Additional model training logic can be added here.

    def set_compliance_rule(self, contract_id: str, conditions: Dict[str, Any]) -> None:
        """
        Sets a compliance rule for a given contract.
        
        Args:
            contract_id (str): Contract identifier.
            conditions (Dict[str, Any]): Conditions for compliance.
        """
        self.compliance_contract.set_rule(contract_id, conditions)

    def enroll_biometric(self, user_id: Any, bio_data: List[float]) -> None:
        """
        Enrolls a user with biometric data.
        
        Args:
            user_id (Any): User identifier.
            bio_data (List[float]): Biometric data.
        """
        self.biometric_kyc.enroll(user_id, bio_data)


# Instantiate the backend
backend = MicroFinanceBackend()


# ------------------------
# Flask API Endpoints
# ------------------------

@app.route('/assess_creditworthiness', methods=['POST'])
def assess_creditworthiness_endpoint() -> Any:
    """
    API endpoint to assess creditworthiness.
    
    Expects JSON with 'data' (required) and optional 'social_data'.
    """
    req_data = request.json
    data = req_data.get('data')
    social_data = req_data.get('social_data')
    if not data:
        return jsonify({'error': 'Missing data'}), 400
    result = backend.assess_creditworthiness(data, social_data)
    return jsonify(result)


@app.route('/verify-compliance', methods=['POST'])
def verify_compliance_endpoint():
    """
    API endpoint to verify compliance.
    
    Expects JSON with 'user_data', 'document_text', 'transaction_data' (required),
    and optional 'bio_data'.
    """
    try:
        data = request.get_json()
        user_data = data.get('user_data')
        document_text = data.get('document_text')
        transaction_data = data.get('transaction_data')
        bio_data = data.get('bio_data')

        if not all([user_data, document_text, transaction_data]):
            return jsonify({'error': 'Missing required data'}), 400

        # Verify KYC
        kyc_result = backend.kyc.verify(user_data)
        
        # Verify document
        doc_result = backend.doc_verifier.check(document_text)
        
        # Check for AML anomalies
        aml_result = backend.aml_detector.detect(transaction_data)
        
        # Verify biometric if provided
        bio_result = None
        if bio_data and user_data.get('idNumber'):
            bio_result = backend.biometric_kyc.verify(user_data['idNumber'], bio_data)

        response = {
            'kyc_verified': kyc_result,
            'document_verified': doc_result,
            'aml_check_passed': not aml_result,  # aml_result is True if anomaly detected
            'biometric_verified': bio_result
        }
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/enroll-biometric', methods=['POST'])
def enroll_biometric_endpoint():
    """
    API endpoint to enroll biometric data.
    
    Expects JSON with 'user_id' and 'bio_data' (required).
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        bio_data = data.get('bio_data')

        if not all([user_id, bio_data]):
            return jsonify({'error': 'Missing required data'}), 400

        # Enroll biometric data
        backend.biometric_kyc.enroll(user_id, bio_data)
        
        return jsonify({'message': 'Biometric data enrolled successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analyze_behavior', methods=['POST'])
def analyze_behavior_endpoint() -> Any:
    """
    API endpoint to analyze user behavior.
    
    Expects JSON with 'features' (required).
    """
    req_data = request.json
    features = req_data.get('features')
    if not features:
        return jsonify({'error': 'Missing features'}), 400
    result = backend.analyze_behavior(features)
    return jsonify(result)


@app.route('/track_esg', methods=['POST'])
def track_esg_endpoint() -> Any:
    """
    API endpoint to track ESG metrics.
    
    Expects JSON with 'source_data', 'factors', 'impact_data' (required) and optional 'risk'.
    """
    req_data = request.json
    source_data = req_data.get('source_data')
    factors = req_data.get('factors')
    impact_data = req_data.get('impact_data')
    risk = req_data.get('risk', 0.5)
    if not source_data or not factors or not impact_data:
        return jsonify({'error': 'Missing required data'}), 400
    result = backend.track_esg(source_data, factors, impact_data, risk)
    return jsonify(result)


@app.route('/recommend-loans', methods=['POST'])
def recommend_loans_endpoint():
    """
    API endpoint to recommend loans.
    
    Expects JSON with 'user_id', 'score', 'risk' (required) and optional 'query', 'action', and 'transactions'.
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        score = data.get('score')
        risk = data.get('risk')
        query = data.get('query', '')
        action = data.get('action', 0.0)
        transactions = data.get('transactions', [])

        # Get loan recommendations
        recommendations = backend.loan_recommender.flow(user_id)
        
        # Structure the loans
        loan_terms = backend.loan_structurer.terms(score, risk)
        
        # Get chatbot guidance if query provided
        guidance = backend.chatbot.match(query) if query else None
        
        # Update game score if action provided
        game_reward = backend.game.play(action) if action != 0.0 else None

        response = {
            'recommendations': recommendations,
            'terms': loan_terms,
            'guidance': guidance,
            'game_reward': game_reward
        }
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/submit-loan', methods=['POST'])
def submit_loan_endpoint():
    """
    API endpoint to submit a loan application.
    
    Expects JSON with application details.
    """
    try:
        data = request.get_json()
        # Process application data here
        # This is a placeholder - you would typically save this to a database
        return jsonify({'message': 'Application submitted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/train_models', methods=['POST'])
def train_models_endpoint() -> Any:
    """
    API endpoint to train models.
    
    Expects JSON with 'training_data' (required).
    """
    req_data = request.json
    training_data = req_data.get('training_data')
    if not training_data:
        return jsonify({'error': 'Missing training data'}), 400
    backend.train_models(training_data)
    return jsonify({'message': 'Models trained successfully'})


@app.route('/set_compliance_rule', methods=['POST'])
def set_compliance_rule_endpoint() -> Any:
    """
    API endpoint to set a compliance rule.
    
    Expects JSON with 'contract_id' and 'conditions' (required).
    """
    req_data = request.json
    contract_id = req_data.get('contract_id')
    conditions = req_data.get('conditions')
    if not contract_id or not conditions:
        return jsonify({'error': 'Missing contract ID or conditions'}), 400
    backend.set_compliance_rule(contract_id, conditions)
    return jsonify({'message': 'Compliance rule set successfully'})


if __name__ == '__main__':
    app.run(debug=True)