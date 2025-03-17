# Edu Management System
A comprehensive web application built with Django for managing students, teachers and subjects.

## Features
### Teacher Management
- Add, view, edit, and delete teacher records.
- Display teacher names in the system.

### Student Management
- Add, view, edit, and delete student records.
- Detailed student profiles with basic information.

### Subject Management
- Create and manage subjects with names.
- View subject details.


### Modern UI
- Clean, responsive interface built with custom CSS and Django Templates.

### Data Validation
- Form validation to ensure data integrity and prevent errors.

## Technology Stack
- **Backend:** Django 5.1
- **Database:** SQLite (default, configurable for PostgreSQL/MySQL)
- **Frontend:** HTML, CSS, Django Templates
- **Deployment:** Compatible with Django-supported hosting platforms

## Installation
Clone the repository:
```sh
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
```

Create and activate a virtual environment:
```sh
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

Install dependencies:
```sh
pip install -r requirements.txt
```

Apply migrations:
```sh
python manage.py migrate
```

Create a superuser (admin):
```sh
python manage.py createsuperuser
```

Collect static files:
```sh
python manage.py collectstatic
```

Run the development server:
```sh
python manage.py runserver
```

Access the application at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

## Usage
### Teacher Management
- **View Teachers:** Navigate to the "Teachers" section to see all registered teachers.
- **Add Teacher:** Use the "Add New Teacher" button to create a new teacher record.
- **Edit/Delete:** Modify or remove teacher records as needed.

### Student Management
- **View Students:** Navigate to the "Students" section to see all registered students.
- **Add Student:** Use the "Add New Student" button to create a new student record.
- **Edit/Delete:** Modify or remove student records as needed.

### Subject Management
- **View Subjects:** Browse available subjects.
- **Add Subject:** Create new subjects.
- **Manage Subjects:** View and edit subject details.

## Project Structure
```
student-management-system/
├── accounts/                  # Main application
│   ├── migrations/            # Database migrations
│   ├── static/                # Static files (CSS, JS)
│   │   └── css/
│   │       └── style.css      # Custom styling
│   ├── templates/             # HTML templates
│   ├── admin.py               # Admin configuration
│   ├── forms.py               # Form definitions
│   ├── models.py              # Data models
│   ├── urls.py                # URL routing
│   └── views.py               # View controllers
├── coreproject/               # Project settings
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL routing
│   └── wsgi.py                # WSGI configuration
├── static/                    # Collected static files
├── staticfiles/               # Production static files
├── manage.py                  # Django management script
└── requirements.txt           # Project dependencies
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add some amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

## Acknowledgments
- Django documentation and community
- Bootstrap for design inspiration
- All contributors who have helped improve this project

