from app import app
from flask import render_template, request, redirect
import methods



@app.route("/postbook")
def post_book():
    return render_template("post.html")
        

@app.route("/index", methods=["GET"])
def view():
    return render_template("index.html")