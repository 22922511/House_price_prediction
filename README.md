# 🏡 House Price Prediction using Machine Learning

A full-stack machine learning project that predicts house prices in Bangalore based on user inputs like location, BHK, bathrooms, and total square feet.


## 📌 Project Overview

This project demonstrates a complete end-to-end ML pipeline:

- **Data Preprocessing & Modeling:** Trained a Linear Regression model using cleaned housing data.
- **Backend API:** Built with FastAPI to serve predictions.
- **Frontend UI:** Streamlit app for an interactive user experience.
- **Deployment Ready:** Backend and frontend can be deployed independently (e.g., Heroku, EC2, or Streamlit Cloud).
  
## 🚀 Features

✅ End-to-End ML Pipeline  
✅ FastAPI for RESTful Prediction API  
✅ Streamlit-based Interactive UI  
✅ Model trained on 13,000+ housing records  
✅ Structured for local & cloud deployment (Render/Streamlit Cloud/EC2)

## 🧠 Model Details

- **Algorithm:** Linear Regression
- **Dataset Size:** ~13,000 entries
- **Accuracy (R² score):**
  
     version_1  75%
  
     version_2  80%
  
- **Key Features:**
  - `location` (Categorical)
  - `total_sqft` (Numerical)
  - `bath` (Numerical)
  - `BHK` (Numerical)


## 📁 Project Structure

<img width="300" height="596" alt="image" src="https://github.com/user-attachments/assets/c77194d5-529f-4c7d-aa92-b03d4bca244f" />


---

## ⚙️ Installation & Setup

### 📦 Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/House_price_prediction.git```
cd House_price_prediction
```

---
### 🐍 Step 2: Create & Activate Virtual Environment
```python -m venv myvenv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # macOS/Linux
```
---
### 📚 Step 3: Install Dependencies
```
pip install -r requirements.txt
```
---
### 🔁 How to Run
## 🧠 Start FastAPI Backend
```
cd App
uvicorn main:app --reload
```
→ Accessible at: http://127.0.0.1:8000  

→ Swagger docs at: http://127.0.0.1:8000/docs  


🌐 Start Streamlit Frontend
```
cd frontend
streamlit run app.py
```
Your Streamlit app will be available at:  

http://localhost:8501
---
🔗 API Endpoint
POST /predict
Request:  

    {  

      "total_sqft": 1600,  
  
      "bath": 2,  
  
      "BHK": 3,  
  
      "location": "whitefield",  
  
    }  


---
Response:  

    {  

      "predicted_category": 74.51  
  
    }  

---
### 🛠 Tech Stack
Python 3.10.6  


FastAPI + Uvicorn  


Streamlit

Scikit-learn

Pandas & NumPy

Pydantic (v2)  
### Visual  


<img width="998" height="1065" alt="image" src="https://github.com/user-attachments/assets/41471ce8-fc10-4044-b5e2-023ba15b4b98" />


