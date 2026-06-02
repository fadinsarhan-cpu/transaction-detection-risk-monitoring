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
