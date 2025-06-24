import pandas as pd

def run_simulation():
    df = pd.read_csv("/Users/anujkandwal/Desktop/Saas Pricing Analytics and Revenue Simulation/data/processed/cleaned_sales_data.csv")
    df['simulated_sales'] = df.apply(
        lambda row: row['sales'] * 1.10 if row['discount'] < 0.1 else row['sales'],
        axis=1
    )
    df.to_csv("data/processed/simulated_sales.csv", index=False)
