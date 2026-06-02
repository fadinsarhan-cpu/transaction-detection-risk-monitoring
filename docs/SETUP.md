# Project Setup Guide

This document explains how to obtain, configure and run the Transaction Detection & Risk Monitoring project from scratch. Following these steps will ensure that you can reproduce the analyses and dashboards included in this repository.

## 1. Clone the Repository

Use Git to clone the repository locally:

```
git clone https://github.com/fadinsarhan-cpu/transaction-detection-risk-monitoring.git
cd transaction-detection-risk-monitoring
```

Alternatively, download the project as a ZIP file from GitHub and extract it.

## 2. Create a Virtual Environment

It is recommended to work within a Python virtual environment to avoid dependency conflicts:

```
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

## 3. Install Dependencies

Once the virtual environment is active, install the required libraries listed in `requirements.txt`:

```
pip install -r requirements.txt
```

If you plan to run the machine learning notebook that uses SMOTE or XGBoost, ensure that your Python environment can compile any necessary dependencies (e.g., a C++ compiler).

## 4. Recommended Notebook Run Order

The analyses and dashboards build on one another. Run the notebooks in the following order to reproduce the workflow:

1. `notebooks/01_etl_transaction_risk.ipynb` – loads the raw data, cleans it, and saves a cleaned dataset to `data/processed/cleaned_transactions.csv`.
2. `notebooks/02_eda_exploration.ipynb` – explores the cleaned dataset and uncovers key patterns in the data.
3. `notebooks/03_statistical_analysis.ipynb` – performs hypothesis testing and account segmentation.
4. `notebooks/04_machine_learning.ipynb` – trains and evaluates several models to predict suspicious transactions.
5. `notebooks/05_dashboard_preparation.ipynb` – generates aggregated tables for the Power BI dashboard.
6. Open `dashboards/Dashboard_Fadi.pbix` in Power BI Desktop – connect the exported CSV tables from `dashboards/dashboard_data/` as data sources.

## 5. Running the Source Scripts

For automated workflows outside of Jupyter notebooks, the `src/` package contains reusable Python modules:

* `src/data_preprocessing.py` – functions to load, clean and enrich the raw data.
* `src/feature_engineering.py` – utilities to construct preprocessing pipelines.
* `src/model_training.py` – routines to train models, evaluate them, and save metrics.
* `src/utils.py` – helper functions for file operations and model persistence.

You can compile the scripts to check for syntax errors using:

```
python -m py_compile src/data_preprocessing.py
python -m py_compile src/feature_engineering.py
python -m py_compile src/model_training.py
python -m py_compile src/utils.py
```

## 6. Opening the Power BI Dashboard

The file `dashboards/Dashboard_Fadi.pbix` can be opened with Power BI Desktop. After running notebook 05, the folder `dashboards/dashboard_data/` will contain CSV files that serve as the dashboard’s data sources. Use **Get Data → Text/CSV** in Power BI Desktop to import each table and build your visuals.

## 7. Data Files

The repository expects the following data files to be present:

* `data/raw/SAML-D_reduced.txt` – raw synthetic transaction dataset.
* `data/processed/SAML-D_clean_optimized.zip` – compressed version of a previously cleaned dataset (optional).

Additional files placed into `data/raw/` (e.g., CSV or XLSX) should be documented, and sensitive information must be handled responsibly. Processed outputs are generated in `data/processed/` by the ETL notebook or preprocessing script.
