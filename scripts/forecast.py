from prophet import Prophet
import pandas as pd

def run_forecast():
    df = pd.read_csv("/Users/anujkandwal/Desktop/Saas Pricing Analytics and Revenue Simulation/data/processed/cleaned_sales_data.csv")
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['order_month'] = df['order_date'].dt.to_period('M').dt.to_timestamp()
    revenue = df.groupby('order_month')['sales'].sum().reset_index()
    revenue.columns = ['ds', 'y']

    model = Prophet()
    model.fit(revenue)
    future = model.make_future_dataframe(periods=6, freq='M')
    forecast = model.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(
        "data/processed/forecast_monthly_revenue.csv", index=False
    )
