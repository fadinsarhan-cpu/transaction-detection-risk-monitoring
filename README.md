# Transaction Detection & Risk Monitoring

This repository contains the complete documentation and assets for a Business Intelligence graduation project titled *Transaction Detection & Risk Monitoring*. The project focuses on detecting suspicious financial transactions using a synthetic anti‑money‑laundering dataset and presenting the results via interactive dashboards.

##**Title Page & Authors**
Authors

Fadi Sarhan (202020144)
Supervised by:

Dr.Husam Barham
University:

University Of Petra
Course:

307498 – Graduation Project
Semester:

Second Semester, 2025/2026
Date:

Date: June 3, 2026
## Abstract

Financial institutions must identify illicit transactions while minimising disruption to legitimate customers. We built an end‑to‑end pipeline that ingests raw transaction data, cleans and enriches it, applies machine‑learning models to assess risk, and visualises insights via a Power BI dashboard. The project demonstrates how data‑driven methods can improve AML monitoring and compliance.

## Project overview

The core of this project is a synthetic transaction dataset (SAML‑D) containing 9.5 million records with 12 features and 28 typology labels. The workflow covers:

1. ETL and data cleaning using Python and pandas;
2. Exploratory data analysis and feature engineering in Jupyter notebooks;
3. Machine‑learning models (logistic regression, random forest, XGBoost) developed with scikit‑learn and XGBoost;
4. Dashboard design in Power BI to visualise risk metrics and flagged transactions.

## Objectives

- Build a reproducible ETL pipeline for transaction data.
- Explore and understand the characteristics of normal versus suspicious transactions.
- Develop a classification model that can detect suspicious transactions with high recall.
- Design an interactive dashboard for analysts and stakeholders.
- Summarise the business impact of the modelling approach.

## Repository structure

```
.
├── README.md                 – high‑level overview and links.
├── docs/                     – detailed documentation for each project phase.
├── data/                     – local folders for raw and processed data (not committed).
│   ├── raw/
│   └── processed/
├── notebooks/                – Jupyter notebooks for ETL, EDA, statistical analysis and modelling.
├── src/                      – Python scripts used in the project.
├── models/                   – saved machine‑learning models.
├── dashboards/               – Power BI dashboard file(s).
└── images/                   – figures and screenshots used in the docs.
```

## Tools used

- Python, pandas, NumPy, scikit‑learn, XGBoost
- Imbalanced‑learn for resampling
- Jupyter notebooks
- Power BI for dashboarding
- GitHub for version control

## Dashboard

The Power BI report is stored in the `dashboards/` folder. To view it, open the `.pbix` file in Power BI Desktop.

## Table of contents

- [Project description and objectives](docs/01_project_description.md)
- [Data research and acquiring effort](docs/02_data_research.md)
- [Links to raw data](docs/03_raw_data_links.md)
- [Data description and understanding](docs/04_data_description.md)
- [Data cleaning and transformation](docs/05_cleaning_transformation.md)
- [Data visualisation and dashboard insights](docs/06_visualization_insights.md)
- [Advanced analytics and AI modelling](docs/07_ai_modeling.md)
- [Tools research and selection](docs/08_tools_selection.md)
- [Deployment / use case](docs/09_deployment_use_case.md)
- [Results](docs/10_results.md)
- [References](docs/11_references.md)

Please refer to the `docs/` folder for in‑depth documentation.
