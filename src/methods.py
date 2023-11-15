from flask import make_response
from app import db

def post_book(username, key, author, title, year, publisher):
    sql = "INSERT INTO book (username, key, author, title, year, publisher) VALUES (:username, :key, :author, :title, :year, :publisher)"
    db.session.execute(sql, {"username":username, "key":key, "author":author, "title":title, "year":year, "publisher"})
    db.session.commit()
    return True

