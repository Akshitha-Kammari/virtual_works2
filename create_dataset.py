import pandas as pd
import numpy as np

data = {
    "CustomerID": range(1, 101),
    "Age": np.random.randint(18, 60, 100),
    "Tenure": np.random.randint(1, 24, 100),
    "MonthlyCharges": np.random.randint(200, 1000, 100),
    "TotalUsage": np.random.randint(10, 100, 100),
    "LoginFrequency": np.random.randint(1, 30, 100),
    "Churn": np.random.choice(["Yes", "No"], 100)
}

df = pd.DataFrame(data)
df.to_excel("dataset.xlsx", index=False)

print("Dataset created successfully")