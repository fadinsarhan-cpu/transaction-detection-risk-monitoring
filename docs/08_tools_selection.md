# Tools Research and Selection Effort

## Purpose of Tool Selection

To build the **Transaction Detection & Risk Monitoring** solution, we selected tools that support the entire business‑intelligence lifecycle: data acquisition, cleaning, analysis, statistical testing, machine learning, dashboarding, version control and final project submission.  The chosen stack balances analytical capability with business usability and aligns with the team’s expertise.

## Selected Tools

| Tool                 | Why selected                                                        | Role in project                                                         | Alternative                 |
| -------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------- |
| **Python**               | Strong for data analytics and machine learning                      | ETL, EDA, statistical analysis, and modelling                            | R                           |
| **Pandas**               | Easy and powerful tabular data processing                           | Cleaning, transformation, grouping, and aggregation                     | Polars                      |
| **NumPy**                | Efficient numerical operations                                      | Numeric calculations and array operations                               | Built into pandas workflows |
| **Matplotlib / Seaborn** | Standard visualisation libraries                                    | EDA charts and statistical visualisations                               | Plotly                      |
| **Plotly**               | Supports interactive and dashboard‑style visualisations             | Optional interactive exploration and visual reporting                   | Power BI visuals            |
| **Scikit‑learn**         | Reliable machine‑learning models and evaluation metrics             | Logistic Regression, Random Forest, preprocessing, and model evaluation | PyCaret                     |
| **XGBoost**              | Strong performance on structured/tabular data                       | Advanced classification model for suspicious transaction detection      | LightGBM                    |
| **Imbalanced‑learn**     | Designed for imbalanced classification problems                     | SMOTE/resampling for rare suspicious transaction cases                  | Class weights               |
| **Jupyter Notebook**     | Supports step‑by‑step analysis with code, outputs, and explanations | Documentation, experiments, EDA, and modelling workflow                  | VS Code notebooks           |
| **Power BI**             | Strong business dashboarding and KPI reporting tool                 | Final BI dashboard for risk monitoring and decision support             | Tableau                     |
| **GitHub**               | Version control and professional project submission                 | Repository organisation, documentation, and submission tracking         | GitLab                      |

## Tool Justification

Python and pandas were chosen as the primary data‑manipulation stack because they provide mature libraries for reading, cleaning, transforming and aggregating tabular data.  NumPy underpins efficient numerical computations, and Jupyter Notebook offers an interactive environment that blends code, narrative and visual outputs – ideal for EDA and model development.

For machine learning, scikit‑learn offers a robust suite of algorithms, preprocessing tools and evaluation metrics that are well suited to binary classification.  XGBoost was considered for its strong performance on structured data; however it is optional depending on environment constraints.  The **imbalanced‑learn** library provides specialised techniques (e.g. SMOTE) to address the extreme rarity of suspicious transactions.

Power BI was selected for the final dashboard because it enables business users to interactively explore KPIs, trends and flagged cases through slicers and drill‑throughs.  While Python plotting libraries create static charts, Power BI delivers a polished business interface for stakeholders.

GitHub manages version control and ensures the project is organised, reproducible and easy to submit for assessment.

## Alternative Tools Considered

Other tools were evaluated during the research phase.  **R** is a strong alternative for statistical analysis; **Tableau** offers interactive dashboards; **LightGBM** provides gradient‑boosted trees similar to XGBoost; **PyCaret** automates model selection; and **GitLab** is an alternative code‑hosting platform.  Ultimately, the selected toolset provided sufficient capabilities and matched the team’s expertise.

## Conclusion

The selected tools support the full BI lifecycle: **data acquisition → cleaning → analysis → modelling → dashboarding → decision support**.  They offer a balance of analytical power and business usability, ensuring the project can be reproduced, extended and presented effectively.
