from app import app
from flask import render_template, request, redirect
import methods


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/postbook")
def post_book():
    return render_template("post.html")
        
