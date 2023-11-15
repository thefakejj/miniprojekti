from flask import make_response

def post_book(username, key, author, title, year, publisher):
    sql = "INSERT INTO book (username, key, author, title, year, publisher) VALUES (:username, :key, :author, :title, :year, :publisher)"
    db.session.execute(sql, {"username":username, "key":key, "author":author, "title":title, "year":year, "publisher":publisher})
    db.session.commit()
    return True

def get_book(username, key, author, title, year, publisher):
    sql = "SELECT username, key, author, title, year, publisher FROM book"
    db.session.execute(sql, {"username":username, "key":key, "author":author, "title":title, "year":year, "publisher":publisher})
    db.session.commit()
    return True

