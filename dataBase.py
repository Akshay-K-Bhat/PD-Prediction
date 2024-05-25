"""
database.py: Module for interacting with the MySQL database.

This module provides functions to establish a connection to a MySQL database,
save user details and prediction results, and create necessary tables if they
do not exist.

Functions:
    - get_db_connection: Establishes a connection to the MySQL database.
    - save_user_details: Saves user details to the 'users' table in the database.
    - save_prediction_to_database: Saves prediction results to the 'predictions' table.
    - create_tables_if_not_exist: Creates 'users' and 'predictions' tables if they don't exist.
"""

import os
import logging
import pymysql
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format='%(asctime)s %(levelname)s: %(message)s',  # Define the format of log messages
    datefmt='%Y-%m-%d %H:%M:%S'  # Define the format of the timestamp
)

def get_db_connection():
    """
    Establishes a connection to the MySQL database.

    Returns:
        pymysql.connections.Connection: A connection object
        representing the connection to the database.
    """
    return pymysql.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        db=os.getenv('MYSQL_DB')
    )

def save_user_details(name, age, phone, email, address, diagnosis_date):
    """
    Saves user details to the 'users' table in the database.

    Args:
        name (str): The name of the user.
        age (int): The age of the user.
        phone (str): The phone number of the user.
        email (str): The email address of the user.
        address (str): The address of the user.
        diagnosis_date (str): The diagnosis date of the user.

    Raises:
        pymysql.Error: If an error occurs while interacting with the database.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        create_tables_if_not_exist()
        cursor.execute("""
            INSERT INTO users (name, age, phone, email, address, diagnosis_date) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, age, phone, email, address, diagnosis_date))
        conn.commit()
        cursor.close()
        conn.close()
        logging.info("User details saved to database successfully!")
    except pymysql.Error as e:
        logging.error("Database error: %s", e)
        raise

def save_prediction_to_database(input_data, prediction, email):
    """
    Saves prediction details to the 'predictions' table in the database.

    Args:
        input_data (str): The input data for the prediction.
        prediction (float): The predicted value.
        email (str): The email address associated with the prediction.

    Raises:
        pymysql.Error: If an error occurs while interacting with the database.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        create_tables_if_not_exist()
        cursor.execute("""
            INSERT INTO predictions (input_data, prediction, email) 
            VALUES (%s, %s, %s)
        """, (str(input_data), prediction, email))
        conn.commit()
        cursor.close()
        conn.close()
        logging.info("Prediction saved to database successfully!")
    except pymysql.Error as e:
        logging.error("Error saving prediction to database: %s", e)
        raise

def create_tables_if_not_exist():
    """
    Creates tables 'users' and 'predictions' in the database if they don't exist already.

    Raises:
        pymysql.Error: If an error occurs while interacting with the database.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        create_users_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            phone VARCHAR(20),
            email VARCHAR(100),
            address TEXT,
            diagnosis_date DATE,
            INDEX email_index (email) 
        )
        """
        create_predictions_table_query = """
        CREATE TABLE IF NOT EXISTS predictions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            input_data TEXT,
            prediction FLOAT,
            email VARCHAR(100),
            FOREIGN KEY (email) REFERENCES users(email)
        )
        """
        cursor.execute(create_users_table_query)
        cursor.execute(create_predictions_table_query)
        conn.commit()
        cursor.close()
        conn.close()
    except pymysql.Error as e:
        logging.error("Error creating tables: %s", e)
        raise

# Ensure tables are created when the module is loaded
create_tables_if_not_exist()
