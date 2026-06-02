# Data Visualization and Dashboard Insights

Exploratory data analysis is presented in the notebook `02_eda_exploration.ipynb`. Key visualisations include:

- **Transaction volume over time** – showing peaks and troughs in daily activity.
- **Distribution of transaction amounts** – highlighting the long‑tail nature of the data.
- **Correlation heatmap** – revealing relationships between features such as amount and risk level.
- **Network diagrams** – illustrating clusters of accounts involved in suspicious typologies.

From these plots we observed that suspicious transactions tend to occur in batches and often involve rapid transfers between many accounts. Normal transactions exhibit broader geographic distribution and higher variability in amounts. These insights informed the feature engineering and model choice.

The final Power BI dashboard (see `dashboards/Dashboard_Ann_Patel (1).pbix`) consolidates these insights into an interactive report. It allows analysts to filter by country, typology and time range, view flagged transactions and drill down into individual cases.
