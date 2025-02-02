# **Multilingual FAQ System with WYSIWYG Support**

Welcome to the **Multilingual FAQ System**! This project offers a robust FAQ platform that supports over 140 languages and integrates a WYSIWYG editor for seamless content management.

## **Key Features**

**Multilingual Support:** Translate FAQs into 140+ languages using `deep_translator`, offering superior performance compared to `googletrans`.

**Rich Text Editing:** Utilize `django-ckeditor` for managing and formatting FAQ content.

**API Integration:** Fully functional API to retrieve FAQs based on language preferences.

**Redis Caching:** Speed up responses with Redis caching.

**Admin Interface:** Manage FAQs effortlessly through the Django admin panel.

**Pagination:** Support for paginated FAQ listings.

## **Technologies Used**

- **Django 3.2+**: Backend framework
- **django-ckeditor**: For WYSIWYG editor integration
- **deep_translator**: For fast and accurate translations
- **Redis**: Caching for performance optimization
- **Django REST Framework**: To create API endpoints
- **Databases Supported**: SQLite, PostgreSQL, MySQL
- **Python 3.8+**

## **Installation Guide**

### **Prerequisites**

- Python 3.8+
- Django 3.2+
- Redis (for caching)

### **Setup Instructions**

**1. Clone the Repository:**

```bash
git clone https://github.com/Nihaar-E/Backend-FAQ.git
cd Backend-FAQ
```

**2. Install Dependencies:**

```bash
pip install -r requirements.txt
```

**3. Configure the Database:**

Adjust the database settings in `settings.py` if needed. By default, SQLite is configured.

**4. Run Migrations:**

```bash
python manage.py migrate
```

**5. Start Redis (if using Redis):**

```bash
redis-server
```

**6. Run the Development Server:**

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the application.

## **Docker Deployment (Optional)**

**1. Build and Run Containers:**

```bash
docker-compose up --build
```

**2. Access the Application:**

Navigate to [http://localhost:8000](http://localhost:8000).

## **Usage Guide**

### **Admin Panel Access**

Manage FAQs via the Django Admin panel:

- **URL:** [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- **Actions:** Add, edit, delete FAQs, and manage translations.

### **Adding New FAQs**

1. Log in to the Admin Panel.
2. Navigate to the FAQ model.
3. Add a new entry with the Question and Answer.
4. Optionally, add translations in other languages.

### **API Access**

- **API Home:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Fetch All FAQs:** [http://127.0.0.1:8000/api/faqs/](http://127.0.0.1:8000/api/faqs/)
- **Fetch FAQs in Hindi:** [http://127.0.0.1:8000/api/faqs/?lang=hi](http://127.0.0.1:8000/api/faqs/?lang=hi)

### **API Endpoints Overview**

| Method | Endpoint                      | Description               |
|--------|-------------------------------|---------------------------|
| GET    | `/api/faqs/`                  | Retrieve all FAQs         |
| GET    | `/api/faqs/?lang=hi`          | Retrieve FAQs in Hindi    |
| POST   | `/api/faqs/`                  | Create a new FAQ          |
| PUT    | `/api/faqs/{id}/`             | Update an existing FAQ    |
| DELETE | `/api/faqs/{id}/`             | Delete an FAQ             |

### **Example API Requests**

- **GET FAQs in English:** [http://127.0.0.1:8000/faqs/?lang=en](http://127.0.0.1:8000/faqs/?lang=en)
- **GET FAQs in Hindi:** [http://127.0.0.1:8000/faqs/?lang=hi](http://127.0.0.1:8000/faqs/?lang=hi)

### **Sample API Response**

```json
[
    {
      "question": "What is BharatFD",
      "answer": "BharatFD is a Financial Startup focused on providing trusted Fixed Deposits for individuals.",
      "id": 1
    }
]
```

## **Docker Deployment Steps**

**1. Build the Docker Image:**

```bash
docker build -t faq-web .
```

**2. Run Docker Compose:**

```bash
docker-compose up --build
```

**3. Access the Application:**

Visit [http://localhost:8000](http://localhost:8000).

## **Contributing**

We welcome contributions to enhance the system!

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push your branch and create a Pull Request.

## **Contact Information**

**Developed by:** Yuvraj Singh Rathore  
**Email:** yuvrajsinghrathore1034@gmail.com  

Feel free to reach out with any questions or suggestions!

