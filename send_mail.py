"""
Module: send_mail.py

Contains function to send email notifications.
"""

import smtplib
import ssl
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send(diagnosis_data, receiver_mail, prediction):
    """
    Send email notification with diagnosis report.

    Args:
        diagnosis_data (dict): Dictionary containing diagnosis data.
        receiver_mail (str): Email address of the receiver.
        prediction (int): Prediction result (0 for Not Detected, 1 for Detected).
    """
    email_sender = os.getenv('EMAIL_SENDER')
    email_password = os.getenv('EMAIL_PASSWORD')
    email_receiver = str(receiver_mail)

    # Determine diagnosis result
    result = 'Not Detected' if prediction == 0 else 'Detected'
    # Format diagnosis data as HTML table with increased size and font
    diagnosis_table = (
        '<table border="1" style="border-collapse: collapse; width: 100%; font-size: 20px;">'
    )

    for key, value in diagnosis_data.items():
        diagnosis_table += f'<tr><td style="padding: 10px; \
        ">{key}</td><td style="padding: 10px;">{value}</td></tr>'
    diagnosis_table += '</table>'

    # Set the subject and body of the email
    subject = 'Your Diagnosis Report'
    body = f"""
    <html>
    <body>
        <p style="font-size:24px;">Diagnosis Data :</p>
        {diagnosis_table}
        <p style="font-size:24px;">Diagnosis result : <strong>{result}</strong></p>
    </body>
    </html>
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    em.add_alternative(body, subtype='html')

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
