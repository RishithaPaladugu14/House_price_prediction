
# 🏡 House Price Prediction Web Application

A web-based Machine Learning application that predicts house prices (in Indian Rupees) from simple property features. Built with a trained regression model and deployed using Flask for an easy, real-time prediction experience.

---

## 📌 Brief description

This project provides a clean web interface where users enter property details (size, BHK, construction status, resale status, RERA approval) and receive an instant price estimate. It's aimed at students and developers learning ML deployment, and at real-estate users who want a quick data-driven price check.

---

## ✨ Features

* Predicts house price in ₹ (Lakhs) using a pre-trained ML model
* Simple, responsive form-based UI built with HTML + Bootstrap
* Flask backend that loads a serialized model (`model.pkl`) for inference
* Form validation and user-friendly output page
* Easy to extend (add location, advanced features, or new models)

---

## 🛠 Tech stack

* Python 3.x
* Flask
* scikit-learn, pandas, numpy
* HTML, CSS, Bootstrap

---

## 🚀 Quick start (run locally)

1. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

4. Open your browser at `http://127.0.0.1:5000` and use the form to predict.

---

## 📁 Project structure

```
House-Price-Prediction/
├── app.py                 # Flask application (routes + model loading)
├── model.pkl              # Serialized trained ML model (pickle)
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html         # Input form
│   └── result.html        # Prediction output page
├── static/
│   └── style.css          # Optional custom styles
├── data/
│   └── dataset.csv        # (optional) dataset used for training
└── README_House_Price_Prediction.md
```

---

## 🧠 Model training (optional / summary)

1. Load and clean your dataset (handle missing values, outliers)
2. Encode categorical features and scale/transform numeric features as needed
3. Train regressors (LinearRegression, RandomForestRegressor, XGBoost, etc.)
4. Evaluate using RMSE, MAE, and R²
5. Save the best model to `model.pkl`:

```python
import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(best_model, f)
```

---

## 📦 Usage

* Fill the form (size, BHK, and options)
* Click **Predict Price**
* View the predicted price on the result page (formatted as `₹ XXX.XX Lakhs`)

---

## 🔮 Future improvements

* Add **location** (city/area) support for regional price variance
* Use feature pipelines and `ColumnTransformer` for robust preprocessing
* Improve model accuracy with more data and advanced models (XGBoost, LightGBM)
* Deploy to cloud (Heroku, Render, AWS)
* Add unit tests and CI pipeline

---

## 📄 License

This project is open-source — feel free to copy, modify, and use it for learning or demos. Add a specific license file if you plan to share it publicly.

---

## ✍️ One-line summary

A simple Flask web app that loads a saved ML model to estimate house prices from basic property features — ideal for students, developers, and quick real-estate checks.
