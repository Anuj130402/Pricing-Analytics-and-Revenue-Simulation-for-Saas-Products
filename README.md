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

## Folder Structure
Request you to follow the same structure as given.

## Key Notes (Folder-Wise):

- 'data' folder contains .csv files (raw and processed) which can be further examined and analyzed using Excel.
- 'Notebooks' folder, although contains only one .ipynb file, however can be structured into a more concise 2-3 .ipynb files where every file performs different functions.
- 'db' folder contains the database that we export. It is important to note that every time an instance of the Jupyter Lab will run, the database will get updated. So keep in mind the duplicate values that you might generate.
- 'app' folder contains the files for API backend using FastAPI. Before you run, make sure to import all the necessary libraries into the folder. Also make sure you create the folder in the 'app' folder itself, otherwise it will not run and will show 'Internal Server Error'.
- 'etl', 'scripts', 'airflow' folders are optional if you do not want to automate the above process. I have used docker for the same purpose and have provided the .yaml file for the same. Again, be sure the import all the necessay libraries before you run.



