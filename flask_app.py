from flask import Flask, render_template, request, redirect,url_for
import predictor
import numpy as np
import pymysql
import saveUser
from flask_mail import Mail, Message
from datetime import date

app = Flask(__name__)

# Connect to MySQL
conn = pymysql.connect(host='localhost', user='root', password='VIKINGastro@17', db='prediction_data')
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form.html')
def form():
    return render_template('form.html')

@app.route('/customerDetails.html')
def customerDetailsForm():
    return render_template('customerDetails.html')


@app.route('/saveUserDetails', methods=['POST'])
def saveUserDetails():
        name = request.form['name']
        age = int(request.form['age'])  
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        diagnosis_date = date.today().isoformat()
        print(f"Name: {name}, Age: {age}, Phone: {phone}, Email: {email}, Address: {address}")
        print("Data received successfully!")
        saveUser.save_user_details(name, age, phone, email, address, diagnosis_date)
        return redirect(url_for('form'))

@app.route('/predict', methods=['POST'])
def predict():
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

        # Save input data and prediction result to MySQL
        save_to_database(data, predictions[0])

        return render_template('result.html', predictions=predictions[0])
    except Exception as e:
        print("Error making predictions:", e)
        return "Error making predictions"

def save_to_database(input_data, prediction):
    try:
        # Create a new record with input data, prediction, and user ID
        sql = "INSERT INTO predictions (user_id, input_data, prediction) VALUES (%s, %s, %s)"
        val = (user_id, str(input_data), prediction)
        cursor.execute(sql, val)
        conn.commit()
        print("Data saved to database successfully!")
    except Exception as e:
        print("Error saving data to database:", e)



if __name__ == "__main__":
    app.run(debug=True)

conn.close()
