import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:/Users/ASAMOAH/Desktop/Case Study/UNICEF Case Study/malnutrition_data.csv")

# Data Visualization
def visualize_data():
    sns.set(style="whitegrid")

    # 1. Malnutrition Status Distribution
    plt.figure(figsize=(8, 6))
    malnutrition_counts = df["Malnutrition_Status"].value_counts()
    sns.barplot(x=malnutrition_counts.index, y=malnutrition_counts.values, palette="viridis")
    plt.title("Malnutrition Status Distribution")
    plt.xlabel("Malnutrition Status")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    # 2. Malnutrition by Urban vs Rural
    urban_rural = df.groupby("Urban_or_Rural")["Malnutrition_Status"].value_counts().unstack()
    urban_rural.plot(kind="bar", stacked=True, colormap="coolwarm", figsize=(10, 6))
    plt.title("Malnutrition by Urban vs Rural")
    plt.xlabel("Location")
    plt.ylabel("Count")
    plt.legend(title="Malnutrition Status")
    plt.tight_layout()
    plt.show()

    # 3. Heatmap of Correlations
    plt.figure(figsize=(8, 6))
    correlation_matrix = df[["Age", "Daily_Meals", "Household_Income"]].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

    # 4. Pie Chart: Parental Education
    plt.figure(figsize=(8, 6))
    parental_education = df["Parental_Education"].value_counts()
    plt.pie(parental_education, labels=parental_education.index, autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
    plt.title("Parental Education Levels")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_data()
