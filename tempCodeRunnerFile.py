from flask import Flask, render_template, request
import predictor
import numpy as np
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Here you would handle the prediction logic using the data sent from the form
    # For now, let's just print the data received
    data = {key: float(request.form[key]) for key in request.form}
    values = np.array([list(data.values())])
    print("Received data:", values)
    model_path = "./model.pkl"
    model = predictor.load_model(model_path)
    if model is None:
        print("Exiting...")
        exit()

    try:
        predictions = model.predict(values)
        print(predictions)
        return render_template('result.html', predictions=predictions[0])
    except Exception as e:
        print("Error making predictions:", e)
        return "Error making predictions"


    # You can then perform prediction using the received data and return the result
if __name__ == "__main__":
    app.run(debug=True)  # You can set debug=False for production

