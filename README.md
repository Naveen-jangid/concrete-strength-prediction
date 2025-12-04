# Concrete Strength Prediction

## Table of Contents
- [Demo](#demo)
- [Overview](#overview)
- [Project Goal](#project-goal)
- [Technical Aspects](#technical-aspects)
- [Installation](#installation)
- [Used Technologies](#used-technologies)
- [Appendix](#appendix)
- [License](#license)
- [Feedback](#feedback)

---

##  Demo  
🔗 **Web Application:** [Concrete Strength Prediction](https://concrete-strength-prediction-7jg6.onrender.com)

### **Overview of Web Application**  
- The web app allows users to **input concrete mix values** and **predict the compressive strength** instantly.  
- It eliminates the need for **28-day testing** with a traditional method.  

---

##  Overview  
Concrete is a vital material in **construction**, and its **compressive strength** is a crucial quality indicator.  
- Traditional testing takes **28 days**, which delays project timelines.  
- This **AI-powered solution** predicts **concrete strength instantly** using **Machine Learning (ML)** models.  

**Dataset:** The model is trained on **Concrete_Data.csv**, containing **1030 records and 8 input features**.  
**Algorithms Used:** XGBoost, Random Forest, Decision Tree, etc.  
**Deployment:** Hosted on **Render** with a Flask API for predictions.  

---

## Project Goal  
This project was developed as part of an **end-to-end AI/ML pipeline**, involving:  
 **Data Preprocessing & Cleaning**  
 **Feature Engineering & Model Training**  
 **Hyperparameter Tuning**  
 **Deployment on Render with Flask API**  

---

## Technical Aspects  
This project is divided into three main stages:

### **1️ Data Preparation**  
 **Data Cleaning:** Handling missing values, outliers  
 **Feature Engineering:** Selecting important predictors  
 **Data Normalization:** Standardizing features  

### **2️ Model Development**  
 **Algorithms:** XGBoost, Random Forest, Decision Tree  
 **Hyperparameter Tuning:** Using GridSearchCV  
 **Model Performance:** Evaluated using RMSE, R²  

### **3️ Model Deployment**  
 **Flask API:** For real-time predictions  
 **Render Hosting:** Deployed as a cloud-based API  
 **Logging:** Tracks requests and predictions  

---

## Installation  
The project requires **Python 3.8+** and Flask.  

### **1️ Clone the Repository**
```bash
git clone https://github.com/your-username/concrete-strength-prediction.git
cd concrete-strength-prediction
```

### **2️ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️ Run the Flask API**
```bash
python app.py
```
Open **http://127.0.0.1:5000/** in your browser.
- for the data:-
    "Cement": 300,
    "Blast_Furnace_Slag": 100,
    "Fly_Ash": 0,
    "Water": 180,
    "Superplasticizer": 5,
    "Coarse_Aggregate": 1000,
    "Fine_Aggregate": 800,
    "Age": 28

![image](https://github.com/user-attachments/assets/a274745f-925c-4173-a532-b427b767a035)

### **Quick command-line prediction (no server required)**
Use the trained model locally without the web UI:

```bash
python predict_cli.py --use-sample
```

Pass custom values by supplying every feature:

```bash
python predict_cli.py \
  --cement 300 --slag 100 --fly-ash 0 --water 180 --superplasticizer 5 \
  --coarse-agg 1000 --fine-agg 800 --age 28
```

### **Validate against the sample dataset**
Compare the trained model to an actual row in `Concrete_Data.csv`:

```bash
python sample_data_prediction.py --row 0
```

Use a different example by changing the `--row` index.


---

##  Used Technologies  
 **Python** (Flask, Pandas, NumPy, Scikit-Learn, XGBoost)  
 **Render** (Cloud Deployment)  
 **GitHub** (Version Control)    
 **Logging** (Python Logging Module)  

 ![image](https://github.com/user-attachments/assets/77e4ba35-6e39-4ba9-a778-b1799f94697d)


---

##  Appendix  
1. High Label Documentation: https://docs.google.com/document/d/1UqDNwOSkValLzX5BlPRRfMAGUp12j2E_/edit?usp=drive_link&ouid=110161944854525864991&rtpof=true&sd=true
2. Low Label Documentation: https://docs.google.com/document/d/1Wo_kEpj2_wiSfdEDsNnkMhb13oM_GAuF/edit?usp=drive_link&ouid=110161944854525864991&rtpof=true&sd=true
3. Architecture: https://docs.google.com/document/d/1S7pY48vw1tJ0OoExw8fUzNEddKauknUN/edit?usp=drive_link&ouid=110161944854525864991&rtpof=true&sd=true
4. Wireframe: https://docs.google.com/document/d/1t5yx_hABbTVB0jIipQdMM-IGvxHr_klI/edit?usp=drive_link&ouid=110161944854525864991&rtpof=true&sd=true


---

## License  
This project is **open-source** under the **MIT License**.

---

## Feedback  
If you have **any suggestions or issues**, please **contact me** at: `nvnjan95@gmail.com` 
```
