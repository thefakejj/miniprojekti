from flask import make_response
from sqlalchemy.sql import text
from app import db
import random
import os

class InvalidInputError(Exception):
    pass

def send_book(username, author, title, p_year, publisher, volume, series, address, edition, month, note):
    reftype = "book"
    if p_year.isalpha():
        raise InvalidInputError("Vuosi väärin!")
    else:
        year = int(p_year)
        if year < 0 or year > 3000:
            raise InvalidInputError("Vuosi väärin!")

    key = generate_key(author,year)

    if len(username) > 100:
        raise InvalidInputError("Liian pitkä username syöte!")
    if len(author) > 100:
        raise InvalidInputError("Liian pitkä author syöte!")
    if len(title) > 100:
        raise InvalidInputError("Liian pitkä title syöte!")
    if len(publisher) > 100:
        raise InvalidInputError("Liian pitkä publisher syöte!")
    if len(volume) > 100:
        raise InvalidInputError("Liian pitkä volume syöte!")
    if len(series) > 100:
        raise InvalidInputError("Liian pitkä series syöte!")
    if len(address) > 100:
        raise InvalidInputError("Liian pitkä address syöte!")
    if len(edition) > 100:
        raise InvalidInputError("Liian pitkä edition syöte!")
    if len(note) > 100:
        raise InvalidInputError("Liian pitkä note syöte!")
    
    if len(month) > 3:
        raise InvalidInputError("Syötä kuukausi tyylillä 'jan', 'feb' jne.")
    
    sql = text("INSERT INTO reference (reftype, username, key, author, title, year, publisher, volume, series, address, edition, month, note) VALUES (:reftype, :username, :key, :author, :title, :year, :publisher, :volume, :series, :address, :edition, :month, :note)")
    db.session.execute(sql, {"reftype":reftype, "username":username, "key":key, "author":author, "title":title, "year":year, "publisher":publisher, "volume":volume, "series":series, "address":address, "edition":edition, "month":month, "note":note})
    db.session.commit()
    return True 

def get_books():
    sql = text("SELECT username, key, author, title, year, publisher, volume, series, address, edition, month, note FROM reference WHERE reftype LIKE '%book%'")
    result = db.session.execute(sql)
    books = result.fetchall()
    return books

def send_master(username, author, title, school, p_year, type, address, month, note):
    reftype = "master"
    
    if p_year.isalpha():
        raise InvalidInputError("Vuosi väärin!")
    else:
        year = int(p_year)
        if year < 0 or year > 3000:
            raise InvalidInputError("Vuosi väärin!")
        
    key = generate_key(author,year)

    if len(username) > 100:
        raise InvalidInputError("Liian pitkä username syöte!")
    if len(author) > 100:
        raise InvalidInputError("Liian pitkä author syöte!")
    if len(title) > 100:
        raise InvalidInputError("Liian pitkä title syöte!")
    if len(school) > 100:
        raise InvalidInputError("Liian pitkä school syöte!")
    if len(type) > 100:
        raise InvalidInputError("Liian pitkä type syöte!")
    if len(address) > 100:
        raise InvalidInputError("Liian pitkä address syöte!")
    if len(note) > 100:
        raise InvalidInputError("Liian pitkä note syöte!")
    
    if len(month) > 3:
        raise InvalidInputError("Syötä kuukausi tyylillä 'jan', 'feb' jne.")
    
    sql = text("INSERT INTO reference (reftype, username, key, author, title, school, year, type, address, month, note) VALUES (:reftype, :username, :key, :author, :title, :school, :year, :type, :address, :month, :note)")
    db.session.execute(sql, {"reftype":reftype, "username":username, "key":key, "author":author, "title":title, "school":school, "year":year, "type":type, "address":address, "month":month, "note":note})
    db.session.commit()
    return True

def get_references():
    sql = text("SELECT * FROM reference")
    result = db.session.execute(sql)
    references = result.fetchall()
    return references

def get_master():
    sql = text('''
        SELECT username, key, author, title, year, type, address, month, note, school 
        FROM reference 
        WHERE reftype LIKE '%master%' 
        ''')
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

def edit_book(username, key, author, title, year, publisher, volume, series, address, edition, month, note):
    reftype = "book"
    sql = text("UPDATE reference SET reftype = :reftype, username = :username, author = :author, title = :title, year = :year, publisher = :publisher, volume = :volume, series = :series, address = :address, edition = :edition, month = :month, note = :note WHERE key = :key")
    db.session.execute(sql, {"reftype": reftype, "username": username, "key": key, "author": author, "title": title, "year": year, "publisher": publisher, "volume": volume, "series": series, "address": address, "edition": edition, "month": month, "note": note})
    db.session.commit()
    return True

def edit_master(username, key, author, title, school, year, type, address, month, note):
    reftype = "master"
    sql = text("UPDATE reference SET reftype = :reftype, username = :username, author = :author, title = :title, school = :school, year = :year, type = :type, address = :address, month = :month, note = :note WHERE key = :key")
    db.session.execute(sql, {"reftype": reftype, "username": username, "key": key, "author": author, "title": title, "school": school, "year": year, "type": type, "address": address, "month": month, "note": note})
    db.session.commit()
    return True

def get_all_references_dict():
    refs_dict = {}
    refs_dict["books"] = get_books()
    refs_dict["masters"] = get_master()

    return refs_dict

def create_book_bibtex_format(book):
    book_ref_text = f'''@book{{{book[1]},
author = {{{book[2]}}},
title = {{{book[3]}}},
year = {{{book[4]}}},
publisher = {{{book[5]}}},
volume = {{{book[6]}}},
series = {{{book[7]}}},
address = {{{book[8]}}},
edition = {{{book[9]}}},
month = {{{book[10]}}},
note = {{{book[11]}}}             
}}
    '''
    return book_ref_text

def create_master_bibtex_format(master):
    master_ref_text = f'''@masterthesis{{{master[1]},
author = {{{master[2]}}},
title = {{{master[3]}}},
year = {{{master[4]}}},
type = {{{master[5]}}},
address = {{{master[6]}}},
month = {{{master[7]}}},
note = {{{master[8]}}},
school = {{{master[9]}}}          
}}
    '''
    return master_ref_text

def create_bibtex_text():
    bibtex_string = ""
    refs_dict = get_all_references_dict()
    for book in refs_dict["books"]:
        bibtex_string += create_book_bibtex_format(book)+"\n"

    for master in refs_dict["masters"]:
        bibtex_string += create_master_bibtex_format(master)+"\n"
    return bibtex_string

def create_bibtex_file():

    if os.path.exists("src/outputs/references.bib"):
        os.remove("src/outputs/references.bib")
    bibtex_string = create_bibtex_text()
    with open("src/outputs/references.bib", "w", encoding='utf-8') as bibtex_file:
        bibtex_file.write(bibtex_string)

#varovasti sitte tän kanssa
def nuke_db():
    sql = text("DROP TABLE reference")
    db.session.execute(sql)
    db.session.commit()
    return True
