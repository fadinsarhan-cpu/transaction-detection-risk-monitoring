# Transaction Detection & Risk Monitoring

## Title Page & Authors

**Title:** Transaction Detection & Risk Monitoring
**Author:** Fadi Sarhan (202020144)
**Supervisor:** Dr. Husam Barham
**University:** University of Petra
**Course:** 307498 – Graduation Project
**Semester:** Second Semester, 2025/2026
**Date:** June 3, 2026

## Table of Contents

* [Title Page & Authors](#title-page--authors)
* [Abstract](#abstract)
* [Acknowledgment](#acknowledgment)
* [Business Intelligence Project Description and Objectives](#business-intelligence-project-description-and-objectives)
* [Data Research and Acquiring Effort](#data-research-and-acquiring-effort)
* [Data Description and Understanding](#data-description-and-understanding)
* [Data Primary Cleaning and Transformation](#data-primary-cleaning-and-transformation)
* [Data Visualization and Insights](#data-visualization-and-insights)
* [Dashboard Design & Business Insights](#dashboard-design--business-insights)
* [Advanced Analytics and AI Modeling](#advanced-analytics-and-ai-modeling)
* [Tools Research and Selection Effort](#tools-research-and-selection-effort)
* [Project Deployment Effort / Use Case](#project-deployment-effort--use-case)
* [Results](#results)
* [References](#references)
* [Setup and Run Instructions](#setup-and-run-instructions)

## Abstract

The project **Transaction Detection & Risk Monitoring** focuses on analyzing financial transaction data to detect suspicious activities and monitor transaction risk. The main objective is to apply Business Intelligence and Data Analytics techniques to support the identification of potential fraud, money-laundering behavior, and high-risk transaction patterns.

The project uses a synthetic AML transaction dataset and follows a complete BI workflow: data acquisition, data cleaning, transformation, exploratory data analysis, visualization, dashboard design, and machine learning. The final solution supports compliance teams, risk managers, analysts, and decision-makers by providing KPIs, risk insights, suspicious transaction trends, and model-based detection support.

## Acknowledgment

I would like to thank **Dr. Husam Barham** for his guidance and support throughout this project. I also thank the **University of Petra**, my family, friends, and everyone who supported me during the completion of this graduation project.

## Business Intelligence Project Description and Objectives

This repository contains the code, data, notebooks, dashboard documentation, source scripts, and project documentation for a Business Intelligence graduation project focused on transaction detection and risk monitoring in a financial services context.

The goal of the project is to build a data-driven analytical workflow that can identify suspicious transaction patterns, support AML-style monitoring, and provide actionable insights to compliance and risk teams.

The main project objectives are:

1. Clean and prepare transaction data for analysis.
2. Explore suspicious transaction patterns and risk indicators.
3. Build dashboard-ready KPIs and visualizations.
4. Train and evaluate machine learning models for suspicious transaction detection.
5. Support compliance, investigation, and risk-monitoring decisions using Business Intelligence outputs.

The project is organized into the following phases:

1. **Data ingestion and preprocessing:** Raw transaction data is loaded, cleaned, and transformed into a structured format suitable for analysis.
2. **Exploratory data analysis:** Notebooks are used to study transaction distributions, suspicious activity patterns, and account-level risk indicators.
3. **Statistical analysis:** Statistical tests and risk segmentation are used to better understand transaction behavior and laundering indicators.
4. **Machine learning:** Classification models are trained and compared to detect suspicious transactions.
5. **Dashboarding:** Dashboard-ready tables and Power BI documentation are prepared to support business users and analysts.
6. **Documentation:** Markdown documentation explains the project methodology, tools, deployment use case, results, and final audit.

## Data Research and Acquiring Effort

Real banking transaction data is usually private, sensitive, and restricted because of confidentiality, privacy, and financial security regulations. For this reason, the project uses the **SAML-D synthetic AML transaction dataset**, which is suitable for academic AML-style transaction monitoring and suspicious activity analysis.

The dataset was selected because it contains transaction-level records and a target label indicating laundering or suspicious activity. This makes it suitable for Business Intelligence analysis, dashboard design, and supervised machine learning classification.

More details are available in [`docs/02_data_research.md`](docs/02_data_research.md) and [`docs/03_raw_data_links.md`](docs/03_raw_data_links.md).

## Data Description and Understanding

The dataset contains transaction-level records that describe the movement of funds between sender and receiver accounts. The main fields include sender account, receiver account, transaction amount, payment currency, received currency, sender bank location, receiver bank location, payment type, laundering label, laundering type, and transaction date/time.

The target variable used for suspicious transaction detection is the laundering indicator, which identifies whether a transaction is normal or suspicious/laundering-related.

A detailed data dictionary is available in [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md).

## Data Primary Cleaning and Transformation

The data cleaning and transformation process prepares the raw dataset for analysis, modeling, and dashboarding. The process includes loading the raw transaction file, standardizing column names, handling missing values, converting data types, removing duplicate records, preparing the target variable, and saving the processed dataset for later stages.

The processed dataset is used by the EDA notebooks, statistical analysis notebook, machine learning notebook, and dashboard preparation notebook.

More details are available in [`docs/05_cleaning_transformation.md`](docs/05_cleaning_transformation.md).

## Data Visualization and Insights

The project includes exploratory visualizations and dashboard-ready outputs to understand suspicious transaction behavior. Key visual areas include suspicious transactions by payment type, suspicious transactions by currency, transaction amount patterns, account-level risk, transaction trends, and laundering-related behavior.

These visualizations support business users by showing where suspicious activity is concentrated and which accounts, transaction types, or patterns require more attention.

More details are available in [`docs/06_visualization_insights.md`](docs/06_visualization_insights.md).

## Dashboard Design & Business Insights

The dashboard converts analytical outputs into business insights for executives, compliance teams, risk managers, and investigators. A detailed explanation of each dashboard page is available in [`dashboards/dashboard_description.md`](dashboards/dashboard_description.md).

The Power BI file `Dashboard_Fadi.pbix` is large and may not be tracked directly in this repository. If it is not included in GitHub, it should be delivered separately or managed using Git LFS. Dashboard screenshots should be stored in `dashboards/dashboard_screenshots/`.

The dashboard is designed around six main pages:

1. **Executive Overview:** High-level KPIs, suspicious transaction rate, total transaction volume, suspicious amount, and transaction trends.
2. **Transaction Risk Monitoring:** Suspicious transactions by payment type, currency, bank, and time.
3. **High-Risk Accounts:** Top sender and receiver accounts, account-level risk bands, and suspicious ratios.
4. **Typology Analysis:** Laundering behavior categories and suspicious amount by typology, if available.
5. **Model Performance:** Confusion matrix, precision, recall, F1-score, ROC/AUC, and model comparison.
6. **Investigation Detail:** Transaction-level table with filters for analyst review.

Key KPIs include:

| KPI                         | Purpose                                                 |
| --------------------------- | ------------------------------------------------------- |
| Total transactions          | Provides the overall monitored transaction volume.      |
| Suspicious transactions     | Shows the main AML/risk detection count.                |
| Suspicious transaction rate | Indicates the concentration of suspicious activity.     |
| Total suspicious amount     | Measures possible financial exposure.                   |
| High-risk accounts          | Helps prioritize investigation work.                    |
| Suspicious by currency      | Supports currency-level risk monitoring.                |
| Suspicious by payment type  | Highlights risky transaction channels.                  |
| Model recall                | Measures the model’s ability to catch suspicious cases. |
| False positive rate         | Indicates analyst workload caused by incorrect alerts.  |

By combining KPIs, charts, and transaction-level details, the dashboard supports both high-level monitoring and case-level investigation.

## Advanced Analytics and AI Modeling

The project includes a machine learning pipeline to classify transactions as normal or suspicious. Detailed methodology and model documentation are available in [`docs/07_ai_modeling.md`](docs/07_ai_modeling.md), and model results are summarized in [`models/model_metrics.md`](models/model_metrics.md).

The modeling workflow includes feature preparation, class imbalance handling, train/test split, model training, model comparison, and evaluation. The models considered include a baseline model, Logistic Regression, Random Forest, and XGBoost if available.

The evaluation metrics include accuracy, precision, recall, F1-score, ROC-AUC, and confusion matrix interpretation. In AML and suspicious transaction monitoring, **recall** is especially important because missing suspicious transactions can be more serious than producing false alerts. However, false positives also matter because they increase analyst workload.

Model comparison outputs are stored in [`models/model_comparison.csv`](models/model_comparison.csv), and supporting model-result documentation is available in [`images/model_results/README.md`](images/model_results/README.md).

## Tools Research and Selection Effort

The project uses a combination of open-source and BI tools to support the full analytics workflow. Python and pandas are used for data preparation, Jupyter Notebook is used for analysis and experimentation, scikit-learn and XGBoost support machine learning, Power BI supports dashboarding, and GitHub is used for version control and final submission.

A full tools comparison and justification is available in [`docs/08_tools_selection.md`](docs/08_tools_selection.md).

The selected tools support the full BI lifecycle:

```text
data acquisition → cleaning → analysis → modeling → dashboarding → decision support
```

## Project Deployment Effort / Use Case

The deployment use case explains how the project could be used by a bank, financial institution, compliance team, AML analyst, or risk department. The goal is to make the analysis usable by business users through dashboard monitoring, risk scoring, and investigation support.

The business workflow is:

```text
Raw Transactions → ETL/Cleaning → Feature Engineering → ML Risk Scoring → Power BI Dashboard → AML Analyst Review
```

A full deployment explanation is available in [`docs/09_deployment_use_case.md`](docs/09_deployment_use_case.md), and the architecture diagram is documented in [`images/architecture_diagram.md`](images/architecture_diagram.md).

## Results

The project produced a complete Business Intelligence workflow for transaction risk monitoring. The main outputs include:

1. A cleaned and processed transaction dataset.
2. ETL, EDA, statistical analysis, machine learning, and dashboard preparation notebooks.
3. Dashboard-ready CSV exports.
4. Dashboard design documentation.
5. Model metrics and model comparison files.
6. Source scripts for preprocessing, feature engineering, model training, and utilities.
7. A data dictionary and setup documentation.
8. A final completion audit report.

The main business result is a risk-monitoring structure that helps identify suspicious transaction patterns, high-risk accounts, risky payment types, and areas where compliance analysts should focus their investigation efforts.

## References

* Kaggle. Anti Money Laundering Transaction Data (SAML-D). Retrieved June 3, 2026.
* University of Petra GP_BI20252 Business Intelligence Graduation Project Template.
* Project documentation files in the [`docs/`](docs/) folder.

## Setup and Run Instructions

For a full setup guide, see [`docs/SETUP.md`](docs/SETUP.md).

### Install dependencies

Create a virtual environment and install the required packages:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Recommended run order

Run the notebooks in this order:

1. `notebooks/01_etl_transaction_risk.ipynb`
2. `notebooks/02_eda_exploration.ipynb`
3. `notebooks/03_statistical_analysis.ipynb`
4. `notebooks/04_machine_learning.ipynb`
5. `notebooks/05_dashboard_preparation.ipynb`

### Run source scripts

Source scripts are stored in `src/`:

```bash
python src/data_preprocessing.py
python src/model_training.py
```

### Dashboard usage

Dashboard-ready files are generated in `dashboards/dashboard_data/`. Open the Power BI dashboard file in Power BI Desktop if it is available locally, or use the dashboard documentation and screenshots in the `dashboards/` folder.

## Repository Structure

```text
transaction-detection-risk-monitoring/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── docs/
│   ├── 00_title_page_authors.md
│   ├── 01_project_description.md
│   ├── 02_data_research.md
│   ├── 03_raw_data_links.md
│   ├── 04_data_description.md
│   ├── 05_cleaning_transformation.md
│   ├── 06_visualization_insights.md
│   ├── 07_ai_modeling.md
│   ├── 08_tools_selection.md
│   ├── 09_deployment_use_case.md
│   ├── 10_results.md
│   ├── 11_references.md
│   ├── SETUP.md
│   ├── DATA_DICTIONARY.md
│   └── FINAL_COMPLETION_AUDIT.md
├── data/
│   ├── raw/
│   │   ├── README.md
│   │   └── SAML-D_reduced.txt
│   └── processed/
│       ├── README.md
│       └── SAML-D_clean_optimized.zip
├── notebooks/
│   ├── 01_etl_transaction_risk.ipynb
│   ├── 02_eda_exploration.ipynb
│   ├── 03_statistical_analysis.ipynb
│   ├── 04_machine_learning.ipynb
│   └── 05_dashboard_preparation.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── utils.py
├── dashboards/
│   ├── dashboard_description.md
│   ├── dashboard_data/
│   └── dashboard_screenshots/
├── models/
│   ├── model_metrics.md
│   └── model_comparison.csv
└── images/
    ├── architecture_diagram.md
    └── model_results/
```

## License

This project is licensed under the terms of the MIT license. See the [`LICENSE`](LICENSE) file for details.
