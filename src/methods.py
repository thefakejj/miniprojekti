from flask import make_response

def post_book(username, key, author, title, year, publisher):
    sql = "INSERT INTO book "