import unittest
import methods
from config import DATABASE_FILE_PATH
from app import app
import sqlite3
#from db_connection import get_database_connection

class MethodsTest(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            #self.connection = get_database_connection()
            self.connection = sqlite3.connect(DATABASE_FILE_PATH)
            self.cursor = self.connection.cursor()
            self.cursor.execute("DROP TABLE reference")
            # self.engine = create_engine('sqlite:///:memory:')
            # self.connection = self.engine.connect()
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS reference (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reftype TEXT NOT NULL,
                username TEXT,
                key TEXT NOT NULL,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                year INTEGER NOT NULL,
                publisher TEXT NOT NULL,
                volume TEXT,
                series TEXT,
                address TEXT,
                edition TEXT,
                month TEXT,
                note TEXT,
                school TEXT,
                type TEXT
                    )
                """)
            self.connection.commit()

    def test_send_and_get_books(self):
        with app.app_context():
            methods.send_book("user1", "Author1", "Title1", 2022, "Publisher1")
            methods.send_book("user2", "Author2", "Title2", 2023, "Publisher2")

            books = methods.get_books()
            self.assertEqual(len(books), 2)
    
    def test_key_generation(self):
        with app.app_context():
            methods.send_book("user3", "Author3", "Title3", 1987, "Publisher3")
            methods.send_book("user4", "Author3", "Title4", 1887, "Publisher4")

            books = methods.get_books()
            key3 = books[0][1]
            key4 = books[1][1]
            self.assertNotEqual(key3, key4)