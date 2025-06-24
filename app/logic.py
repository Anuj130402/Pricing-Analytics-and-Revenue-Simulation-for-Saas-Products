import pandas as pd
from prophet import Prophet

def load_forecast_data():
    df = pd.read_csv("/Users/anujkandwal/Desktop/Saas Pricing Analytics and Revenue Simulation/data/processed/forecast_monthly_revenue.csv")
    return df

def simulate_price_change(percent_increase: float):
    df = pd.read_csv("/Users/anujkandwal/Desktop/Saas Pricing Analytics and Revenue Simulation/data/processed/simulated_sales.csv")
    df['adjusted_sales'] = df.apply(
        lambda row: row['Sales'] * (1 + percent_increase / 100)
        if row['Discount'] < 0.1 else row['Sales'], axis=1
    )
    result = df.groupby('order_date')['adjusted_sales'].sum().reset_index()
    return result

def get_kpis():
    df = pd.read_csv("/Users/anujkandwal/Desktop/Saas Pricing Analytics and Revenue Simulation/data/processed/cleaned_sales_data.csv")
    return {
        "total_sales": round(df['Sales'].sum(), 2),
        "total_profit": round(df['Profit'].sum(), 2),
        "avg_margin": round((df['Profit'] / df['Sales']).mean(), 3),
        "avg_discount": round(df['Discount'].mean(), 3)
    }
