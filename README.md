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

1. [Abstract](#abstract)
2. [Acknowledgment](#acknowledgment)
3. [Business Intelligence Project Description and Objectives](#business-intelligence-project-description-and-objectives)
4. [Data Research and Acquiring Effort](#data-research-and-acquiring-effort)
5. [Data Description and Understanding](#data-description-and-understanding)
6. [Data Primary Cleaning and Transformation](#data-primary-cleaning-and-transformation)
7. [Data Visualization and Insights](#data-visualization-and-insights)
8. [Dashboard Design & Business Insights](#dashboard-design--business-insights)
9. [Advanced Analytics and AI Modeling](#advanced-analytics-and-ai-modeling)
10. [Tools Research and Selection Effort](#tools-research-and-selection-effort)
11. [Project Deployment Effort – Use Case](#project-deployment-effort--use-case)
12. [Results](#results)
13. [References](#references)

## Abstract

The project **Transaction Detection & Risk Monitoring** focuses on analyzing financial transaction data to detect suspicious activities and monitor transaction risk. The main objective of this project is to apply Business Intelligence and Data Analytics techniques to support the identification of potential fraud and money-laundering patterns. By transforming raw transaction data into meaningful insights, the project aims to help decision-makers understand risk levels, detect unusual behavior, and improve monitoring processes.

The implementation approach includes data acquisition, data cleaning, data transformation, exploratory data analysis, visualization, dashboard development, and advanced analytics. Python was used for data processing, cleaning, statistical analysis, and machine learning modeling. Power BI was used to design an interactive dashboard that presents key indicators, transaction patterns, risk levels, and suspicious activity insights. Machine learning techniques were also applied to support suspicious transaction detection and risk classification.

The project resulted in a complete Business Intelligence solution that provides clear visual insights into financial transactions and risk behavior. The dashboard helps users monitor transaction activity, identify high-risk patterns, and support faster decision-making. Overall, the project demonstrates how Business Intelligence, data analytics, and AI modeling can be used together to improve fraud detection, strengthen financial risk monitoring, and support better data-driven decisions.

## Acknowledgment

I would like to thank **Dr. Husam Barham** for his guidance and support throughout this project. I also thank the **University of Petra**, my family, friends, and everyone who supported me during the completion of **Transaction Detection & Risk Monitoring**.

## Business Intelligence Project Description and Objectives

For this project, I searched for a financial transaction dataset that could support transaction detection, suspicious activity analysis, and risk monitoring. Since real banking data is private and difficult to access, I used a synthetic anti-money laundering dataset that is safe for academic and analytical use.

The main dataset used is **SAML-D: Synthetic Anti-Money Laundering Transaction Dataset** from Kaggle. It contains transaction records with labels showing whether transactions are suspicious or normal, making it suitable for dashboards, risk analysis, and machine learning classification.

The data was acquired by downloading the dataset from Kaggle. No API or web scraping was used because the dataset was already available as a downloadable file. After downloading, the dataset was reduced and optimized so it could be used in the project and uploaded to GitHub.

### Data Source

| Source                       | Link                                                 | Description                                                                                              |
| ---------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| SAML-D Synthetic AML Dataset | Kaggle: Synthetic Transaction Monitoring Dataset AML | Main transaction dataset used to analyze suspicious activity, transaction risk, and laundering patterns. |

### Project Data Files

| File                         | Location          | Purpose                                                                     |
| ---------------------------- | ----------------- | --------------------------------------------------------------------------- |
| `SAML-D_reduced.txt`         | `data/raw/`       | Raw reduced dataset used as the starting point.                             |
| `SAML-D_clean_optimized.zip` | `data/processed/` | Cleaned and compressed dataset used for analysis, dashboards, and modeling. |

The dataset was used for data cleaning, exploratory analysis, dashboard development, feature engineering, and machine learning model training for detecting suspicious transactions.

## Data Research and Acquiring Effort

For this project, I searched for financial transaction datasets that could support suspicious transaction detection, fraud analysis, and anti-money laundering risk monitoring. Since real banking transaction data is usually private and difficult to access because of confidentiality and security regulations, I focused on publicly available synthetic datasets that simulate realistic financial transactions while still being safe to use for academic analysis.

The main dataset used in this project is the **Anti Money Laundering Transaction Data (SAML-D)** dataset, available on Kaggle. This dataset was selected because it contains transaction records designed for anti-money laundering and transaction monitoring research. It includes financial transaction records with labels that indicate suspicious or laundering-related activity, making it suitable for data cleaning, exploratory analysis, dashboard development, and machine learning modeling.

The data was acquired manually from Kaggle by downloading the raw dataset files and preparing a reduced version for project development and GitHub storage. No web scraping or API integration was required because the dataset was already available as a downloadable public dataset.

Raw data source: **Anti Money Laundering Transaction Data (SAML-D) – Kaggle**. This dataset contains synthetic financial transaction records created for AML transaction monitoring. It is useful for identifying suspicious patterns, analyzing transaction behavior, and training machine learning models for risk classification.

The dataset was used as the main raw data source for the project. After acquisition, it was cleaned, optimized, and transformed into a processed dataset suitable for analysis, visualization, dashboard design, and AI modeling.

More details are available in [`docs/02_data_research.md`](docs/02_data_research.md) and [`docs/03_raw_data_links.md`](docs/03_raw_data_links.md).

## Data Description and Understanding

The dataset used in this project is a financial transaction dataset designed for anti-money laundering and suspicious transaction monitoring. It contains transaction-level records with information about sender accounts, receiver accounts, transaction amount, currencies, bank locations, payment methods, laundering labels, laundering types, and transaction date and time. The cleaned dataset contains **950,486 transactions** and **11 fields**.

### Data Dictionary

| Field Name               | Description                                                                                                       | Why It Matters                                                                                |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `Sender_account`         | The account number of the person or entity sending the money.                                                     | Helps identify sender behavior and repeated suspicious activity.                              |
| `Receiver_account`       | The account number of the person or entity receiving the money.                                                   | Helps detect suspicious receivers and unusual money flow.                                     |
| `Amount`                 | The value of the transaction.                                                                                     | Important for identifying high-value transactions and risk patterns.                          |
| `Payment_currency`       | The currency used to send the payment.                                                                            | Helps analyze currency-based transaction behavior and international risk.                     |
| `Received_currency`      | The currency received by the receiver.                                                                            | Useful for detecting currency conversion and cross-border transaction patterns.               |
| `Sender_bank_location`   | The country/location of the sender’s bank.                                                                        | Helps identify geographic risk and source locations of transactions.                          |
| `Receiver_bank_location` | The country/location of the receiver’s bank.                                                                      | Helps analyze destination risk and cross-border money movement.                               |
| `Payment_type`           | The method used for the transaction, such as cheque, credit card, debit card, ACH, cash, or cross-border payment. | Helps compare risk levels between different transaction methods.                              |
| `Is_laundering`          | A label showing whether the transaction is laundering-related or normal.                                          | This is the main target field used for suspicious transaction detection and machine learning. |
| `Laundering_type`        | The transaction behavior type or laundering pattern.                                                              | Helps understand the type of activity and classify transaction behavior.                      |
| `Datetime`               | The date and time when the transaction occurred.                                                                  | Useful for time-based analysis, trends, and monitoring transaction activity over time.        |

### Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the structure, distribution, and behavior of the transaction data before building the dashboard and machine learning model. The analysis focused on transaction amounts, payment methods, laundering labels, currencies, bank locations, and transaction patterns over time.

The data showed that the majority of transactions are normal, while only a small number are labeled as laundering-related. This indicates that the dataset is highly imbalanced, which is common in fraud and anti-money laundering problems. This imbalance is important because machine learning models may become biased toward normal transactions if the laundering class is not handled properly.

Several charts and visualizations were used during the EDA process, including transaction amount distribution, laundering vs. non-laundering count, payment type distribution, currency distribution, sender and receiver bank location analysis, and laundering type analysis. These visualizations helped identify which transaction methods, locations, and transaction patterns are more relevant to risk monitoring.

The analysis also showed that transaction amount has a relationship with suspicious activity, although it is not the only factor that determines risk. Other fields, such as payment type, bank location, currency, and laundering type, also provide important information for identifying unusual behavior. These relationships supported the project objective of building a Business Intelligence dashboard and machine learning model that help detect suspicious transaction patterns and improve financial risk monitoring.

A detailed data dictionary is also available in [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md).

## Data Primary Cleaning and Transformation

The data preparation process started by loading the raw SAML-D transaction dataset into Python using the pandas library. The raw data was reviewed to understand its structure, column names, data types, and the overall quality of the transaction records before applying any cleaning or transformation steps.

The first transformation step was converting the required fields into suitable data types. The transaction amount field was converted into a numeric format to allow statistical analysis, aggregation, and machine learning processing. The date and time fields were also converted into a proper datetime format, which made it possible to analyze transaction trends over time and extract time-based insights.

Missing values were checked across the dataset. Records with missing values in important fields such as transaction amount, sender account, or receiver account were removed because these fields are essential for transaction analysis and risk monitoring. This helped ensure that the cleaned dataset contained complete and reliable transaction records.

Since the project used one main transaction dataset, no major dataset merging was required. However, the data was transformed and prepared for different project needs, including exploratory data analysis, dashboard visualization, and machine learning modeling. Some aggregations were applied during the analysis stage, such as grouping transactions by payment type, laundering label, currency, sender account, receiver account, and bank location to identify patterns and risk behavior.

Additional transformations included standardizing the transaction structure, keeping the relevant fields, preparing the laundering label as the target variable, and saving the cleaned dataset as a processed file. The final cleaned and optimized dataset was then used for visualization, statistical analysis, dashboard creation, and AI modeling.

More details are available in [`docs/05_cleaning_transformation.md`](docs/05_cleaning_transformation.md).

## Data Visualization and Insights

The dashboard was created in Power BI to monitor suspicious transaction activity and highlight key risk patterns.

### Main KPIs

| KPI                          |   Value | Insight                                                        |
| ---------------------------- | ------: | -------------------------------------------------------------- |
| Total Transaction Volume     |    950K | Large transaction dataset analyzed.                            |
| Suspicious Alerts            |    1011 | Total suspicious transactions detected.                        |
| Alert Rate                   |   0.00% | Suspicious cases are very rare compared to total transactions. |
| Suspicious Transaction Value | £47.14M | Suspicious activity has high financial impact.                 |

### Key Visualizations

**1. Suspicious Alerts by Month and Payment Type**
Shows how suspicious alerts change across months for different payment methods.
**Insight:** Suspicious activity appears throughout the year, with stronger activity in some months, especially around the beginning and end of the year.

**2. Transactions by Payment Type**
Compares transaction volume across payment methods such as credit card, cheque, debit card, ACH, cross-border, cash withdrawal, and cash deposit.
**Insight:** Credit card, cheque, debit card, and ACH have the highest transaction volumes, making them important channels for monitoring.

**3. Suspicious Alerts by Laundering Type**
Shows which laundering patterns produced the most alerts.
**Insight:** Structuring is the highest suspicious pattern, followed by cash withdrawal and smurfing.

**4. Transaction Amount by Laundering Type**
Compares the total transaction value for each laundering type.
**Insight:** Some laundering types may not have the highest number of alerts but still represent a large financial value, so both alert count and transaction value should be considered.

### Overall Insight

The dashboard shows that suspicious activity is rare but financially significant. The main risk patterns are linked to specific payment types and laundering methods, especially structuring, cash withdrawal, and smurfing. This helps prioritize which transaction behaviors should be monitored more closely.

More details are available in [`docs/06_visualization_insights.md`](docs/06_visualization_insights.md).

## Dashboard Design & Business Insights

The final BI dashboard was designed in Power BI to help monitor suspicious transaction activity, identify high-risk payment channels, and understand which laundering patterns create the highest business risk.

### Business Questions Answered

1. How many transactions were analyzed?
2. How many suspicious alerts were detected?
3. What is the total suspicious transaction value?
4. Which payment types are linked to suspicious activity?
5. Which laundering types appear most often?
6. Which laundering types have the highest financial impact?
7. Are suspicious alerts changing over time?

### Chart 1: KPI Summary Cards

**Description:**
This section shows the main project KPIs: total transaction volume, number of suspicious alerts, alert rate, and suspicious transaction value.

**Insight Derived:**
The business can quickly see the overall risk level. Although suspicious alerts are low compared to total transactions, the suspicious transaction value is high, which means even a small number of alerts can represent serious financial risk.

### Chart 2: Suspicious Alerts by Month and Payment Type

**Description:**
This line chart shows the number of suspicious alerts across each month, grouped by payment type.

**Insight Derived:**
The business can identify when suspicious activity increases and which payment methods are involved. This helps risk teams monitor specific months and payment channels more closely.

### Chart 3: Count of Transactions by Payment Type and Laundering Status

**Description:**
This bar chart compares transaction counts across payment types and separates normal transactions from suspicious ones.

**Insight Derived:**
The business can see which payment methods have the highest transaction activity. High-volume channels such as credit card, cheque, debit card, and ACH should receive stronger monitoring because more activity can increase exposure to suspicious behavior.

### Chart 4: Suspicious Alerts by Laundering Type

**Description:**
This chart ranks laundering types based on the number of suspicious alerts.

**Insight Derived:**
Structuring, cash withdrawal, and smurfing appear as the main suspicious patterns. This helps the business understand which laundering behaviors are most common and should be prioritized in risk rules and monitoring.

### Chart 5: Transaction Amount by Laundering Type

**Description:**
This chart shows the total transaction value for each laundering type.

**Insight Derived:**
Some laundering types may not have the highest number of alerts but still represent a large financial value. This is important because risk should be measured by both alert count and transaction amount.

### Overall Business Insight

The dashboard shows that suspicious activity is rare compared to total transactions, but it has a high financial impact. The most important risk areas are specific payment types and laundering patterns, especially structuring, cash withdrawal, and smurfing. These insights help the business focus monitoring efforts on the riskiest transaction behaviors and improve decision-making in financial risk detection.

A detailed dashboard description is available in [`dashboards/dashboard_description.md`](dashboards/dashboard_description.md). Dashboard screenshots should be stored in [`dashboards/dashboard_screenshots/`](dashboards/dashboard_screenshots/).

## Advanced Analytics and AI Modeling

This section explains the machine learning work completed for the **Transaction Detection & Risk Monitoring** project.

### Model Type

A predictive classification model was built to detect whether a transaction is suspicious or normal.

The target column predicted by the model is:

```text
is_laundering
```

| Value | Meaning                             |
| ----: | ----------------------------------- |
|     0 | Normal transaction                  |
|     1 | Suspicious / laundering transaction |

### Models Used

The project used pre-built machine learning models from scikit-learn:

| Model                        | Purpose                                      |
| ---------------------------- | -------------------------------------------- |
| Logistic Regression          | Baseline model for comparison                |
| Random Forest Classifier     | Main tree-based classification model         |
| Gradient Boosting Classifier | Additional model used to compare performance |

The project also used **SMOTE** to handle class imbalance because suspicious transactions are much fewer than normal transactions.

### What the Model Was Trying to Predict

The goal was to predict whether a transaction should be flagged as suspicious. This supports the business objective of identifying risky transactions that may require further investigation.

### Model Evaluation Metrics

The models were evaluated using:

| Metric    | Meaning                                                             |
| --------- | ------------------------------------------------------------------- |
| Accuracy  | Overall correct predictions                                         |
| Precision | How many predicted suspicious transactions were actually suspicious |
| Recall    | How many real suspicious transactions the model detected            |
| F1-score  | Balance between precision and recall                                |
| ROC-AUC   | Ability of the model to separate normal and suspicious transactions |

### Model Results

| Model               | ROC-AUC | Main Finding                                            |
| ------------------- | ------: | ------------------------------------------------------- |
| Logistic Regression |  0.5075 | Weak performance, close to random prediction            |
| Random Forest       |  0.5016 | High accuracy but poor suspicious transaction detection |
| Gradient Boosting   |  0.5804 | Best performing model, but still needs improvement      |

### Findings

The results show that Gradient Boosting performed the best, but the overall performance was still limited. This is mainly because the dataset is highly imbalanced, meaning suspicious transactions are rare compared to normal transactions.

Random Forest achieved high accuracy, but it did not perform well in detecting suspicious transactions. This shows that accuracy alone is not enough for fraud or laundering detection. In this type of project, recall and ROC-AUC are more important because the business needs to detect suspicious cases, not only predict normal transactions correctly.

### Business Insight

The AI modeling helped show that suspicious transaction detection is a challenging problem. Even though suspicious transactions are rare, they can have a high financial impact. The model can support risk monitoring by helping identify transactions that need further review, but future improvements should focus on better feature engineering, more behavioral indicators, and improved handling of imbalanced data.

More details are available in [`docs/07_ai_modeling.md`](docs/07_ai_modeling.md), [`models/model_metrics.md`](models/model_metrics.md), and [`models/model_comparison.csv`](models/model_comparison.csv).

## Tools Research and Selection Effort

Several tools were evaluated for this project to support data analysis, visualization, machine learning, and deployment. For data analysis, tools such as Python, R, and SQL were considered. Python was ultimately selected because it provides powerful libraries for data cleaning, transformation, statistical analysis, and machine learning, such as pandas, NumPy, Matplotlib, scikit-learn, and XGBoost.

For data visualization and dashboard development, tools such as Tableau, Power BI, and Looker were evaluated. Power BI was selected as the main visualization tool because it is user-friendly, supports interactive dashboards, provides strong filtering and reporting features, and is widely used in business intelligence projects. It was also suitable for presenting transaction risk indicators and suspicious activity patterns in a clear visual format.

For machine learning and advanced analytics, Python libraries were used because they support different classification models and allow flexible experimentation. Scikit-learn was used to build and evaluate predictive models, while other Python libraries supported data preprocessing, feature preparation, and model performance analysis.

For project deployment and presentation, tools such as Streamlit, Flask, FastAPI, and cloud platforms were considered. The final project focused mainly on Power BI dashboard delivery and GitHub documentation, while deployment tools were evaluated as possible future options for turning the model into an interactive web application.

Overall, the selected tools supported the project by covering the full Business Intelligence workflow: Python for data preparation and machine learning, Power BI for dashboard design and business insights, and GitHub for project organization, documentation, and sharing.

A full tools comparison and justification is available in [`docs/08_tools_selection.md`](docs/08_tools_selection.md).

## Project Deployment Effort – Use Case

The project is designed to be consumed by business users through an interactive Power BI dashboard. A business user, such as a risk analyst, compliance officer, or decision-maker, can use the dashboard to monitor transaction activity, identify suspicious transactions, review risk indicators, and understand patterns related to possible fraud or money laundering. The dashboard provides a simple visual interface that allows users to explore the data without needing technical knowledge of Python or machine learning.

The deployment process started by preparing and cleaning the raw transaction dataset using Python. After the data was cleaned and transformed, the processed dataset was exported and connected to Power BI. The dashboard was then designed using visual components such as KPI cards, bar charts, distribution charts, filters, and transaction risk summaries. These visuals were organized to answer key business questions related to suspicious activity, transaction volume, payment methods, currencies, and bank locations.

The implementation steps were completed in chronological order as follows: first, the raw dataset was acquired and reviewed; second, the data was cleaned and transformed using Python; third, exploratory data analysis and machine learning experiments were performed; fourth, the processed dataset was loaded into Power BI; fifth, the dashboard visuals and filters were designed; and finally, the project files, notebooks, dataset samples, and documentation were organized in GitHub for submission and review.

For this prototype, the main deployment method is a Power BI dashboard file supported by project documentation and Python notebooks. In a real business environment, the dashboard could be published to the Power BI Service, refreshed on a schedule, and shared with authorized users. Future deployment options may include adding a Streamlit web application, connecting the model to a live API, or integrating the dashboard with a real banking database.

Infrastructure considerations include secure data storage, access control, scheduled data refresh, user permissions, and data privacy. Since financial data is sensitive, any real deployment must protect customer information and follow compliance rules. Overall, the deployment use case demonstrates how the project can be used as a practical Business Intelligence solution for transaction monitoring and financial risk analysis.

A full deployment explanation is available in [`docs/09_deployment_use_case.md`](docs/09_deployment_use_case.md), and the architecture diagram is available in [`images/architecture_diagram.md`](images/architecture_diagram.md).

## Results

The project **Transaction Detection & Risk Monitoring** resulted in a complete Business Intelligence solution for analyzing financial transaction data and monitoring suspicious activity. The analysis showed that most transactions in the dataset were normal, while laundering-related transactions represented a much smaller portion. This finding confirmed that the dataset is highly imbalanced, which is common in fraud and anti-money laundering cases. The project also showed that transaction amount, payment type, currency, sender location, and receiver location are important factors for understanding transaction behavior and identifying potential risk patterns.

The most important insights came from the laundering vs. non-laundering transaction chart, payment type analysis, transaction amount distribution, and bank location analysis. These visualizations helped reveal how suspicious transactions differ from normal transactions and how risk can appear across different transaction methods and locations. The Power BI dashboard made these findings easier to understand by presenting the data through KPIs, charts, filters, and interactive visuals.

The machine learning results showed that suspicious transaction detection cannot depend on one feature only, such as transaction amount. The model performance was limited in the initial version, which indicates that better results require more feature engineering, additional behavioral indicators, and stronger handling of class imbalance. This result is important because it shows that fraud detection should combine dashboard analysis, risk indicators, and predictive modeling.

From a business perspective, the project can help financial institutions improve transaction monitoring, detect suspicious patterns faster, and support better decision-making. The dashboard allows business users to quickly identify risk areas and investigate unusual activity. It is recommended that future work include more advanced features such as customer behavior profiling, real-time transaction monitoring, automated alerts, scheduled dashboard refresh, and integration with live banking systems.

## References

* Kaggle. (n.d.). Anti Money Laundering Transaction Data (SAML-D). Kaggle. Retrieved June 3, 2026, from https://www.kaggle.com/datasets/berkanoztas/synthetic-transaction-monitoring-dataset-aml
* University of Petra GP_BI20252 Business Intelligence Graduation Project Template.
