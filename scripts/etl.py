import pandas as pd

def run_etl():
    df = pd.read_csv("/Users/anujkandwal/Desktop/Saas Pricing Analytics and Revenue Simulation/data/raw/aws_saas_sales.csv")
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['profit'] = df['sales'] - df['cost']
    df['profit_margin'] = df['profit'] / df['sales']
    df.to_csv("data/processed/cleaned_sales_data.csv", index=False)
