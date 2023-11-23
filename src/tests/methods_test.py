import unittest
import methods
from db_connection import get_database_connection

class MethodsTest(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection()
        # self.engine = create_engine('sqlite:///:memory:')
        # self.connection = self.engine.connect()
        self.connection.execute("CREATE TABLE reference ("
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