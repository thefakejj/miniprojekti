import unittest
import methods
from config import DATABASE_FILE_PATH
import sqlite3
#from db_connection import get_database_connection

class MethodsTest(unittest.TestCase):
    def setUp(self):
        #self.connection = get_database_connection()
        self.connection = sqlite3.connect(DATABASE_FILE_PATH)
        self.cursor = self.connection.cursor()
        self.cursor.execute("DROP TABLE reference")
        # self.engine = create_engine('sqlite:///:memory:')
        # self.connection = self.engine.connect()
        self.cursor.execute("CREATE TABLE reference ("
                                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                "username TEXT,"
                                "key TEXT,"
                                "author TEXT,"
                                "title TEXT,"
                                "year INTEGER,"
                                "publisher TEXT,"
                                "school TEXT,"
                                "type TEXT,"
                                "address TEXT,"
                                "month TEXT,"
                                "note TEXT)"
                                )
        self.connection.commit()
    def test_send_and_get_books(self):
        methods.send_book("user1", "Author1", "Title1", 2022, "Publisher1")
        methods.send_book("user2", "Author2", "Title2", 2023, "Publisher2")

        books = methods.get_books()
        self.assertEqual(len(books), 2)
