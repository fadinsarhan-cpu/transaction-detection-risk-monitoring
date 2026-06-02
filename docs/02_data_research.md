# Data Research and Acquiring Effort

This project uses a publicly available synthetic dataset for anti‑money‑laundering (AML) transaction monitoring. The dataset, called **SAML‑D (Synthetic Anti Money Laundering Dataset)**, was published on Kaggle by Berk Oztaş to support research on transaction monitoring techniques.

The dataset comprises approximately 9.5 million transactions with 12 features and 28 typology labels. Only about 0.1 % of transactions are suspicious, which simulates the imbalance encountered in real banking data. The typology labels represent different patterns of legitimate and illicit behaviour.

We obtained the data by downloading it from Kaggle using the Kaggle API. The Kaggle dataset page provides a full description of the features, typologies and network graphs that accompany the data.

To comply with the university guidelines we did not commit the raw data to this repository. Instead, we store it in the **data/raw** folder on a local drive. Instructions on how to download the dataset are provided below.
