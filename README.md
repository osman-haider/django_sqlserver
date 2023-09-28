# SQL Server Database Connection with Django App

This repository demonstrates how to connect a Django web application to a SQL Server database and perform CRUD (Create, Read, Update, Delete) operations using HTML templates. You can easily set up and use this repository by following the steps below.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- Python (3.6 or higher)
- Django (3.0 or higher)
- SQL Server
- SQL Server Database Credentials

### Clone the Repository

You can clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/your-repo-name.git
```

### Database Configuration

In order to connect your Django app to your SQL Server database, you need to provide your database credentials. Follow these steps:

1. Navigate to the `db_config.py` file in the project directory.
2. Open `db_config.py` in a text editor.

```python
# db_config.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlserver',  # Database engine for SQL Server
        'NAME': 'your-database-name',             # Replace with your database name
        'USER': 'your-username',                  # Replace with your SQL Server username
        'PASSWORD': 'your-password',              # Replace with your SQL Server password
        'HOST': 'your-host',                      # Replace with your SQL Server host (usually 'localhost')
        'PORT': '',                                # Leave this empty or replace with your port if needed
    }
}
```

3. Replace `'your-database-name'`, `'your-username'`, `'your-password'`, and `'your-host'` with your SQL Server database credentials.

### Running the Application

Once you have configured the database, you can run the Django application. Open your terminal/command prompt and navigate to the project directory. Then, run the following command:

```bash
python manage.py runserver
```

You will see a URL in the terminal, typically `localhost:8000`. Open your web browser and navigate to this URL.

### Accessing the Employee Data

By default, you can access the employee data at `localhost:8000/employee`. If you want to change the URL, you can do so in the `sqldkango/urls.py` file.

## Usage

- Visit the specified URL (e.g., `localhost:8000/employee`) in your web browser to view and interact with the employee data.
- Use the provided HTML templates to perform CRUD operations on the database.

## Customization

Feel free to customize the Django app, HTML templates, and database queries according to your specific requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [SQL Server Documentation](https://docs.microsoft.com/en-us/sql/sql-server/sql-server-technical-documentation)

Happy coding! If you have any questions or encounter any issues, please don't hesitate to open an issue in this repository or reach out to us.
