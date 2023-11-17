from flask import make_response
from sqlalchemy.sql import text
from app import db

def send_book(username, key, author, title, year, publisher):
    sql = text("INSERT INTO book (username, key, author, title, year, publisher) VALUES (:username, :key, :author, :title, :year, :publisher)")
    db.session.execute(sql, {"username":username, "key":key, "author":author, "title":title, "year":year, "publisher":publisher})
    db.session.commit()
    return True

def get_books():
    sql = text("SELECT username, key, author, title, year, publisher FROM book")
    result = db.session.execute(sql)
    books = result.fetchall()
    return books

