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
    except Exception as e:
        print("Error loading the model:", e)
        return None

def predict(model, data):
    """
    Use the trained model to make predictions on new data.

    Parameters:
    - model: Trained model object.
    - data (numpy.ndarray): New data for prediction.

    Returns:
    - predictions: Predicted values.
    """
    try:
        predictions = model.predict(data)
        return predictions
    except Exception as e:
        print("Error making predictions:", e)
        return None

