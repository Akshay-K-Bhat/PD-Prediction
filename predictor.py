"""
This module provides functionality to load a trained model and make predictions using that model.

Functions:
- load_model(model_path): Load the trained model from the specified file path.
- predict(model, data): Use the trained model to make predictions on new data.

Dependencies:
- joblib: Used for loading the trained model from a file.

Example Usage:
---------------
model = load_model('path/to/model.pkl')
if model is not None:
    data = np.array([[feature1, feature2, ...]])
    predictions = predict(model, data)
    if predictions is not None:
        print("Predictions:", predictions)
"""

import joblib

def load_model(model_path):
    """
    Load the trained model from the specified file path.

    Parameters:
    - model_path (str): File path to the trained model.

    Returns:
    - model: Loaded model object.
    """
    try:
        model = joblib.load(model_path)
        return model
    except ValueError as e:
        print("Error loading the model:", e)
        return None

def predict(model, data):
    """
    Use the trained model to make predictions on new data.

    Parameters:
    - model: Trained model object.
    - data (numpy.array): New data for prediction.

    Returns:
    - predictions: Predicted values.
    """
    try:
        predictions = model.predict(data)
        return predictions
    except ValueError as e:
        print("Error making predictions:", e)
        return None
