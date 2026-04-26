import sqlite3
import os

def fun_connection():
    os.makedirs("reportes", exist_ok=True)
    return sqlite3.connect(os.path.join("reportes", "clima.db"))
