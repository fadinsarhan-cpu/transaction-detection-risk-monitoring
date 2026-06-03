<!--
  This README provides an overview of the Business Intelligence graduation project
  on transaction detection and risk monitoring. It introduces the objectives,
  describes the structure of the repository and explains how to reproduce the
  results. The content in this document replaces the original placeholder
  README and is intended for submission to the University of Petra.
-->

# Transaction Detection & Risk Monitoring

This repository contains the code, data and documentation for a Business
Intelligence graduation project that explores **transaction detection** and
**risk monitoring** in a financial services context.  The goal of the project
is to build a data‑driven system that can flag suspicious transactions and
provide actionable insights to compliance teams.

## Project overview

The project consists of several phases:

1. **Data ingestion and preprocessing:** Raw payment data is ingested and
   converted into a clean tabular format.  Scripts in `src/data_preprocessing.py`
   and `src/feature_engineering.py` handle missing values, derive new
   attributes and normalise the fields for modelling.

2. **Exploratory data analysis (EDA):** The notebooks in the `notebooks/`
   directory perform an exploratory analysis to understand the distribution of
   normal vs. suspicious behaviour.  Charts and summary statistics are saved
   under `images/eda_charts/`.

3. **Modelling:** Supervised models are trained to classify transactions as
   normal or suspicious.  The training pipeline, hyper‑parameter tuning and
   evaluation metrics are defined in `src/model_training.py`.  Model
   performance is summarised in `models/model_metrics.md`, and result figures
   are stored in `images/model_results/`.

4. **Dashboarding:** Interactive dashboards are implemented using Plotly
   Dash and/or other visualization libraries.  Markdown documentation for
   dashboards lives in `dashboards/dashboard_description.md`, and screenshots
   should be placed in `dashboards/dashboard_screenshots/`.  A notebook
   demonstrating the preparation of dashboard data is provided at
   `notebooks/05_dashboard_preparation.ipynb`.

5. **Documentation:** The `docs/` folder contains a series of markdown files
   detailing project requirements, data research, cleaning steps, modelling
   choices and deployment considerations.  These documents complement this
   README and serve as a formal report for the graduation project.

## Repository structure

```text
├── README.md                 ← Project overview and instructions (you are here)
├── LICENSE                   ← License information
├── .gitignore                ← Files and folders excluded from version control
├── requirements.txt          ← Python dependencies with pinned versions
├── docs/                     ← Detailed project documentation
├── data/
│   ├── raw/                  ← Original datasets (keep `SAML-D_reduced.txt` here)
│   │   └── README.md         ← Notes about raw data
│   └── processed/            ← Cleaned datasets ready for analysis
│       └── README.md         ← Notes about processed data
├── notebooks/                ← Jupyter notebooks for ETL, EDA, modelling, dashboards
│   └── 05_dashboard_preparation.ipynb ← Prepares data for dashboards
├── src/
│   ├── data_preprocessing.py ← Functions for cleaning and transforming raw data
│   ├── feature_engineering.py← Feature extraction and selection
│   ├── model_training.py      ← Training and evaluating ML models
│   └── utils.py               ← Reusable helper functions
├── dashboards/
│   ├── dashboard_description.md ← Explanation of dashboard design and usage
│   └── dashboard_screenshots/    ← Screenshots of dashboards
├── models/
│   └── model_metrics.md      ← Evaluation metrics and discussion of model performance
└── images/
    ├── eda_charts/           ← Plots produced during exploratory analysis
    └── model_results/        ← Visualisations of model outputs
```

## Getting started

1. **Install dependencies**

   Create a virtual environment (optional) and install the required packages:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the notebooks**

   Launch JupyterLab and open the notebooks in the `notebooks/` directory to
   reproduce the ETL, EDA and modelling steps:

   ```bash
   jupyter lab
   ```

3. **Train models**

   You can run the training pipeline as a script:

   ```bash
   python src/model_training.py --config configs/train_config.yaml
   ```

   Adjust the training script and configuration as needed for your chosen
   algorithms and hyper‑parameters.

4. **Build dashboards**

   Once the data is prepared, use Plotly Dash or another BI tool to
   implement interactive dashboards.  Refer to
   `dashboards/dashboard_description.md` for guidance.

## Contributing

This repository is maintained for educational purposes.  Contributions are
welcome via pull requests.  Please ensure that new code follows the existing
style conventions and includes appropriate documentation.

## License

This project is licensed under the terms of the MIT license.  See the
`LICENSE` file for details.

## Reproducibility and Run Order

For a step‑by‑step guide to running the project from scratch, consult
[`docs/SETUP.md`](docs/SETUP.md).  That document covers cloning the
repository, creating a virtual environment, installing dependencies and
executing the notebooks in the correct sequence.  All notebooks and scripts
are designed to use **relative paths** via `pathlib.Path`, so the
repository can be moved between machines without breaking file references.

The expected order of execution is:

1. **01_etl_transaction_risk.ipynb** – cleanse and enrich the raw data, saving
   a tidy CSV to `data/processed/cleaned_transactions.csv`.
2. **02_eda_exploration.ipynb** – perform exploratory analysis to
   understand patterns in the cleaned data.
3. **03_statistical_analysis.ipynb** – run hypothesis tests and create
   account‑level risk bands.
4. **04_machine_learning.ipynb** – train and compare models for
   detecting suspicious transactions.  Evaluation metrics are written to
   `models/model_metrics.md` and `models/model_comparison.csv`.
5. **05_dashboard_preparation.ipynb** – generate aggregated tables for the
   Power BI dashboard.  Outputs are saved to `dashboards/dashboard_data/`.

After executing the notebooks, you can open
`dashboards/Dashboard_Fadi.pbix` in Power BI Desktop and connect the
generated CSV files as data sources.  Processed outputs and models are
deterministically derived from the raw data, ensuring that results can be
reproduced on other systems.

## Dashboard Design & Business Insights

The interactive dashboard turns raw analytics into actionable insights for
executives, risk managers and investigators.  A detailed description of
each dashboard page is provided in
[`dashboards/dashboard_description.md`](dashboards/dashboard_description.md).
Because the Power BI file (`Dashboard_Fadi.pbix`) is large, it is **not
tracked** in this repository; download it separately or use Git LFS as
explained in the dashboard documentation.  Final screenshots of the
dashboard pages should be stored in
`dashboards/dashboard_screenshots/`.

The dashboard consists of six pages:

1. **Executive Overview** – high‑level KPIs and a transaction trend.
2. **Transaction Risk Monitoring** – suspicious transactions by payment type,
   currency, bank and over time.
3. **High‑Risk Accounts** – top sender/receiver accounts and risk band
   summaries.
4. **Typology Analysis** – distribution of typology codes and suspicious
   amounts (if available).
5. **Model Performance** – confusion matrix, precision/recall/F1 metrics,
   ROC/AUC curves and a model comparison table.
6. **Investigation Detail** – transaction‑level table with filters for
   date, account, payment type, currency, risk band and model prediction.

### Key KPIs

| KPI                         | Purpose                                           |
| --------------------------- | ------------------------------------------------- |
| Total transactions          | Provides context for risk metrics.                |
| Suspicious transactions     | Main AML/risk detection count.                    |
| Suspicious transaction rate | Indicates the concentration of suspicious activity |
| Total suspicious amount     | Measures potential financial exposure.            |
| High‑risk accounts          | Helps prioritise investigations.                  |
| Top sender/receiver banks   | Shows where risk is concentrated on the origin and destination sides. |
| Suspicious by currency      | Supports currency‑level risk monitoring.          |
| Suspicious by payment type  | Highlights risky transaction channels.           |
| Model recall                | Reflects the model’s ability to catch suspicious cases. |
| False positive rate         | Indicates analyst workload due to incorrect alerts. |

By combining KPIs, distribution charts and a detailed transaction table,
the dashboard supports both high‑level monitoring and case‑level
investigation.  Decision‑makers can quickly identify where risk is
concentrated and drill down into individual transactions.

## Advanced Analytics and AI Modeling

The project includes a machine‑learning pipeline to classify transactions
as suspicious or normal.  Detailed methodology and results are documented
in [`docs/07_ai_modeling.md`](docs/07_ai_modeling.md), with the latest
metrics summarised in [`models/model_metrics.md`](models/model_metrics.md).

The pipeline trains and compares several algorithms — a baseline classifier,
logistic regression with class weights, a random forest and (optionally)
XGBoost — using the cleaned dataset.  The notebook
`notebooks/04_machine_learning.ipynb` handles feature preparation,
class‑imbalance mitigation, model training, metric computation and result
export.  Performance metrics are saved to `models/model_comparison.csv`.

In an AML context, **recall** is more important than accuracy or precision:
missing a suspicious transaction could allow illicit activity to go
undetected.  However, high‑recall models often produce many false
positives, increasing analyst workload.  The model comparison table helps
stakeholders understand this trade‑off and choose a model that balances
risk appetite and operational capacity.  See `docs/07_ai_modeling.md`
for a full discussion of the modelling objective, evaluation metrics,
confusion matrix interpretation, feature importance and limitations.

## Tools Research and Selection

A variety of open‑source and commercial tools were evaluated for this project.  Python, pandas and Jupyter Notebooks were selected for data preparation and analysis; scikit‑learn and optional XGBoost provide the machine‑learning algorithms; Power BI delivers the final dashboard; and GitHub manages version control and submission.  A full comparison of selected tools, justifications and alternative options is provided in [docs/08_tools_selection.md](docs/08_tools_selection.md).

## Project Deployment Effort / Use Case

Turning the analysis into a usable solution requires a clear business workflow and deployment architecture.  In summary, transactions are ingested and cleaned, features are engineered, models assign risk scores, high‑risk cases are flagged, and the Power BI dashboard enables users to monitor KPIs and drill into individual transactions.  See [docs/09_deployment_use_case.md](docs/09_deployment_use_case.md) for the full workflow, target user descriptions, operational considerations and limitations.  A high‑level architecture diagram is available in [images/architecture_diagram.md](images/architecture_diagram.md).
