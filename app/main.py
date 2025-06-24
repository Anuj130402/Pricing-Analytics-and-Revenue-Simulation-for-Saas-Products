from fastapi import FastAPI
from app.logic import load_forecast_data, simulate_price_change, get_kpis
from app.models import PriceSimInput

app = FastAPI(title="SaaS Pricing Analytics API")

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/forecast")
def forecast():
    data = load_forecast_data()
    return data.to_dict(orient="records")

@app.post("/simulate-price-change")
def simulate(data: PriceSimInput):
    result = simulate_price_change(data.percent_increase)
    return result.to_dict(orient="records")

@app.get("/kpis")
def kpis():
    return get_kpis()
