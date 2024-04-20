import smtplib

def send_email(name, email, data):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("akshaybhat1206@gmail.com", "vikingASTRO@17")
    # message to be sent
    message =  f'Hello Mr. {name}, your Diagnosis details are as below: {data}'
    # sending the mail
    s.sendmail("akshaybhat1206@gmail.com", email, message)
    # terminating the session
    s.quit()
    return 'Email sent successfully!'




