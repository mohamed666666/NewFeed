
from ..connection import get_db

class User:
    @staticmethod
    def get_all():
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        return cursor.fetchall()

    @staticmethod
    def create(name, email):
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()