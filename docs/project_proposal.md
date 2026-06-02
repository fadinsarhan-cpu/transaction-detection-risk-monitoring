# Transaction Detection & Risk Monitoring – Project Proposal

## Background and Motivation

Money laundering poses a serious threat to the integrity of financial systems. Criminals exploit the complexity of global payment networks to conceal illicit funds among millions of legitimate transactions. Traditional rule‑based monitoring systems struggle to adapt to evolving fraud patterns and generate a high volume of false positives. Modern data‑driven approaches offer the potential to improve detection accuracy while reducing operational overhead.

## Problem Statement

Given a large volume of transaction data from a financial institution, we need to identify suspicious payments that may be indicative of money laundering or other illicit activities. The dataset is highly imbalanced, with suspicious transactions comprising only a tiny fraction of total volume. The challenge is to design a system that can detect these rare events without flagging too many legitimate transactions.

## Objectives

- **Data acquisition and preparation:** Obtain a representative dataset for anti‑money‑laundering research, ingest it into a secure environment and perform ETL to produce a clean analysis‑ready dataset.
- **Exploratory analysis:** Understand the statistical properties of normal and suspicious transactions, identify influential variables and uncover patterns or anomalies.
- **Modelling:** Develop and evaluate machine‑learning models capable of classifying transactions as normal or suspicious, with emphasis on high recall and low false‑positive rates.
- **Dashboarding:** Create an interactive dashboard that visualises transaction flows, risk metrics and model outputs to support analysts in their decision‑making.
- **Documentation:** Maintain clear documentation and reproducible code to facilitate future maintenance and extension of the system.

## Data Source

We will use the **SAML‑D** dataset, a synthetic anti money‑laundering dataset available on Kaggle. It contains roughly 9.5 million transactions, 12 features and 28 typology labels. Only about 0.1039 % of records are labelled as suspicious, mirroring the class imbalance found in real‑world banking data.

## Methodology

1. **ETL and Data Cleaning:** Load the raw CSV data, handle missing values, filter invalid records, encode categorical variables and scale numerical features. Generate a processed dataset stored in a Parquet file.
2. **Exploratory Data Analysis:** Produce summary statistics and visualisations to understand distributions, correlations and anomalies. This phase informs feature engineering and model selection.
3. **Model Development:** Train multiple classifiers (logistic regression, random forest, XGBoost) using the processed data. Use resampling techniques to address class imbalance and evaluate models using recall and AUC.
4. **Model Evaluation and Selection:** Compare models via cross‑validation, choose the best performing one and analyse feature importance.
5. **Dashboard and Deployment:** Build an interactive dashboard in Power BI that displays aggregate metrics, risk scores and allows drill‑down into individual transactions. Design a deployment architecture for integrating the model into a live monitoring system.

## Tools and Technologies

- **Python / Jupyter:** For data manipulation and machine learning (pandas, NumPy, scikit‑learn, XGBoost, imbalanced‑learn).
- **Power BI:** For interactive dashboards and reporting.
- **GitHub:** For version control and collaboration.
- **Kaggle API:** For data acquisition.

## Expected Deliverables

- Cleaned and processed dataset (not committed to GitHub due to size).
- Jupyter notebooks demonstrating ETL, EDA, statistical analysis and modelling.
- Trained machine‑learning model saved to the `models/` directory.
- Power BI dashboard file (.pbix) in the `dashboards/` directory.
- Comprehensive documentation in Markdown covering all phases of the project.
- This project proposal document outlining the plan and rationale.

## Timeline

| Phase                    | Description                                | Duration |
|-------------------------|--------------------------------------------|---------|
| Data acquisition & ETL  | Download and clean the dataset             | 1 week  |
| Exploratory analysis    | Generate descriptive statistics & visuals   | 1 week  |
| Modelling               | Train and evaluate multiple classifiers     | 2 weeks |
| Dashboard development   | Build interactive reports in Power BI       | 1 week  |
| Documentation & review  | Write final report and prepare for defence | 1 week  |

## Conclusion

The proposed project will leverage modern data‑analytics and machine‑learning techniques to enhance transaction monitoring for anti money‑laundering compliance. By the end of the project we expect to deliver a reproducible pipeline, a high‑performing detection model, an interactive dashboard and a comprehensive report summarising our findings and recommendations.
