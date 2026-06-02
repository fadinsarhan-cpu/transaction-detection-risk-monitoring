# Links to Raw Data

The raw transaction dataset can be obtained from Kaggle:

- [Anti Money Laundering Transaction Data (SAML-D)](https://www.kaggle.com/datasets/berkanoztas/synthetic-transaction-monitoring-dataset-aml)

To download the dataset via the Kaggle API, run:

```
kaggle datasets download -d berkanoztas/synthetic-transaction-monitoring-dataset-aml
```

Extract the downloaded archive and place the CSV files in `data/raw/`. **Do not commit the raw data** to GitHub because of its size and licensing.

## Cleaned Dataset

After cleaning the raw SAML-D dataset – including missing-value imputation, outlier removal, one-hot encoding of categorical variables, scaling of numeric variables and addressing class imbalance – the processed dataset is saved to the `data/processed/` folder. Because the cleaned dataset is still large, we do not commit it to GitHub. If you wish to reproduce the analysis, run the cleaning notebook in `notebooks/` or scripts in `src/` to generate the cleaned dataset yourself.
