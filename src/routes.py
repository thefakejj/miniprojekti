from app import app
from flask import render_template, request, redirect
from sqlalchemy.sql import text
import methods


@app.route("/index")
def index():
    return render_template("index.html")

<<<<<<< HEAD
@app.route("/postbook")
def post_book():
    return render_template("post.html")
        
=======
@app.route("/index", methods=["GET"])
def view():
    return render_template("index.html")
    
>>>>>>> 38d531cdc335ee41e56c0e7d181ad01ae16cf634
