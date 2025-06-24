# Pricing-Analytics-and-Revenue-Simulation-for-Saas-Products
A live project involving an end-to-end analytics system to understand sales patterns, forecast future revenue, and simulate the impact of price changes using real-world-like sales data.
# Pricing Analytics & Revenue Simulation – SaaS Sales Data

An end-to-end data analytics project for simulating pricing strategies and forecasting revenue using real-world SaaS sales data.

---

## Overview

- Forecast revenue using Prophet
- Simulate price changes & impact on profit
- Tableau dashboard for insights
- Automated pipeline with Airflow
- REST API with FastAPI

---

## Tech Stack

| Component       | Tools Used                    |
|----------------|-------------------------------|
| Data Wrangling  | Python, Pandas, NumPy         |
| Forecasting     | Prophet                       |
| Simulation      | Scikit-learn                  |
| Visualization   | Tableau                       |
| API             | FastAPI, Pydantic             |
| Automation      | Apache Airflow                |

---

## 📁 Folder Structure
project/
├── dags/ ← Airflow DAGs
├── scripts/ ← ETL, Forecast, Simulate scripts
├── data/
│ └── processed/ ← Cleaned & forecasted CSVs
├── api/ ← FastAPI code
└── README.md

