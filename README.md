🌍📁 ##Multilingual FAQ System with WYSIWYG Support

Welcome to the Multilingual FAQ System! This project offers a robust FAQ platform that supports over 140 languages and integrates a WYSIWYG editor for seamless content management. 🚀

🌟 Key Features

Multilingual Support: Translate FAQs into 140+ languages using deep_translator, offering superior performance compared to googletrans.

Rich Text Editing: Utilize django-ckeditor for managing and formatting FAQ content.

API Integration: Fully functional API to retrieve FAQs based on language preferences.

Redis Caching: Speed up responses with Redis caching.

Admin Interface: Manage FAQs effortlessly through the Django admin panel.

Pagination: Support for paginated FAQ listings.

🛠️ Technologies

Django 3.2+: Backend framework

django-ckeditor: For WYSIWYG editor integration

deep_translator: For fast and accurate translations

Redis: Caching for performance optimization

Django REST Framework: To create API endpoints

Databases Supported: SQLite, PostgreSQL, MySQL

Python 3.8+

⚡ Installation Guide

📦 Prerequisites

Python 3.8+

Django 3.2+

Redis (for caching)

🏗️ Setup Instructions

Clone the Repository:

git clone https://github.com/Nihaar-E/Backend-FAQ.git
cd Backend-FAQ

Install Dependencies:

pip install -r requirements.txt

Configure the Database:
Adjust the database settings in settings.py if needed. By default, SQLite is configured.

Run Migrations:

python manage.py migrate

Start Redis (if using Redis):

redis-server

Run the Development Server:

python manage.py runserver

Visit http://127.0.0.1:8000/ to view the application.

🐫 Docker Deployment (Optional)

Build and Run Containers:

docker-compose up --build

Access the Application:
Navigate to http://localhost:8000.

📖 Usage Guide

🏛 Admin Panel Access

Manage FAQs via the Django Admin panel:

URL: http://127.0.0.1:8000/admin

Actions: Add, edit, delete FAQs, and manage translations.

Adding New FAQs

Log in to the Admin Panel.

Navigate to the FAQ model.

Add a new entry with the Question and Answer.

Optionally, add translations in other languages.

🔹 API Access

API Home: http://127.0.0.1:8000/

Fetch All FAQs: http://127.0.0.1:8000/api/faqs/

Fetch FAQs in Hindi: http://127.0.0.1:8000/api/faqs/?lang=hi

🔗 API Endpoints Overview

Method

Endpoint

Description

GET

/api/faqs/

Retrieve all FAQs

GET

/api/faqs/?lang=hi

Retrieve FAQs in Hindi

POST

/api/faqs/

Create a new FAQ

PUT

/api/faqs/{id}/

Update an existing FAQ

DELETE

/api/faqs/{id}/

Delete an FAQ

Example API Request

GET FAQs in English:http://127.0.0.1:8000/faqs/?lang=en

GET FAQs in Hindi:http://127.0.0.1:8000/faqs/?lang=hi

Sample API Response

[
    {
      "question": "What is BharatFD",
      "answer": "BharatFD is a Financial Startup focused on providing trusted Fixed Deposits for individuals.",
      "id": 1
    }
]

🛥️ Docker Deployment Steps

Build the Docker Image:

docker build -t faq-web .

Run Docker Compose:

docker-compose up --build

Access the app at http://localhost:8000.

🖋️ Contributing

We welcome contributions to enhance the system!

Fork the repository

Create a new branch for your feature

Commit your changes

Push your branch and create a Pull Request

🔗 Contact Information

Developed by: Yuvraj Singh RathoreEmail: yuvrajsinghrathore1034@gmail.com

Feel free to reach out with any questions or suggestions! 😊
