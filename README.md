# 🛒 Supermarket Sales Prediction

A machine learning web application that predicts total sales per transaction in a supermarket using Random Forest regression.

![Python](https://img.shields.io/badge/Python-3.10-blue) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange) ![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red) ![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow) ![Status](https://img.shields.io/badge/Status-Live-brightgreen)

---

## 🎯 Project Objective

Build a machine learning model that accurately predicts supermarket transaction sales to support inventory management, staff scheduling, business decision-making, and revenue forecasting.

---

## 📸 Screenshots

## 📸 Screenshots

### 🖥️ Live Streamlit App
![App Screenshot](https://raw.githubusercontent.com/asiya-sabiu25/supermarket-sales-prediction/main/images/app_screenshot.png)

### 📊 Feature Importance
![Feature Importance](https://raw.githubusercontent.com/asiya-sabiu25/supermarket-sales-prediction/main/images/feature_importance.png)

### 🎯 Actual vs Predicted Sales
![Actual vs Predicted](https://raw.githubusercontent.com/asiya-sabiu25/supermarket-sales-prediction/main/images/actual_vs_predicted.png)

### 📈 Sales by Branch
![Sales by Branch](https://raw.githubusercontent.com/asiya-sabiu25/supermarket-sales-prediction/main/images/sales_by_branch.png)

### 🔥 Correlation Heatmap
![Correlation Heatmap](https://raw.githubusercontent.com/asiya-sabiu25/supermarket-sales-prediction/main/images/correlation_heatmap.png)
---

## 📊 Dataset

- **Source:** [Kaggle — Supermarket Sales Dataset](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)
- **Size:** 1,000 transactions × 17 features
- **Features:** Branch, City, Customer type, Gender, Product line, Unit price, Quantity, Rating, Date, Time, Payment method

---

## 🔬 Key Steps

### 1. Exploratory Data Analysis
- Sales distribution across branches, product lines, and customer segments
- Time-based patterns (hourly, daily, monthly trends)
- Correlation analysis between numerical features

### 2. Feature Engineering
- **Fixed data leakage** — removed mathematically derived columns (`Tax 5%`, `cogs`, `gross margin %`, `gross income`) that inflated model performance artificially
- **Extracted date/time features** — `hour`, `day_of_week`, `month`, `is_weekend`
- One-hot encoded all categorical variables

### 3. Model Training & Comparison

| Model | Notes |
|---|---|
| Linear Regression | Baseline |
| Decision Tree | Prone to overfitting |
| Random Forest | Best balanced performance ✅ |
| Gradient Boosting | Competitive alternative |

### 4. Hyperparameter Tuning
Used `RandomizedSearchCV` with 5-fold cross-validation to optimize `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`, and `max_features`.

### 5. Model Explainability
- Feature importance visualization
- SHAP values for prediction transparency

---

## 💡 Business Insights

1. **Quantity purchased** is the strongest driver of total sales
2. **Unit price** significantly impacts transaction value
3. **Peak shopping hours** show higher average sales — staffing should reflect this
4. **Branch performance varies** — inventory should be distributed accordingly
5. **Product line differences** suggest targeted marketing opportunities
6. **Weekend vs weekday** patterns enable smarter promotional planning

---

## 🚀 Live Demo

Deployed as an interactive Streamlit web app — input transaction details and get an instant sales prediction.

**To run locally:**
```bash
git clone https://github.com/YOUR_USERNAME/supermarket-sales-prediction
cd supermarket-sales-prediction
pip install -r requirements.txt
streamlit run app.py
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas & NumPy | Data manipulation |
| Scikit-learn | ML modelling |
| Matplotlib & Seaborn | Visualization |
| SHAP | Model explainability |
| Streamlit | Web app deployment |
| Power BI | Interactive business dashboard |
| Google Colab | Development environment |

---

## 📁 Repository Structure

```
supermarket-sales-prediction/
│
├── Supermarket_Sales_Upgraded.ipynb   # Main ML notebook
├── app.py                              # Streamlit web app
├── supermarket_model.pkl              # Saved trained model
├── feature_columns.pkl                # Saved feature list
├── Supermarket_Dashboard.pbix         # Power BI dashboard (coming soon)
├── requirements.txt                   # Dependencies
└── README.md                          # This file
```

---

## 💾 Saving Charts From Colab

To save all charts as image files directly from Google Colab, add `plt.savefig()` after each plot:

```python
# After each chart, save it before plt.show()
plt.savefig('images/feature_importance.png', dpi=150, bbox_inches='tight')
plt.show()

# Then download all at once
from google.colab import files
files.download('images/feature_importance.png')
files.download('images/actual_vs_predicted.png')
files.download('images/sales_by_branch.png')
files.download('images/correlation_heatmap.png')
```

---

## 📦 Requirements

```
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
shap
joblib
pyngrok
openpyxl
```

---

## 👤 Author

**[Aiya Sabiu Sulaiman]**
Human Physiology Graduate | Data Science & ML (3MTT Certified) | Microsoft Power BI (In Progress)
📧 your.email@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/asiya-sabiu25/)
🐙 [GitHub](https://github.com/asiyasabiu25)

## 🎓 Certifications & Training

| Certification | Issuer | Status |
|---|---|---|
| B.Sc. Human Physiology | [Bayero University] | ✅ Completed |
| Data Science & ML Certificate | 3MTT — Federal Government of Nigeria | ✅ Completed |
| Microsoft Power BI Data Analyst (PL-300) | Microsoft | 🔄 In Progress |
| Google Data Analytics Certificate | Google / Coursera | 📅 Planned |
| Azure AI Fundamentals (AI-900) | Microsoft | 📅 Planned |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
