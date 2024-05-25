"""
Flask application for Parkinson's Disease Prediction.
"""

import os
import logging
from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
from flask_session import Session
import prediction
import user_details

# Load environment variables from .env file
load_dotenv()

app = Flask("Parkinson's Disease Prediction")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Configure Flask-Session for filesystem-based storage
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False  # Session expires when the browser is closed
app.config['SESSION_USE_SIGNER'] = True  # Enable secure session cookie
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Session(app)

@app.route('/')
def index():
    """
    Render the index page.
    """
    return render_template('index.html')

@app.route('/form.html')
def form():
    """
    Render the form page.
    """
    return render_template('form.html')

@app.route('/customerDetails.html')
def customer_details_form():
    """
    Render the customer details form page.
    """
    return render_template('customerDetails.html')

@app.route('/saveUserDetails', methods=['POST'])
def save_user_details():
    """
    Save user details submitted through the form.
    """
    user_details.save_user_details(request, session)
    return redirect(url_for('form'))

@app.route('/predict', methods=['POST'])
def predict():
    """
    Perform prediction based on user input.
    """
    prediction_result = prediction.predict_and_send_email(request.form, session)
    return render_template('result.html', predictions=prediction_result)

if __name__ == "__main__":
    app.run(debug=True)
