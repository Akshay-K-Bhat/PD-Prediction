# Parkinson's Disease Prediction

## Overview

This project is a Flask web application designed to collect user data, perform predictions for Parkinson's Disease using an XGBoost machine learning model, and store the results in a MySQL database. It also includes functionality to send email notifications using Flask-Mail.

## Features

- User data collection through web forms
- Prediction of Parkinson's Disease using an XGBoost machine learning model
- Storing user details and prediction results in a MySQL database
- Email notifications using Flask-Mail

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- NumPy
- PyMySQL
- Flask-Mail
- XGBoost
- MySQL Server

### Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/projectname.git
   cd pd-detection
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the database:**

   - Ensure MySQL is installed and running on your machine.
   - Create a database named `prediction_data` and set up the required tables.

   Example SQL for table creation:

   ```sql
   CREATE DATABASE prediction_data;
   USE prediction_data;

   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100),
       age INT,
       phone VARCHAR(20),
       email VARCHAR(100),
       address TEXT,
       diagnosis_date DATE
   );

   CREATE TABLE predictions (
       id INT AUTO_INCREMENT PRIMARY KEY,
       input_data TEXT,
       prediction FLOAT,
       email VARCHAR(100)
   );
   ```

4. **Set environment variables (if needed):**

   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   export SECRET_KEY=your_secret_key
   export MAIL_SERVER=smtp.yourmailserver.com
   export MAIL_PORT=587
   export MAIL_USERNAME=your_email@example.com
   export MAIL_PASSWORD=your_email_password
   ```

### Running the Project

Start the Flask development server:

```bash
python flask_app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000/` to view the application.

## Usage

1. **Home Page:**

   - Access the home page at `http://127.0.0.1:5000/`.

2. **User Details Form:**

   - Navigate to `http://127.0.0.1:5000/customerDetails.html` to fill out and submit the user details form.

3. **Prediction Form:**

   - After submitting user details, proceed to `http://127.0.0.1:5000/form.html` to enter data for prediction.

4. **View Prediction Results:**
   - After submitting the prediction form, results will be displayed on a new page.

## Contributing

To contribute to this project, follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to the contributors of Flask and its extensions for providing such a robust framework.
- Special thanks to the authors of the XGBoost library used in this project.

---
