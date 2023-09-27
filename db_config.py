DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'your_db_name',
        'USER': 'your_db_user_name',
        'PASSWORD': 'password',
        'HOST': 'server',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}
