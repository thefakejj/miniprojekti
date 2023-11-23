from flask import make_response
from sqlalchemy.sql import text
from app import db

def send_book(username, author, title, year, publisher):
    sql = text("INSERT INTO reference (username, key, author, title, year, publisher) VALUES (:username, :key, :author, :title, :year, :publisher)")
    db.session.execute(sql, {"username":username, "key":generate_key(author,year), "author":author, "title":title, "year":year, "publisher":publisher})
    db.session.commit()
    return True

def get_books():
    sql = text("SELECT username, key, author, title, year, publisher FROM reference")
    result = db.session.execute(sql)
    books = result.fetchall()
    return books

def send_master(username, author, title, school, year, type, address, month, note):
    sql = text("INSERT INTO reference (username, key, author, title, school, year, type, address, month, note) VALUES (:username, :key, :author, :title, :school, :year, :address, :month, :note)")
    db.session.execute(sql, {"username":username, "key":generate_key(author,year), "author":author, "title":title, "school":school, "year":year, "type":type, "address":address, "month":month, "note":note})
    db.session.commit()
    return True

def get_master():
    sql = text("SELECT username, key, author, title, year, type, address, month, note, school FROM reference")
    result = db.session.execute(sql)
    master = result.fetchall()
    return master

def generate_key(author, year):
    year = str(year)
    authkey = author[:2]
    yearkey = year[2:]
    key = authkey + yearkey
    return key