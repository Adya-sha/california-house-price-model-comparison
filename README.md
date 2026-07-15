# 🏠 California House Price Prediction - Model Comparison

## 📌 Project Overview

This project was completed as **Task 2** during my **AI & Machine Learning Internship at Main Crafts Technology**.

The objective of this project is to compare multiple machine learning regression models for predicting California house prices and identify the best-performing model based on evaluation metrics.

---

# 🎯 Objective

- Perform data preprocessing and feature scaling.
- Train multiple regression models.
- Compare their performance using standard evaluation metrics.
- Select the best-performing model.
- Save the trained model for future predictions.
- Build a Streamlit application for real-time house price prediction.

---

# 📂 Dataset

The project uses the **California Housing Dataset** provided by **Scikit-learn**.

### Features

- MedInc (Median Income)
- HouseAge
- AveRooms
- AveBedrms
- Population
- AveOccup
- Latitude
- Longitude

### Target Variable

- HousePrice (Median House Value)

---

# 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

# ⚙️ Project Workflow

1. Import Libraries
2. Load Dataset
3. Exploratory Data Analysis (EDA)
4. Data Visualization
5. Feature Scaling using StandardScaler
6. Train-Test Split
7. Train Multiple Regression Models
8. Model Evaluation
9. Model Comparison
10. Best Model Selection
11. Save Model and Scaler
12. Streamlit Deployment

---

# 🤖 Machine Learning Models Compared

- Linear Regression
- Ridge Regression
- Decision Tree Regressor

---

# 📊 Model Performance

| Model | MAE | RMSE | R² Score |
|------|------:|------:|------:|
| Linear Regression | **0.5332** | **0.7456** | **0.5758** |
| Ridge Regression | **0.5332** | **0.7456** | **0.5758** |
| Decision Tree Regressor | **0.4531** | **0.7022** | **0.6237** |

---

# 🏆 Best Model

After comparing all models, the **Decision Tree Regressor** achieved the best performance.

### Final Results

- **Model:** Decision Tree Regressor
- **MAE:** **0.4531**
- **RMSE:** **0.7022**
- **R² Score:** **0.6237**

The trained model was saved as:

- `best_house_price_model.pkl`

The fitted StandardScaler was also saved as:

- `scaler.pkl`

These files are used in the Streamlit application for making predictions on new data.

---

# 📈 Visualizations Included

The notebook contains:

- Correlation Heatmap
- Feature Distributions
- House Price Distribution
- Scatter Plot
- Boxplots
- Actual vs Predicted Plot
- Residual Plot
- Model Comparison Table

---

# 📱 Streamlit Application

The project includes a Streamlit web application that allows users to enter housing details and predict the median house price using the trained Decision Tree model.

To run the application:

```bash
streamlit run app.py
```

---

# 📁 Project Structure

```
AI_ML_Task2/
│
├── AI_ML_Task2_Model_Comparison.ipynb
├── app.py
├── best_house_price_model.pkl
├── scaler.pkl
├── README.md
├── requirements.txt
└── venv/
```

---

# 🚀 Future Improvements

- Hyperparameter tuning
- Random Forest Regression
- XGBoost Regression
- Cross Validation
- Feature Engineering
- Cloud Deployment using Streamlit Community Cloud

---

# 👩‍💻 Author

**Adyasha Sahu**

B.Tech Computer Science and Engineering Student

AI & Machine Learning Intern

Main Crafts Technology

---

## ⭐ Acknowledgement

This project was developed as part of the **AI & Machine Learning Internship at Main Crafts Technology** to demonstrate regression model comparison, evaluation, and deployment using Python and Streamlit.