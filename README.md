 📊 Customer Churn Prediction using XGBoost


🚀 **Live Demo:** https://customerchurnprediction-a2o7rzxgsckgitgpbfmuab.streamlit.app/  
📸 Scroll down to see app screenshots

---
## 🚀 Project Overview

Customer churn is a critical challenge in the telecom industry, as retaining customers is significantly more cost-effective than acquiring new ones.

This project builds an end-to-end Machine Learning pipeline to predict whether a telecom customer is likely to churn using **XGBoost**, a powerful gradient boosting algorithm.

The solution includes:

- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Class Imbalance Handling (SMOTE)  
- Model Comparison  
- ROC-AUC Evaluation  
- Threshold Optimization  
- Interactive Streamlit Deployment  

---

## 🎯 Business Objective

The objective of this project is to identify high-risk customers before they churn so that businesses can:

- Offer personalized retention strategies  
- Reduce customer attrition  
- Increase long-term revenue  
- Improve customer lifetime value  

---

## 📂 Dataset Information

**Dataset:** Telco Customer Churn Dataset  

### Features Include:

- 👤 Demographics (Gender, Senior Citizen, Partner, Dependents)
- 📄 Contract Type & Tenure
- 🌐 Internet Services (DSL, Fiber Optic)
- 🔐 Online Security & Tech Support
- 💳 Payment Method
- 💰 Monthly Charges & Total Charges

### Target Variable:

- `Churn`
  - 0 → Customer Stays
  - 1 → Customer Churns

---

## ⚙️ Machine Learning Workflow

1. Data Cleaning  
2. Handling Missing Values  
3. One-Hot Encoding  
4. Train-Test Split  
5. SMOTE for Class Imbalance  
6. Feature Scaling  
7. Model Training  
8. ROC Curve Evaluation  
9. Feature Importance Analysis  
10. Streamlit Web Deployment  

---

## 🧠 Models Evaluated

| Model | Accuracy | ROC-AUC |
|--------|----------|----------|
| Logistic Regression | ~0.79 | ~0.84 |
| Random Forest | ~0.79 | ~0.85 |
| **XGBoost (Final Model)** | ~0.79 | ~0.83 |

### ✅ Final Model: XGBoost

XGBoost was selected because:

- Strong performance on structured/tabular datasets  
- Robust gradient boosting algorithm  
- Excellent generalization capability  
- Widely used in real-world production systems  

---

## 📈 Model Evaluation

Since churn prediction is an **imbalanced classification problem**,  
**ROC-AUC** was used as the primary evaluation metric instead of accuracy.

Final XGBoost ROC-AUC Score: **~0.83**

---

## 📊 Key Business Insights

- Month-to-month contracts show the highest churn rate  
- Customers with low tenure are more likely to churn  
- High monthly charges increase churn probability  
- Fiber optic users exhibit higher churn behavior  
- Automatic payment methods reduce churn risk  

---

## 🖥 Streamlit Web Application

An interactive Streamlit application allows users to:

- Input customer details  
- Adjust churn decision threshold  
- View churn probability  
- See risk classification (Low / Medium / High)  


## 📸 Application Screenshot

### Stay Prediction

<img width="1366" height="768" alt="Screenshot 2026-02-12 193742" src="https://github.com/user-attachments/assets/f898ca0c-d223-44a4-a290-b2c63e6480f8" />

<img width="1366" height="768" alt="Screenshot 2026-02-12 193838" src="https://github.com/user-attachments/assets/1cffff62-a17c-4e81-aa2f-a4c5fff5c94b" />

### Churn Prediction

<img width="1366" height="768" alt="Screenshot 2026-02-12 194105" src="https://github.com/user-attachments/assets/7bba2bc8-d833-428c-84de-e871c1ae8e98" />

<img width="1366" height="768" alt="Screenshot 2026-02-12 194130" src="https://github.com/user-attachments/assets/f1bb5dc1-29fe-4321-b4f9-558bb9884aab" />



> Interactive churn prediction dashboard built with Streamlit.
### Run Locally:

```bash
git clone https://github.com/ishivamm/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction
pip install -r requirements.txt
streamlit run app.py

