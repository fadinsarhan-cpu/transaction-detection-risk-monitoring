# Data Cleaning and Transformation

The ETL process is implemented in the notebook `01_etl_transaction_risk.ipynb`. The main steps include:

1. **Loading** the raw CSV files and merging them into a single dataset.
2. **Handling missing values** by imputing or removing records depending on the feature.
3. **Filtering invalid records**, such as transactions with negative amounts or impossible timestamps.
4. **Encoding categorical variables** (transaction type, channel, country) using one‑hot encoding.
5. **Scaling numerical features** such as amount and time intervals using standardisation.
6. **Addressing class imbalance** by constructing balanced training sets with under‑sampling of normal transactions.
7. **Saving the cleaned dataset** to `data/processed/transactions_cleaned.parquet` for downstream use.

These transformations ensure that the machine‑learning models receive consistent and meaningful inputs.
