import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/ASAMOAH/Desktop/Case Study/UNICEF Case Study/malnutrition_data.csv")

# Data Analysis
def analyze_data():
    # Malnutrition Distribution
    malnutrition_distribution = df["Malnutrition_Status"].value_counts(normalize=True) * 100
    print("Malnutrition Distribution (%):\n", malnutrition_distribution)

    # Malnutrition by Urban vs Rural
    urban_rural = df.groupby("Urban_or_Rural")["Malnutrition_Status"].value_counts(normalize=True).unstack() * 100
    print("\nMalnutrition by Urban vs Rural (%):\n", urban_rural)

    # Parental Education Impact
    education_impact = df.groupby("Parental_Education")["Malnutrition_Status"].value_counts(normalize=True).unstack() * 100
    print("\nImpact of Parental Education (%):\n", education_impact)

    # Meal Frequency and Household Income Correlation
    correlation = df[["Daily_Meals", "Household_Income"]].corr()
    print("\nCorrelation between Daily Meals and Household Income:\n", correlation)

if __name__ == "__main__":
    analyze_data()
