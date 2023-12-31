from flask import make_response
from sqlalchemy.sql import text
from app import db
import random
import os

class InvalidInputError(Exception):
    pass

def send_book(username, author, title, p_year, publisher, volume, series, address, edition, month, note):
    reftype = "book"

    check_reference_validity([username, author, title, p_year, publisher, volume, series, address, edition, month, note],
                             ["username", "author", "title", "year", "publisher", "volume", "series", "address", "edition", "month", "note"])

    year = int(p_year)
    key = keygen(author,year)

    sql = text("INSERT INTO reference (reftype, username, key, author, title, year, publisher, volume, series, address, edition, month, note) VALUES (:reftype, :username, :key, :author, :title, :year, :publisher, :volume, :series, :address, :edition, :month, :note)")
    db.session.execute(sql, {"reftype":reftype, "username":username, "key":key, "author":author, "title":title, "year":year, "publisher":publisher, "volume":volume, "series":series, "address":address, "edition":edition, "month":month, "note":note})
    db.session.commit()
    return True 

def get_books():
    sql = text("SELECT username, key, author, title, year, publisher, volume, series, address, edition, month, note FROM reference WHERE reftype LIKE '%book%'")
    result = db.session.execute(sql)
    books = result.fetchall()
    return books

def send_masterthesis(username, author, title, school, p_year, type, address, month, note):
    reftype = "masterthesis"

    check_reference_validity([username, author, title, school, p_year, type, address, month, note],
                             ["username", "author", "title", "school", "year", "type", "address", "month", "note"])

    year = int(p_year)
    key = keygen(author,year)

    sql = text("INSERT INTO reference (reftype, username, key, author, title, school, year, type, address, month, note) VALUES (:reftype, :username, :key, :author, :title, :school, :year, :type, :address, :month, :note)")
    db.session.execute(sql, {"reftype":reftype, "username":username, "key":key, "author":author, "title":title, "school":school, "year":year, "type":type, "address":address, "month":month, "note":note})
    db.session.commit()
    return True

def get_references():
    sql = text("SELECT * FROM reference")
    result = db.session.execute(sql)
    references = result.fetchall()
    return references

def get_masterthesis():
    sql = text('''
        SELECT username, key, author, title, year, type, address, month, note, school 
        FROM reference 
        WHERE reftype LIKE '%masterthesis%' 
        ''')
    result = db.session.execute(sql)
    masterthesis = result.fetchall()
    return masterthesis

def send_article(username, author, title, journal, p_year, volume, number, pages, month, note):
    reftype = "article"

    check_reference_validity([username, author, title, journal, p_year, volume, number, pages, month, note],
                             ["username", "author", "title", "journal", "year", "volume", "number", "pages", "month", "note"])

    year = int(p_year)
    key = keygen(author,year)

    sql = text("INSERT INTO reference (reftype, username, key, author, title, journal, year, volume, number, pages, month, note) VALUES (:reftype, :username, :key, :author, :title, :journal, :year, :volume, :number, :pages, :month, :note)")
    db.session.execute(sql, {"reftype":reftype, "username":username, "key":key, "author":author, "title":title, "journal":journal, "year":year, "volume":volume, "number":number, "pages":pages, "month":month, "note":note})
    db.session.commit()
    return True

def get_article():
    sql = text('''
        SELECT username, key, author, title, journal, year, volume, number, pages, month, note 
        FROM reference 
        WHERE reftype LIKE '%article%' 
        ''')
    result = db.session.execute(sql)
    article = result.fetchall()
    return article

def send_phdthesis(username, author, title, school, p_year, type, address, month, note):
    reftype = "phdthesis"

    check_reference_validity([username, author, title, school, p_year, type, address, month, note],
                             ["username", "author", "title", "school", "year", "type", "address", "month", "note"])

    year = int(p_year)
    key = keygen(author,year)

    sql = text("INSERT INTO reference (reftype, username, key, author, title, school, year, type, address, month, note) VALUES (:reftype, :username, :key, :author, :title, :school, :year, :type, :address, :month, :note)")
    db.session.execute(sql, {"reftype":reftype, "username":username, "key":key, "author":author, "title":title, "school":school, "year":year, "type":type, "address":address, "month":month, "note":note})
    db.session.commit()
    return True

def get_phdthesis():
    sql = text('''
        SELECT username, key, author, title, year, type, address, month, note, school 
        FROM reference 
        WHERE reftype LIKE '%phdthesis%' 
        ''')
    result = db.session.execute(sql)
    phdthesis = result.fetchall()
    return phdthesis

def get_keys():
    sql = text("SELECT key FROM reference")
    result = db.session.execute(sql)
    masterthesis = result.fetchall()
    return masterthesis

def keygen(author, year):
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

    check_reference_validity([username, author, title, year, publisher, volume, series, address, edition, month, note],
                             ["username", "author", "title", "year", "publisher", "volume", "series", "address", "edition", "month", "note"])

    year = int(year)

    sql = text("UPDATE reference SET reftype = :reftype, username = :username, author = :author, title = :title, year = :year, publisher = :publisher, volume = :volume, series = :series, address = :address, edition = :edition, month = :month, note = :note WHERE key = :key")
    db.session.execute(sql, {"reftype": reftype, "username": username, "key": key, "author": author, "title": title, "year": year, "publisher": publisher, "volume": volume, "series": series, "address": address, "edition": edition, "month": month, "note": note})
    db.session.commit()
    return True

def edit_masterthesis(username, key, author, title, school, year, type, address, month, note):
    reftype = "masterthesis"

    check_reference_validity([username, author, title, school, year, type, address, month, note],
                             ["username", "author", "title", "school", "year", "type", "address", "month", "note"])

    year = int(year)

    sql = text("UPDATE reference SET reftype = :reftype, username = :username, author = :author, title = :title, school = :school, year = :year, type = :type, address = :address, month = :month, note = :note WHERE key = :key")
    db.session.execute(sql, {"reftype": reftype, "username": username, "key": key, "author": author, "title": title, "school": school, "year": year, "type": type, "address": address, "month": month, "note": note})
    db.session.commit()
    return True

def edit_article(username, key, author, title, journal, year, volume, number, pages, month, note):
    reftype = "article"

    check_reference_validity([username, author, title, journal, year, volume, number, pages, month, note],
                             ["username", "author", "title", "journal", "year", "volume", "number", "pages", "month", "note"])

    year = int(year)

    sql = text("UPDATE reference SET reftype = :reftype, username = :username, author = :author, title = :title, journal = :journal, year = :year, volume = :volume, number = :number, pages = :pages, month = :month, note = :note WHERE key = :key")
    db.session.execute(sql, {"reftype": reftype, "username": username, "key": key, "author": author, "title": title, "journal": journal, "year": year, "volume": volume, "number": number, "pages": pages, "month": month, "note": note})
    db.session.commit()
    return True

def edit_phdthesis(username, key, author, title, school, year, type, address, month, note):
    reftype = "phdthesis"

    check_reference_validity([username, author, title, school, year, type, address, month, note],
                             ["username", "author", "title", "school", "year", "type", "address", "month", "note"])

    year = int(year)

    sql = text("UPDATE reference SET reftype = :reftype, username = :username, author = :author, title = :title, school = :school, year = :year, type = :type, address = :address, month = :month, note = :note WHERE key = :key")
    db.session.execute(sql, {"reftype": reftype, "username": username, "key": key, "author": author, "title": title, "school": school, "year": year, "type": type, "address": address, "month": month, "note": note})
    db.session.commit()
    return True

def check_reference_validity(reference_values_list, reference_field_names):
    index_for_field_name = 0
    for value in reference_values_list:

        if reference_field_names[index_for_field_name] == "month":
            if len(value) > 3:
                raise InvalidInputError("Syötä kuukausi tyylillä 'jan', 'feb' jne.")

        if reference_field_names[index_for_field_name] == "year":
            for char in value:
                if char.isalpha():
                    raise InvalidInputError("Vuosi väärin!")
            year = int(value)
            if year < 0 or year > 3000:
                raise InvalidInputError("Vuosi väärin!")

        if len(value) > 100:
            raise InvalidInputError("Liian pitkä " + reference_field_names[index_for_field_name] + " syöte!")

        index_for_field_name += 1

def get_all_references_dict():
    refs_dict = {}
    refs_dict["books"] = get_books()
    refs_dict["masterthesis"] = get_masterthesis()
    refs_dict["articles"] = get_article()
    refs_dict["phdthesis"] = get_phdthesis()

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

def create_masterthesis_bibtex_format(masterthesis):
    masterthesis_ref_text = f'''@masterthesis{{{masterthesis[1]},
author = {{{masterthesis[2]}}},
title = {{{masterthesis[3]}}},
year = {{{masterthesis[4]}}},
type = {{{masterthesis[5]}}},
address = {{{masterthesis[6]}}},
month = {{{masterthesis[7]}}},
note = {{{masterthesis[8]}}},
school = {{{masterthesis[9]}}}          
}}
    '''
    return masterthesis_ref_text

def create_article_bibtex_format(article):
    masterthesis_ref_text = f'''@article{{{article[1]},
author = {{{article[2]}}},
title = {{{article[3]}}},
journal = {{{article[4]}}},
year = {{{article[5]}}},
volume = {{{article[6]}}},
number = {{{article[7]}}},
pages = {{{article[8]}}},
month = {{{article[9]}}},
note = {{{article[10]}}}         
}}
    '''
    return masterthesis_ref_text


def create_phdthesis_bibtex_format(phd):
    phdthesis_ref_text = f'''@phdthesis{{{phd[1]},
author = {{{phd[2]}}},
title = {{{phd[3]}}},
year = {{{phd[4]}}},
type = {{{phd[5]}}},
address = {{{phd[6]}}},
month = {{{phd[7]}}},
note = {{{phd[8]}}},
school = {{{phd[9]}}}          
}}
    '''
    return phdthesis_ref_text

def create_bibtex_text():
    bibtex_string = ""
    refs_dict = get_all_references_dict()
    for book in refs_dict["books"]:
        bibtex_string += create_book_bibtex_format(book)+"\n"

    for masterthesis in refs_dict["masterthesis"]:
        bibtex_string += create_masterthesis_bibtex_format(masterthesis)+"\n"

    for article in refs_dict["articles"]:
        bibtex_string += create_article_bibtex_format(article)+"\n"

    for phd in refs_dict["phdthesis"]:
        bibtex_string += create_phdthesis_bibtex_format(phd)+"\n"

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

def get_references_by_author():
    sql = text("SELECT * FROM reference ORDER BY author")
    result = db.session.execute(sql)
    references = result.fetchall()
    return references

def get_references_by_year():
    sql = text("SELECT * FROM reference ORDER BY year")
    result = db.session.execute(sql)
    references = result.fetchall()
    return references

def get_reference_search(query):
    sql = text("SELECT * FROM reference WHERE "
               "lower(reftype) LIKE lower(:query) OR "
               "lower(username) LIKE lower(:query) OR "
               "lower(key) LIKE lower(:query) OR "
               "lower(author) LIKE lower(:query) OR "
               "lower(title) LIKE lower(:query) OR "
               "lower(year) LIKE lower(:query) OR "
               "lower(publisher) LIKE lower(:query) OR "
               "lower(volume) LIKE lower(:query) OR "
               "lower(series) LIKE lower(:query) OR "
               "lower(address) LIKE lower(:query) OR "
               "lower(edition) LIKE lower(:query) OR "
               "lower(month) LIKE lower(:query) OR "
               "lower(note) LIKE lower(:query) OR "
               "lower(school) LIKE lower(:query) OR "
               "lower(type) LIKE lower(:query)"
               )
    
    result = db.session.execute(sql,{"query": f"%{query}%"})
    references = result.fetchall()
    return references
