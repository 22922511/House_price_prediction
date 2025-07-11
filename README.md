# 🏡 House Price Prediction using Machine Learning

A full-stack machine learning project that predicts house prices in Bangalore based on user inputs like location, BHK, bathrooms, and total square feet.


## 📌 Project Overview

This project demonstrates a complete end-to-end ML pipeline:

- **Data Preprocessing & Modeling:** Trained a Linear Regression model using cleaned housing data.
- **Backend API:** Built with FastAPI to serve predictions.
- **Frontend UI:** Streamlit app for an interactive user experience.
- **Deployment Ready:** Backend and frontend can be deployed independently (e.g., Heroku, EC2, or Streamlit Cloud).


## 🧠 Model Details

- **Algorithm:** Linear Regression
- **Dataset Size:** ~13,000 entries
- **Accuracy (R² score):** 73%
- **Key Features:**
  - `location` (Categorical)
  - `total_sqft` (Numerical)
  - `bath` (Numerical)
  - `BHK` (Numerical)


## 📁 Project Structure

House_price_prediction/
├── App/ # FastAPI backend
│ └── main.py
├── Model/
│ └── House_price_prediction_model.pkl
├── columns_name/
│ └── columns_name.json
├── frontend/
│ └── app.py # Streamlit UI
├── requirements.txt
├── README.md
└── .gitignore

