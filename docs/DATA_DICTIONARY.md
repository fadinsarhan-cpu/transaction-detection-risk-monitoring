# Data Dictionary

This document describes the key fields used in the **Transaction Detection & Risk Monitoring** project. The processed dataset is stored in `data/processed/SAML-D_clean_optimized.zip` and contains transaction-level features for analysis, dashboarding, and machine-learning modelling.

| Column | Description | Example Use |
| --- | --- | --- |
| `Sender_account` | Account identifier for the sender of the transaction. | Sender-level aggregation and high-risk account detection. |
| `Receiver_account` | Account identifier for the receiver of the transaction. | Receiver-level aggregation and investigation drill-down. |
| `Amount` | Monetary value of the transaction. | Amount bands, suspicious amount totals, and risk scoring. |
| `Payment_currency` | Currency used to send the payment. | Currency-level risk monitoring. |
| `Received_currency` | Currency received by the destination account. | FX/currency conversion pattern analysis. |
| `Sender_bank_location` | Sender bank location or country. | Geographic and source-bank risk concentration analysis. |
| `Receiver_bank_location` | Receiver bank location or country. | Destination-bank risk concentration analysis. |
| `Payment_type` | Payment channel or transfer type. | Suspicious transaction analysis by payment type. |
| `Is_laundering` | Binary target variable: `0` = normal / non-suspicious, `1` = suspicious / laundering transaction. | Machine-learning target and dashboard suspicious-count KPI. |
| `Laundering_type` | Typology or laundering pattern label where available. | Typology analysis and investigation context. |
| `Datetime` | Timestamp of the transaction. | Time-series trends and dashboard date filtering. |

## Derived Features

The notebooks and source scripts may create additional analysis features, including:

| Derived Feature | Description |
| --- | --- |
| `amount_band` | Groups transaction amounts into low, medium, high, and very high ranges. |
| `large_transaction_flag` | Flags unusually large transactions based on an amount threshold. |
| `sender_risk_ratio` | Measures the proportion of suspicious activity associated with a sender account. |
| `risk_band` | Categorises accounts or transactions into risk groups for dashboard filtering. |

These derived fields are generated during preprocessing, feature engineering, and dashboard preparation rather than being part of the original raw dataset.
