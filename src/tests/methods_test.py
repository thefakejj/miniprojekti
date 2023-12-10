import unittest
import methods
from config import DATABASE_FILE_PATH
from app import app
import sqlite3
import os
from db_connection import get_database_connection
from methods import InvalidInputError
from pathlib import Path

# self.connection = get_database_connection()
# self.engine = create_engine('sqlite:///:memory:')
# self.connection = self.engine.connect()

class MethodsTest(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            self.connection = sqlite3.connect(DATABASE_FILE_PATH)
            self.cursor = self.connection.cursor()
            self.cursor.execute("DROP TABLE reference")
            self.too_long = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS reference (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reftype TEXT NOT NULL,
                username TEXT, 
                key TEXT NOT NULL, 
                author TEXT, 
                title TEXT, 
                year INTEGER, 
                publisher TEXT,
                volume TEXT,
                series TEXT,
                address TEXT,
                edition TEXT,
                month TEXT,
                note TEXT,
                school TEXT,
                type TEXT,
                journal TEXT,
                number TEXT,
                pages TEXT
                    )
                """)
            self.connection.commit()

#------------------------------------------------------------

    def test_send_and_get_books(self):
        with app.app_context():
            methods.send_book("user1", "Author1", "Title1", "2022", "Publisher1", "volume7", "series7", "address7", "edition7", "aug", "note")
            methods.send_book("user2", "Author2", "Title2", "2023", "Publisher2", "", "", "", "", "", "")

            books = methods.get_books()
            self.assertEqual(len(books), 2)
    
    def test_and_send_books_all(self):
        with app.app_context():
            methods.send_book("user7", "Author7", "Title7", "2012", "Publisher7", "", "", "", "", "", "")

            books = methods.get_books()
            self.assertEqual(len(books), 1)

    def test_and_send_books_too_long_user(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book(self.too_long, "Author7", "Title7", "2012", "Publisher7", "", "", "", "", "", "")

    def test_and_send_books_too_long_author(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book("user7", self.too_long, "Title7", "2012", "Publisher7", "", "", "", "", "", "")
    
    def test_and_send_books_too_long_title(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book("user7", "Author7", self.too_long, "2012", "Publisher7", "", "", "", "", "", "")
    
    def test_and_send_books_year_invalid_string(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book("user7", "Author7", "Title7", "väärä", "Publisher7", "", "", "", "", "", "")
    
    def test_and_send_books_year_invalid_negative(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book("user7", "Author7", "Title7", "-1", "Publisher7", "", "", "", "", "", "")
        
    def test_and_send_books_year_invalid_big(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book("user7", "Author7", "Title7", "4444", "Publisher7", "", "", "", "", "", "")

    def test_and_send_books_too_long_publisher(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book("user7", "Author7", "Title7", "2012", self.too_long, "", "", "", "", "", "")

    def test_and_send_books_too_long_volume(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book("user7", "Author7", "Title7", "2012", "Publisher7", self.too_long, "", "", "", "", "")
    
    def test_and_send_books_too_long_series(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book("user7", "Author7", "Title7", "2012", "Publisher7", "", self.too_long, "", "", "", "")

    def test_and_send_books_too_long_address(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book("user7", "Author7", "Title7", "2012", "Publisher7", "", "", self.too_long, "", "", "")

    def test_and_send_books_too_long_edition(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book("user7", "Author7", "Title7", "2012", "Publisher7", "", "", "", self.too_long, "", "")

    def test_and_send_books_too_long_note(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book("user7", "Author7", "Title7", "2012", "Publisher7", "", "", "", "", "", self.too_long)

    def test_and_send_books_too_long_month(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_book("user7", "Author7", "Title7", "2012", "Publisher7", "", "", "", "", "väärä", "")

#------------------------------------------------------------

    def test_send_and_get_master(self):
        with app.app_context():
            methods.send_master("user4", "Author4", "Title4", "School4", "2022", "", "", "", "")
            methods.send_master("user5", "Author5", "Title5", "School5", "2023", "", "", "", "")

            master = methods.get_master()
            self.assertEqual(len(master), 2)
    
    def test_send_and_get_master_all(self):
        with app.app_context():
            methods.send_master("user8", "Author8", "Title8", "School8", "2018", "type", "address8", "feb", "note8")
            master = methods.get_master()
            self.assertEqual(len(master), 1)
    
    def test_and_send_master_too_long_user(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_master(self.too_long, "Author4", "Title4", "School4", "2022", "", "", "", "")
    
    def test_and_send_master_too_long_author(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_master("user8", self.too_long, "Title4", "School4", "2022", "", "", "", "")
    
    def test_and_send_master_too_long_title(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_master("user8", "Author4", self.too_long, "School4", "2022", "", "", "", "")
    
    def test_and_send_master_too_long_school(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_master("user8", "Author4", "Title4", self.too_long, "2022", "", "", "", "")
    
    def test_and_send_master_too_long_type(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_master("user8", "Author4", "Title4", "School4", "2022", self.too_long, "", "", "")

    def test_and_send_master_too_long_address(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_master("user8", "Author4", "Title4", "School4", "2022", "", self.too_long, "", "")

    def test_and_send_master_too_long_note(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_master("user8", "Author4", "Title4", "School4", "2022", "", "", "", self.too_long)

    def test_and_send_master_too_long_month(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_master("user8", "Author4", "Title4", "School4", "2022", "", "", "väärä", "")
    
    def test_and_send_master_year_invalid_string(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_master("user8", "Author4", "Title4", "School4", "väärä", "", "", "", "")
    
    def test_and_send_master_year_invalid_negative(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_master("user8", "Author4", "Title4", "School4", "-1", "", "", "", "")
    
    def test_and_send_master_year_invalid_big(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_master("user8", "Author4", "Title4", "School4", "4444", "", "", "", "")

#------------------------------------------------------------

    def test_send_and_get_phdthesis(self):
        with app.app_context():
            methods.send_phdthesis("user4", "Author4", "Title4", "School4", "2022", "", "", "", "")
            methods.send_phdthesis("user5", "Author5", "Title5", "School5", "2023", "", "", "", "")

            phdthesis = methods.get_phdthesis()
            self.assertEqual(len(phdthesis), 2)
    
    def test_send_and_get_phdthesis_all(self):
        with app.app_context():
            methods.send_phdthesis("user8", "Author8", "Title8", "School8", "2018", "type", "address8", "feb", "note8")
            phdthesis = methods.get_phdthesis()
            self.assertEqual(len(phdthesis), 1)
    
    def test_and_send_phdthesis_too_long_user(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_phdthesis(self.too_long, "Author4", "Title4", "School4", "2022", "", "", "", "")
    
    def test_and_send_phdthesis_too_long_author(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_phdthesis("user8", self.too_long, "Title4", "School4", "2022", "", "", "", "")
    
    def test_and_send_phdthesis_too_long_title(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_phdthesis("user8", "Author4", self.too_long, "School4", "2022", "", "", "", "")
    
    def test_and_send_phdthesis_too_long_school(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_phdthesis("user8", "Author4", "Title4", self.too_long, "2022", "", "", "", "")
    
    def test_and_send_phdthesis_too_long_type(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_phdthesis("user8", "Author4", "Title4", "School4", "2022", self.too_long, "", "", "")

    def test_and_send_phdthesis_too_long_address(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_phdthesis("user8", "Author4", "Title4", "School4", "2022", "", self.too_long, "", "")

    def test_and_send_phdthesis_too_long_note(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_phdthesis("user8", "Author4", "Title4", "School4", "2022", "", "", "", self.too_long)

    def test_and_send_phdthesis_too_long_month(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_phdthesis("user8", "Author4", "Title4", "School4", "2022", "", "", "väärä", "")
    
    def test_and_send_phdthesis_year_invalid_string(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_phdthesis("user8", "Author4", "Title4", "School4", "väärä", "", "", "", "")
    
    def test_and_send_phdthesis_year_invalid_negative(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_phdthesis("user8", "Author4", "Title4", "School4", "-1", "", "", "", "")
    
    def test_and_send_phdthesis_year_invalid_big(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_phdthesis("user8", "Author4", "Title4", "School4", "4444", "", "", "", "")

#------------------------------------------------------------

    def test_send_and_get_article(self):
        with app.app_context():
            methods.send_article("user1", "Author1", "Title1", "Journal1", "1999", "volume1", "number1", "pages1", "aug", "note")
            methods.send_article("user2", "Author2", "Title2", "Journal2", "1999", "", "", "", "", "")

            articles = methods.get_article()
            self.assertEqual(len(articles), 2)
    
    def test_and_send_article_all(self):
        with app.app_context():
            methods.send_article("user1", "Author1", "Title1", "Journal1", "1999", "", "", "", "", "")

            articles = methods.get_article()
            self.assertEqual(len(articles), 1)

    def test_and_send_article_too_long_user(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article(self.too_long, "Author7", "Title7", "Journal1", "1999", "", "", "", "", "")

    def test_and_send_article_too_long_author(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", self.too_long, "Title7", "Journal1", "1999", "", "", "", "", "")
    
    def test_and_send_article_too_long_title(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", "Author7", self.too_long, "Journal1", "1999", "", "", "", "", "")

    def test_and_send_article_too_long_journal(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", "Author7", "Title7", self.too_long, "1999", "", "", "", "", "")
    
    def test_and_send_article_year_invalid_string(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", "Author7", "Title7", "Journal1", "väärä", "", "", "", "", "")
    
    def test_and_send_article_year_invalid_negative(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", "Author7", "Title7", "Journal1", "-1", "", "", "", "", "")
        
    def test_and_send_article_year_invalid_big(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", "Author7", "Title7", "Journal1", "4444", "", "", "", "", "")

    def test_and_send_article_too_long_publisher(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", "Author7", "Title7", "1999", self.too_long, "", "", "", "", "")

    def test_and_send_article_too_long_volume(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", "Author7", "Title7", "Journal1", "1999", self.too_long, "", "", "", "")
    
    def test_and_send_article_too_long_series(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", "Author7", "Title7", "Journal1", "1999", "", self.too_long, "", "", "")

    def test_and_send_article_too_long_address(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", "Author7", "Title7", "Journal1", "1999", "", self.too_long, "", "", "")

    def test_and_send_article_too_long_edition(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", "Author7", "Title7", "Journal1", "1999", "", "", self.too_long, "", "")

    def test_and_send_article_too_long_note(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", "Author7", "Title7", "Journal1", "1999", "", "", "", "", self.too_long)

    def test_and_send_article_wrong_input_month(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.send_article("user7", "Author7", "Title7", "Journal1", "1999", "", "", "", "väärä", "")

#------------------------------------------------------------

    def test_key_generation(self):
        with app.app_context():
            methods.send_book("user3", "Author3", "Title3", "1987", "Publisher3", "", "", "", "", "", "")
            methods.send_book("user4", "Author3", "Title4", "1887", "Publisher4", "", "", "", "", "", "")

            books = methods.get_books()
            key3 = books[0][1]
            key4 = books[1][1]
            self.assertNotEqual(key3, key4)

#------------------------------------------------------------
    
    def test_delete_book(self):
        with app.app_context():
            methods.send_book("user3", "Author6", "Title6", "1987", "Publisher3", "", "", "", "", "", "")

            methods.delete_reference("Au87")

            keys_after = [key[0] for key in methods.get_keys()]
            self.assertNotIn("Au87", keys_after)
    
    def test_delete_master(self):
        with app.app_context():
            methods.send_master("user9", "Author9", "Title9", "School9", "1999", "", "", "", "")

            methods.delete_reference("Au99")

            keys_after = [key[0] for key in methods.get_keys()]
            self.assertNotIn("Au99", keys_after)

#------------------------------------------------------------

    def test_edit_book(self):
        with app.app_context():
            methods.send_book("user5", "Testikirjailija", "Tämäpoistetaan_title", "1921", "Publisher5", "", "", "", "", "","")
            methods.edit_book("user5", "Te21", "Testikirjailija", "Kirjannimi", "1921", "Publisher5", "2222", "", "", "", "", "")
            after = methods.get_references()
            self.assertNotIn("Tämäpoistetaan_title", after[0])
            self.assertIn("2222", after[0])

    def test_edit_master(self):
        with app.app_context():
            methods.send_master("user4", "Author4", "Tämäpoistetaan_title", "School4", "2022", "", "", "", "")
            methods.edit_master("user4", "Au22", "Author4", "Title_after", "School4", "2022", "2222", "", "", "")
            after = methods.get_references()
            self.assertNotIn("Tämäpoistetaan_title", after[0])
            self.assertIn("2222", after[0])

    def test_edit_article(self):
        with app.app_context():
            methods.send_article("user4", "Author4", "Tämäpoistetaan_title", "Journal1", "2022", "", "", "", "", "")
            methods.edit_article("user4", "Au22", "Author4", "Title_after", "School4", "2022", "2222", "", "", "", "")
            after = methods.get_references()
            self.assertNotIn("Tämäpoistetaan_title", after[0])
            self.assertIn("2222", after[0])

    def test_edit_phdthesis(self):
        with app.app_context():
            methods.send_phdthesis("user4", "Author4", "Tämäpoistetaan_title", "School4", "2022", "", "", "", "")
            methods.edit_phdthesis("user4", "Au22", "Author4", "Title_after", "School4", "2022", "2222", "", "", "")
            after = methods.get_references()
            self.assertNotIn("Tämäpoistetaan_title", after[0])
            self.assertIn("2222", after[0])

#------------------------------------------------------------
    
    def test_create_bibtex_file_when_doesnt_exist(self):
        if os.path.exists("src/outputs/references.bib"):
            os.remove("src/outputs/references.bib")
        with app.app_context():
            methods.send_book("user7", "Author7", "Title7", "2012", "Publisher7", "", "", "", "", "", "")
            methods.send_master("user4", "Author4", "Title4", "School4", "2022", "", "", "", "")
            methods.send_article("user3", "Author2", "Title3", "Journal2", "2002", "","","","","")
            methods.create_bibtex_file()
            self.assertTrue(os.path.exists("src/outputs/references.bib"))

    def test_create_bibtex_file_correct_start(self):
        with app.app_context():
            methods.send_book("user7", "Author7", "Title7", "2012", "Publisher7", "", "", "", "", "", "")
            methods.create_bibtex_file()
            with open("src/outputs/references.bib", 'r', encoding='utf-8') as file:
                self.assertIn("@book{Au12,\n", file)

    def test_create_bibtex_file_correct_after_new_file(self):
        with app.app_context():
            methods.send_book("user7", "Author7", "Title7", "2012", "Publisher7", "", "", "", "", "", "")
            methods.create_bibtex_file()
            with open("src/outputs/references.bib", 'r', encoding='utf-8') as file:
                self.assertIn("@book{Au12,\n", file)
            methods.send_master("user4", "Author4", "Title4", "School4", "2022", "", "", "", "")
            methods.create_bibtex_file()
            with open("src/outputs/references.bib", 'r', encoding='utf-8') as file:
                self.assertIn("@masterthesis{Au22,\n", file)
            methods.send_article("user2", "Author2", "Title2", "Journal2", "2002", "", "", "", "", "")
            methods.create_bibtex_file()
            with open("src/outputs/references.bib", 'r', encoding='utf-8') as file:
                self.assertIn("@article{Au02,\n", file)

#------------------------------------------------------------

    def test_get_references_by_author(self):
        with app.app_context():
            methods.send_book("user7", "Author7", "Title7", "2012", "Publisher7", "", "", "", "", "", "")
            methods.send_book("user4", "Author4", "Title4", "2022", "Publisher6", "", "", "", "", "", "")
            methods.get_references_by_author()
            references = methods.get_references()
            self.assertEqual(references[1][4], "Author4")
            self.assertEqual(references[0][4], "Author7")

    def test_get_references_by_year(self):
        with app.app_context():
            methods.send_book("user4", "Author4", "Title4", "2022", "Publisher6", "", "", "", "", "", "")
            methods.send_book("user7", "Author7", "Title7", "2012", "Publisher7", "", "", "", "", "", "")
            methods.get_references_by_year()
            references = methods.get_references()
            self.assertEqual(references[1][4], "Author7")
            self.assertEqual(references[0][4], "Author4")

#------------------------------------------------------------

    def test_get_references_search_reftype(self):
        with app.app_context():
            methods.send_book("user4", "Author4", "Title4", "2022", "Publisher6", "", "", "", "", "", "")
            methods.send_master("user3", "Author3", "title3", "School3", "2022", "", "", "", "")
            references = methods.get_reference_search("book")
            self.assertIn(references[0][1], "book")
            self.assertNotIn(references[0][1], "master")
    
    def test_get_references_search_username(self):
        with app.app_context():
            methods.send_book("user4", "Author4", "Title4", "2022", "Publisher6", "", "", "", "", "", "")
            methods.send_master("user3", "Author3", "title3", "School3", "2022", "", "", "", "")
            references = methods.get_reference_search("user4")
            self.assertIn(references[0][2], "user4")
            self.assertNotIn(references[0][2], "user3")
    
    def test_get_references_search_key(self):
        with app.app_context():
            methods.send_book("user4", "Author4", "Title4", "2022", "Publisher6", "", "", "", "", "", "")
            methods.send_master("user3", "Author3", "title3", "School3", "2021", "", "", "", "")
            references = methods.get_reference_search("Au22")
            self.assertIn(references[0][3], "Au22")
            self.assertNotIn(references[0][3], "Au21")
    
    def test_get_references_search_author(self):
        with app.app_context():
            methods.send_book("user4", "Author4", "Title4", "2022", "Publisher6", "", "", "", "", "", "")
            methods.send_master("user3", "Author3", "title3", "School3", "2021", "", "", "", "")
            references = methods.get_reference_search("Au22")
            self.assertIn(references[0][4], "Author4")
            self.assertNotIn(references[0][4], "Author3")
    
    def test_get_references_search_title(self):
        with app.app_context():
            methods.send_book("user4", "Author4", "Title4", "2022", "Publisher6", "", "", "", "", "", "")
            methods.send_master("user3", "Author3", "title3", "School3", "2021", "", "", "", "")
            references = methods.get_reference_search("Title4")
            self.assertIn(references[0][5], "Title4")
            self.assertNotIn(references[0][5], "Title3")
    
    def test_get_references_search_year(self):
        with app.app_context():
            methods.send_book("user4", "Author4", "Title4", "2022", "Publisher6", "", "", "", "", "", "")
            methods.send_master("user3", "Author3", "title3", "School3", "2021", "", "", "", "")
            references = methods.get_reference_search("2021")
            self.assertIn(str(references[0][6]), "2021")
            self.assertNotIn(str(references[0][6]), "2022")

#------------------------------------------------------------

    def test_and_edit_books_too_long_user(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book(self.too_long, "key7", "Author7", "Title7", "2012", "Publisher7", "", "", "", "", "", "")

    def test_and_edit_books_too_long_author(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book("user7", "key7", self.too_long, "Title7", "2012", "Publisher7", "", "", "", "", "", "")
    
    def test_and_edit_books_too_long_title(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book("user7", "key7","Author7", self.too_long, "2012", "Publisher7", "", "", "", "", "", "")
    
    def test_and_edit_books_year_invalid_string(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book("user7", "key7","Author7", "Title7", "väärä", "Publisher7", "", "", "", "", "", "")
    
    def test_and_edit_books_year_invalid_negative(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book("user7", "key7","Author7", "Title7", "-1", "Publisher7", "", "", "", "", "", "")
        
    def test_and_edit_books_year_invalid_big(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book("user7", "key7","Author7", "Title7", "4444", "Publisher7", "", "", "", "", "", "")

    def test_and_edit_books_too_long_publisher(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book("user7", "key7","Author7", "Title7", "2012", self.too_long, "", "", "", "", "", "")

    def test_and_edit_books_too_long_volume(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book("user7", "key7","Author7", "Title7", "2012", "Publisher7", self.too_long, "", "", "", "", "")
    
    def test_and_edit_books_too_long_series(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book("user7", "key7","Author7", "Title7", "2012", "Publisher7", "", self.too_long, "", "", "", "")

    def test_and_edit_books_too_long_address(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book("user7", "key7", "Author7", "Title7", "2012", "Publisher7", "", "", self.too_long, "", "", "")

    def test_and_edit_books_too_long_edition(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book("user7", "key7", "Author7", "Title7", "2012", "Publisher7", "", "", "", self.too_long, "", "")

    def test_and_edit_books_too_long_note(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book("user7", "key7", "Author7", "Title7", "2012", "Publisher7", "", "", "", "", "", self.too_long)

    def test_and_edit_books_too_long_month(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_book("user7", "key7", "Author7", "Title7", "2012", "Publisher7", "", "", "", "", "väärä", "")  

#------------------------------------------------------------
    
    def test_and_edit_master_too_long_user(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_master(self.too_long, "key8", "Author4", "Title4", "School4", "2022", "", "", "", "")
    
    def test_and_edit_master_too_long_author(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_master("user8", "key8", self.too_long, "Title4", "School4", "2022", "", "", "", "")
    
    def test_and_edit_master_too_long_title(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_master("user8", "key8", "Author4", self.too_long, "School4", "2022", "", "", "", "")
    
    def test_and_edit_master_too_long_school(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_master("user8", "key8", "Author4", "Title4", self.too_long, "2022", "", "", "", "")
    
    def test_and_edit_master_too_long_type(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_master("user8", "key8", "Author4", "Title4", "School4", "2022", self.too_long, "", "", "")

    def test_and_edit_master_too_long_address(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_master("user8", "key8", "Author4", "Title4", "School4", "2022", "", self.too_long, "", "")

    def test_and_edit_master_too_long_note(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_master("user8", "key8", "Author4", "Title4", "School4", "2022", "", "", "", self.too_long)

    def test_and_edit_master_too_long_month(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_master("user8", "key8", "Author4", "Title4", "School4", "2022", "", "", "väärä", "")
    
    def test_and_edit_master_year_invalid_string(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_master("user8", "key8", "Author4", "Title4", "School4", "väärä", "", "", "", "")
    
    def test_and_edit_master_year_invalid_negative(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_master("user8", "key8", "Author4", "Title4", "School4", "-1", "", "", "", "")
    
    def test_and_edit_master_year_invalid_big(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_master("user8", "key8", "Author4", "Title4", "School4", "4444", "", "", "", "")

#------------------------------------------------------------
    
    def test_and_edit_phdthesis_too_long_user(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_phdthesis(self.too_long, "key8", "Author4", "Title4", "School4", "2022", "", "", "", "")
    
    def test_and_edit_phdthesis_too_long_author(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_phdthesis("user8", "key8", self.too_long, "Title4", "School4", "2022", "", "", "", "")
    
    def test_and_edit_phdthesis_too_long_title(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_phdthesis("user8", "key8", "Author4", self.too_long, "School4", "2022", "", "", "", "")
    
    def test_and_edit_phdthesis_too_long_school(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_phdthesis("user8", "key8", "Author4", "Title4", self.too_long, "2022", "", "", "", "")
    
    def test_and_edit_phdthesis_too_long_type(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_phdthesis("user8", "key8", "Author4", "Title4", "School4", "2022", self.too_long, "", "", "")

    def test_and_edit_phdthesis_too_long_address(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_phdthesis("user8", "key8", "Author4", "Title4", "School4", "2022", "", self.too_long, "", "")

    def test_and_edit_phdthesis_too_long_note(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_phdthesis("user8", "key8", "Author4", "Title4", "School4", "2022", "", "", "", self.too_long)

    def test_and_edit_phdthesis_too_long_month(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_phdthesis("user8", "key8", "Author4", "Title4", "School4", "2022", "", "", "väärä", "")
    
    def test_and_edit_phdthesis_year_invalid_string(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_phdthesis("user8", "key8", "Author4", "Title4", "School4", "väärä", "", "", "", "")
    
    def test_and_edit_phdthesis_year_invalid_negative(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_phdthesis("user8", "key8", "Author4", "Title4", "School4", "-1", "", "", "", "")
    
    def test_and_edit_phdthesis_year_invalid_big(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_phdthesis("user8", "key8", "Author4", "Title4", "School4", "4444", "", "", "", "")

#------------------------------------------------------------

    def test_and_edit_article_too_long_user(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_article(self.too_long, "key8", "Author4", "Title4", "Journal1", "2022", "", "", "", "", "")

    def test_and_edit_article_too_long_author(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_article("user8", "key8", self.too_long, "Title4", "Journal1", "2022", "", "", "", "", "")
    
    def test_and_edit_article_too_long_title(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_article("user8", "key8", "Author4", self.too_long, "Journal1", "2022", "", "", "", "", "")

    def test_and_edit_article_too_long_journal(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_article("user8", "key8", "Author4", "Title4", self.too_long, "2022", "", "", "", "", "")

    def test_and_edit_article_too_long_volume(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_article("user8", "key8", "Author4", "Title4", "Journal1", "2022", self.too_long, "", "", "", "")

    def test_and_edit_article_too_long_number(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_article("user8", "key8", "Author4", "Title4", "Journal1", "2022", "", self.too_long, "", "", "")

    def test_and_edit_article_too_long_pages(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_article("user8", "key8", "Author4", "Title4", "Journal1", "2022", "", "", self.too_long, "", "")

    def test_and_edit_article_too_long_month(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_article("user8", "key8", "Author4", "Title4", "Journal1", "2022", "", "", "", "väärä", "")

    def test_and_edit_article_too_long_note(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_article("user8", "key8", "Author4", "Title4", "Journal1", "2022", "", "", "", "", self.too_long)
    
    def test_and_edit_article_year_invalid_string(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_article("user8", "key8", "Author4", "Title4", "Journal1", "väärä", "", "", "", "", "")
    
    def test_and_edit_article_year_invalid_negative(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_article("user8", "key8", "Author4", "Title4", "Journal1", "-1", "", "", "", "", "")
    
    def test_and_edit_article_year_invalid_big(self):
        with app.app_context():
            with self.assertRaises(InvalidInputError):
                methods.edit_article("user8", "key8", "Author4", "Title4", "Journal1", "4444", "", "", "", "", "")
