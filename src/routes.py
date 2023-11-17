from app import app
from flask import render_template, request, redirect
import methods



@app.route("/postbook")
def post_book():
    return render_template("post.html")
        
@app.route("/sendbook", methods=["POST"])
def send_book():
    username = request.form["username"]
    key = request.form["key"]
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    publisher = request.form["publisher"]

    if methods.send_book(username,key,author,title,year,publisher):
        return redirect("/")

@app.route("/")
def get_books():
    books = methods.get_books()
    return render_template("index.html", books=books)