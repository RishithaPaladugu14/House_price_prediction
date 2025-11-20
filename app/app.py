from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# --------------------------------------------------------
#  LOAD MODEL USING ABSOLUTE PATH (WORKS ON RAILWAY)
# --------------------------------------------------------
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "model.pkl")
model_path = os.path.abspath(model_path)

model = pickle.load(open(model_path, "rb"))

# --------------------------------------------------------
#  HOME PAGE
# --------------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')


# --------------------------------------------------------
#  PREDICTION ROUTE
# --------------------------------------------------------
@app.route('/predict', methods=['POST'])
def predict():

    if request.method == "POST":

        size = float(request.form['size'])
        bhk = float(request.form['bhk'])
        under_construction = float(request.form['under_construction'])
        ready_to_move = float(request.form['ready_to_move'])
        resale = float(request.form['resale'])
        rera = float(request.form['rera'])

        # Input order must match training data
        features = [[size, bhk, under_construction, ready_to_move, resale, rera]]

        output = model.predict(features)[0]

        return render_template('index.html', prediction_text=f"Predicted House Price: ₹ {round(output, 2)}")

    return render_template('index.html')


# --------------------------------------------------------
#  NOTE:
#  DO NOT WRITE app.run() HERE.
#  GUNICORN (IN PROCFILE) WILL RUN THIS FILE.
# --------------------------------------------------------