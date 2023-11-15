from app import app
from flask import render_template, request, redirect
from sqlalchemy.sql import text
import methods



@app.route("/postbook")
def post_book():
    return render_template("post.html")
        

@app.route("/index", methods=["GET"])
def view():
    return render_template("index.html")