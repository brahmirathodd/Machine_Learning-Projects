
# Bank Customer Attrition (Churn) Prediction

### Project Overview
This project aims to build predictive models to identify bank customers who are likely to churn. By leveraging historical data, the models can generalize to new customers, allowing the bank to proactively manage customer relationships and reduce churn rates, thereby improving customer satisfaction and profitability.

### Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model Building and Evaluation](#model-building-and-evaluation)
- [Hyperparameter Tuning](#hyperparameter-tuning)
- [Results](#results)
- [Conclusion](#conclusion)
- [License](#license)

### Dataset
The dataset used for this project is `BankChurners.csv`, which includes the following features:

- **Attrition_Flag**: Indicates if the customer has churned or not
- **Customer_Age**: Age of the customer
- **Gender**: Gender of the customer
- **Dependent_count**: Number of dependents
- **Education_Level**: Education level of the customer
- **Marital_Status**: Marital status of the customer
- **Income_Category**: Income category of the customer
- **Card_Category**: Type of card the customer holds
- **Months_on_book**: Number of months the customer has been with the bank
- **Total_Relationship_Count**: Total number of products the customer holds
- **Months_Inactive_12_mon**: Number of months the customer was inactive in the last 12 months
- **Contacts_Count_12_mon**: Number of contacts in the last 12 months
- **Credit_Limit**: Credit limit of the customer
- **Total_Revolving_Bal**: Total revolving balance of the customer
- **Avg_Open_To_Buy**: Average open to buy credit line
- **Total_Amt_Chng_Q4_Q1**: Total amount changed from Q4 to Q1
- **Total_Trans_Amt**: Total transaction amount
- **Total_Trans_Ct**: Total transaction count
- **Total_Ct_Chng_Q4_Q1**: Total count change from Q4 to Q1
- **Avg_Utilization_Ratio**: Average utilization ratio

### Exploratory Data Analysis
- Visualizations using Plotly and Seaborn are created to understand feature distributions and relationships.
- Insights into characteristics of attrited and existing customers are provided.

### Model Building and Evaluation
- Models are trained using techniques like Stratified K-Fold cross-validation.
- Evaluation metrics include accuracy, precision, recall, F1-score, and ROC AUC.

### Hyperparameter Tuning
- RandomizedSearchCV is used to optimize model performance.
