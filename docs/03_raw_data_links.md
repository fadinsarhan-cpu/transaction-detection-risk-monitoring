# Links to Raw Data

The raw transaction dataset can be obtained from Kaggle:

- [Anti Money Laundering Transaction Data (SAML‑D)](https://www.kaggle.com/datasets/berkanoztas/synthetic-transaction-monitoring-dataset-aml)

To download the dataset via the Kaggle API run:

```
kaggle datasets download -d berkanoztas/synthetic-transaction-monitoring-dataset-aml
```

Extract the downloaded archive and place the CSV files in `data/raw/`. Do not commit the raw data to GitHub because of its size and licensing.

The cleaned dataset produced after applying our data cleaning pipeline is also available for download:

- [SAML‑D_clean.csv](https://media.githubusercontent.com/media/AlonaDrok/Anti-Money-Laundering-Transaction-Detection---CAPSTONE-PROJECT-2026/refs/heads/main/jupyter_notebooks/data/processed/SAML-D_clean.csv) – this file contains the processed version of the SAML‑D dataset after we performed missing-value imputation, outlier removal, one‑hot encoding and scaling. We have not committed the cleaned CSV to GitHub because of its size. You can download it from this link if you wish to reproduce the analysis.
