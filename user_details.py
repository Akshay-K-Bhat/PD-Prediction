"""
Module: user_details.py

Contains functions related to saving user details.
"""

from datetime import date
import logging
import database

def save_user_details(request, session):
    """
    Save user details to the database.

    Args:
        request (Request): Flask request object containing form data.
        session (Session): Flask session object.

    Returns:
        tuple: A tuple containing status message and HTTP status code.
    """
    try:
        name = request.form['name']
        age = int(request.form['age'])
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        diagnosis_date = date.today().isoformat()

        logging.info("Received user details:  %s, %s, %s, %s, %s", name, age, phone, email, address)

        # Save user details to the database
        database.save_user_details(name, age, phone, email, address, diagnosis_date)

        # Store email in session
        session['email'] = email
        return "User details saved successfully", 200
    except ValueError as e:
        logging.error("Error saving user details: %s", e)
        return "Error saving user details", 500
