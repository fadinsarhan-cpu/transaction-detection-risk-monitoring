# Data Description and Understanding

The SAML‑D dataset includes 12 numerical and categorical features describing each transaction. Key fields include:

- **sender_id** and **receiver_id**: anonymised identifiers for the sending and receiving accounts;
- **timestamp**: transaction time and date;
- **amount**: transaction value in synthetic currency units;
- **transaction_type**: categorical code for payment type (transfer, withdrawal, deposit, etc.);
- **channel**: channel used (online, ATM, branch);
- **typology**: label indicating the pattern of behaviour (normal or one of the suspicious typologies);

Other columns capture geographic region, transaction country, currency and risk level. A separate label column marks each transaction as **normal** (legitimate) or **suspicious**.

Descriptive analysis shows that the dataset is highly imbalanced: only about 0.1039 % of transactions are suspicious. The distribution of transaction amounts is right‑skewed with heavy tails. Suspicious transactions often occur in bursts with specific patterns of sender–receiver relationships.

We performed exploratory statistics to understand ranges, outliers and correlations. These insights guided the feature engineering and model selection described in later sections.
