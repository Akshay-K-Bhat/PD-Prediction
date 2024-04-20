import pymysql
from datetime import date

# Connect to MySQL
conn = pymysql.connect(host='localhost', user='root', password='VIKINGastro@17', db='prediction_data')
cursor = conn.cursor()

# Function to save user details to the database
def save_user_details(name, age, phone, email, address, diagnosis_date):
    try:
        cursor.execute("""
            INSERT INTO users (name, age, phone, email, address, diagnosis_date) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, age, phone, email, address, diagnosis_date))
        conn.commit()
        print("User details saved to database successfully!")
    except Exception as e:
        print("Error saving user details to database:", e)

def close_connection(exception=None):
    conn.close()
