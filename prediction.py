"""
This module contains functions for performing predictions based
on input data and sending email notifications asynchronously.
"""
import threading
import logging
import numpy as np
import database
import predictor
import send_mail

def predict_and_send_email(data, session):
    """
    Perform prediction based on the input data and send email asynchronously.

    Args:
        data (dict): Input data for prediction.
        session (dict): Session data containing user email.

    Returns:
        tuple: A tuple containing the prediction result and HTTP status code.
    """
    try:
        data = {key: float(data[key]) for key in data}
        values = np.array([list(data.values())])

        logging.info("Received prediction data: %s", values)

        model = predictor.load_model("./model.pkl")
        if model is None:
            logging.error("Model not found")
            return "Model not found", 500

        predictions = model.predict(values)

        # Retrieve email from session
        email = session.get('email')
        if email is None:
            logging.error("No email found in session")
            return "No email found in session", 500

        # Save input data and prediction result to MySQL
        database.save_prediction_to_database(data, predictions[0],email)

        # Send email asynchronously
        send_email_async(data, email, predictions[0])

        return predictions[0]
    except ValueError as e:
        logging.error("Error making predictions: %s", e)
        return "Error making predictions", 500

def send_email_async(data, email, prediction):
    """
    Send email asynchronously.

    Args:
        data (dict): Input data for prediction.
        email (str): User email address.
        prediction (float): Prediction result.
    """
    threading.Thread(target=send_mail.send, args=(data, email, prediction)).start()
