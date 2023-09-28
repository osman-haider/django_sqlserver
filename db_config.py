DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'data base name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'server_name',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}
