# db_server.py

import pyodbc
from db_config import DATABASES

def get_connection():
    db_config = DATABASES['default']
    conn_str = (
        f"DRIVER={{{db_config['OPTIONS']['driver']}}};"
        f"SERVER={db_config['HOST']};"
        f"DATABASE={db_config['NAME']};"
        f"UID={db_config['USER']};"
        f"PWD={db_config['PASSWORD']};"
    )
    return pyodbc.connect(conn_str)
