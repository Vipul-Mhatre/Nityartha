import pandas as pd
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
loans_df = pd.read_csv('data/kiva_loans.csv')
loan_themes_df = pd.read_csv('data/loan_themes_by_region.csv')
mpi_locations_df = pd.read_csv('data/kiva_mpi_region_locations.csv')

# 1. Sentiment Analysis on Loan Descriptions
def get_sentiment(text):
    """Compute sentiment polarity of text."""
    return TextBlob(str(text)).sentiment.polarity

loans_df['sentiment'] = loans_df['use'].apply(get_sentiment)

# Sentiment by Sector
sector_sentiment = loans_df.groupby('sector')['sentiment'].mean().sort_values(ascending=False)
print("Sentiment by Sector:\n", sector_sentiment)

plt.figure(figsize=(12, 6))
sector_sentiment.plot(kind='bar')
plt.title('Average Sentiment by Loan Sector')
plt.xlabel('Sector')
plt.ylabel('Sentiment Polarity')
plt.tight_layout()
plt.savefig('outputs/sector_sentiment.png')
plt.close()

# 2. Geographical Distribution of Loans
country_loan_count = loans_df['country'].value_counts()
country_loan_amount = loans_df.groupby('country')['loan_amount'].sum()

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
country_loan_count.head(10).plot(kind='bar')
plt.title('Number of Loans by Country')
plt.xlabel('Country')
plt.ylabel('Number of Loans')

plt.subplot(1, 2, 2)
country_loan_amount.head(10).plot(kind='bar')
plt.title('Total Loan Amount by Country')
plt.xlabel('Country')
plt.ylabel('Total Loan Amount')
plt.tight_layout()
plt.savefig('outputs/loan_geography.png')
plt.close()

# 3. Relationship between Loan Themes and Poverty Indices
# Merge loan themes with MPI locations
loan_themes_mpi = pd.merge(
    loan_themes_df, 
    mpi_locations_df[['LocationName', 'MPI']], 
    left_on='LocationName', 
    right_on='LocationName', 
    how='inner'
)

# Average loan amount by region and MPI
region_mpi_loans = loan_themes_mpi.groupby('region').agg({
    'amount': 'mean', 
    'MPI': 'first'
}).sort_values('MPI')

plt.figure(figsize=(15, 6))
plt.scatter(region_mpi_loans['MPI'], region_mpi_loans['amount'])
plt.title('Loan Amount vs Multidimensional Poverty Index by Region')
plt.xlabel('Multidimensional Poverty Index')
plt.ylabel('Average Loan Amount')
plt.tight_layout()
plt.savefig('outputs/mpi_loan_relationship.png')
plt.close()

# Correlation between MPI and Loan Amount
correlation = region_mpi_loans['MPI'].corr(region_mpi_loans['amount'])
print(f"\nCorrelation between MPI and Loan Amount: {correlation}")

# Theme distribution across poverty levels
theme_mpi = loan_themes_mpi.groupby('Loan Theme Type').agg({
    'MPI': ['mean', 'count']
}).sort_values(('MPI', 'mean'), ascending=False)
print("\nLoan Themes across Poverty Levels:\n", theme_mpi)

# Save detailed results
sector_sentiment.to_csv('outputs/sector_sentiment.csv')
country_loan_count.to_csv('outputs/country_loan_count.csv')
country_loan_amount.to_csv('outputs/country_loan_amount.csv')
region_mpi_loans.to_csv('outputs/region_mpi_loans.csv')
theme_mpi.to_csv('outputs/theme_mpi.csv')

print("\nAnalysis complete. Check the 'outputs' directory for detailed results and visualizations.")
