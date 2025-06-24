import pandas as pd
import sqlite3

def clean_and_engineer(filepath):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['order_month'] = df['order_date'].dt.to_period('M').astype(str)
    df = df.dropna(subset=['order_date', 'sales', 'profit', 'discount'])
    df['profit_margin'] = df['profit'] / df['sales']
    df['is_high_discount'] = df['discount'] > 0.2
    df['order_month'] = df['order_date'].dt.to_period('M').astype(str)
    return df

def save_to_db(df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql('sales_data', conn, if_exists='replace', index=False)

if __name__ == "__main__":
    df_clean = clean_and_engineer("/Users/anujkandwal/Desktop/Saas Pricing Analytics and Revenue Simulation/data/raw/aws_saas_sales.csv")
    save_to_db(df_clean, "/Users/anujkandwal/Desktop/Saas Pricing Analytics and Revenue Simulation/db/saas_sales.db")
