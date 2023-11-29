from flask import make_response
from sqlalchemy.sql import text
from app import db
import random

def send_book(username, author, title, year, publisher, volume, series, address, edition, month, note):
    reftype = "book"
    key = generate_key(author,year)
    sql = text("INSERT INTO reference (reftype, username, key, author, title, year, publisher, volume, series, address, edition, month, note) VALUES (:reftype, :username, :key, :author, :title, :year, :publisher, :volume, :series, :address, :edition, :month, :note)")
    db.session.execute(sql, {"reftype":reftype, "username":username, "key":key, "author":author, "title":title, "year":year, "publisher":publisher, "volume":volume, "series":series, "address":address, "edition":edition, "month":month, "note":note})
    db.session.commit()
    return True

def get_books():
    sql = text("SELECT username, key, author, title, year, publisher, volume, series, address, edition, month, note FROM reference WHERE reftype LIKE '%book%'")
    result = db.session.execute(sql)
    books = result.fetchall()
    return books

def send_master(username, author, title, school, year, type, address, month, note):
    reftype = "master"
    key = generate_key(author,year)
    sql = text("INSERT INTO reference (reftype, username, key, author, title, school, year, type, address, month, note) VALUES (:reftype, :username, :key, :author, :title, :school, :year, :type, :address, :month, :note)")
    db.session.execute(sql, {"reftype":reftype, "username":username, "key":key, "author":author, "title":title, "school":school, "year":year, "type":type, "address":address, "month":month, "note":note})
    db.session.commit()
    return True

def get_master():
    sql = text("SELECT username, key, author, title, year, type, address, month, note, school FROM reference WHERE reftype LIKE '%master%'")
    result = db.session.execute(sql)
    master = result.fetchall()
    return master

def get_keys():
    sql = text("SELECT key FROM reference")
    result = db.session.execute(sql)
    master = result.fetchall()
    return master

def generate_key(author, year):
    year = str(year)
    authkey = author[:2]
    yearkey = year[2:]
    key = authkey + yearkey
    return key_is_unique(key)

def key_is_unique(key):
    sql = text("SELECT COUNT(*) FROM reference WHERE key = :key")
    result = db.session.execute(sql, {"key": key})
    count = result.scalar()
    if count > 0:
        key += str(random.randint(1,100))
    return key

def keyview(key):
    sql = text("SELECT * FROM reference WHERE key = :key")
    result = db.session.execute(sql, {"key": key})
    view = result.fetchone()
    return view

def delete_reference(key):
    sql = text("DELETE FROM reference WHERE key = :key")
    result = db.session.execute(sql, {"key": key})
    db.session.commit()
    return True