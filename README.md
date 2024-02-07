# Introduction

**_MediPulse_** is a convenient and efficient online platform designed to streamline the process of booking doctor appointments. Our user-friendly interface allows you to easily schedule appointments with a variety of medical professionals, ensuring timely access to healthcare services tailored to your needs. Say goodbye to long waiting times and cumbersome booking processes – with [Website Name], your health is just a click away. Get started today and take control of your well-being!

# Features

- **User Registration and Authentication**: Users can create accounts and securely log in to access the appointment scheduling functionalities.
- **Appointment Booking**: Patients can browse available doctors, view their schedules, and book appointments based on their preferred date and time.
- **Doctor Dashboard**: Doctors have access to a dashboard where they can manage their availability, view upcoming appointments, and update their profiles.
- **Admin Panel**: Administrators can manage users, doctors, appointments, and other system settings.

# Getting Started

To get started you can simply clone this project repository and install the dependencies.

Clone the MediPulse repository using git:

```
git clone https://github.com/AmanRahees/MediPulse-Backend.git

cd backend
```

Create a virtual environment to install dependencies in and activate it:

```
python3 -m venv env

env\Scripts\activate
```

Then install the dependencies:

```
(env) pip install -r requirement.txt
```

Once `pip` has finished downloading the dependencies:

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

And navigate to <a href="http://127.0.0.1:8000">`http://127.0.0.1:8000`</a>

**_Attention_** : Note: In order to run the project correctly, you will need to create a .env file in the root directory of the project. This file is crucial for storing sensitive information such as database credentials, API keys, and other configuration variables. For security reasons, we cannot provide the actual content of the .env file. However, we will provide you with the template/structure of the .env file that you need to populate with the correct details to run the application smoothly.

Here is the template/structure of the .env file:

```python
# Django Secret Key
SECRET_KEY=your_secret_key_here

# Database Configuration
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port

# Email Configuration (Optional)
EMAIL_HOST=your_email_host
EMAIL_PORT=your_email_port
EMAIL_HOST_USER=your_email_username
EMAIL_HOST_PASSWORD=your_email_password
EMAIL_USE_TLS=your_email_tls_status

# Debug Mode (Set to True for development, False for production)
DEBUG=True

```
