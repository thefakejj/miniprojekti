from app import app
from flask import render_template, request, redirect
from sqlalchemy.sql import text
import methods


@app.route("/index")
def post_reference():
    if request.method == "POST":
        return render_template("post.html")
    if request.methid == "GET":
        

@app.route("/index", methods=["GET"])
def view():
    return render_template("index.html")
    
