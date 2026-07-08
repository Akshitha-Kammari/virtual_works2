import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("dataset.xlsx")

# Display first rows
print("First 5 rows:")
print(df.head())

# Churn count
print("\nChurn Count:")
print(df["Churn"].value_counts())

# Churn chart
df["Churn"].value_counts().plot(kind="bar")
plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()