
# 🩺 Medical Result Prediction Web App

## 📌 Overview

This project is a **Flask-based web application** that predicts medical results based on patient data.
It uses a pre-trained **Machine Learning model** to classify the outcome based on various health parameters entered by the user.

The application features:

* A user-friendly **form** to collect patient health details
* **Machine Learning model** integration for predictions
* A **report page** showing the user’s inputs and prediction results
* Modular structure for scalability

---

## 🚀 Features

✅ Web-based interface built with **HTML + CSS + Flask**
✅ Input form for patient health data
✅ Pre-trained **ML model** for predictions
✅ **Result report** with all user inputs + prediction outcome
✅ Easy to deploy locally or on cloud platforms like **Heroku, Render, or PythonAnywhere**

---

## 🏗 Project Structure

```
medical-prediction-app/
│
├── app.py                # Main Flask application
├── model.pkl             # Pre-trained ML model
├── templates/
│   ├── index.html        # Input form page
│   ├── result.html       # Displays only the prediction
│   ├── report.html       # Displays detailed input + prediction report
│
├── static/
│   └── style.css         # Optional CSS styles
│
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/medical-prediction-app.git
cd medical-prediction-app
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask App

```bash
python app.py
```

### 4️⃣ Open in Browser



---

## 📊 How It Works

1. **User fills out the form** with health parameters (age, blood pressure, symptoms, etc.)
2. The app converts the input into a **DataFrame**
3. The **ML model** (`model.pkl`) predicts the result
4. The prediction and input data are displayed on the **report page**

---

## 🧠 Machine Learning Model

* Model: RandomForestClassifier (or any trained classifier)
* Training Data: Historical medical records dataset
* Features:

  * Gender
  * Age
  * Patient Type
  * Severity
  * Breath Shortness
  * Visual Changes
  * Nose Bleeding
  * Systolic BP
  * Diastolic BP
  * Controlled Diet

---

## 🖥 Example Screenshots

*(Add screenshots here of `index.html` and `report.html`)*

---



---

