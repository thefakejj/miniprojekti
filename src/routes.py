from app import app
from flask import render_template, request, redirect
import methods


@app.route("/index")
def post_reference():
    if request.method == "POST":
        return render_template("post.html")
    if request.methid == "GET":
        

