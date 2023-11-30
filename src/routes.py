from app import app
from flask import render_template, request, redirect, send_file
import methods



@app.route("/postbook")
def post_book():
    return render_template("postbook.html")
        
@app.route("/sendbook", methods=["POST"])
def send_book():
    username = request.form["username"]
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    publisher = request.form["publisher"]
    volume = request.form["volume"]
    series = request.form["series"]
    address = request.form["address"]
    edition = request.form["edition"]
    month = request.form["month"]
    note = request.form["note"]

    if len(username) > 100:
        return render_template("error.html",message="Liian pitkä username syöte!")
    if len(author) > 100:
        return render_template("error.html",message="Liian pitkä author syöte!")
    if len(title) > 100:
        return render_template("error.html",message="Liian pitkä title syöte!")
    if len(year) > 100:
        return render_template("error.html",message="Liian pitkä year syöte!")
    if len(publisher) > 100:
        return render_template("error.html",message="Liian pitkä publisher syöte!")
    if len(volume) > 100:
        return render_template("error.html",message="Liian pitkä volume syöte!")
    if len(series) > 100:
        return render_template("error.html",message="Liian pitkä series syöte!")
    if len(address) > 100:
        return render_template("error.html",message="Liian pitkä address syöte!")
    if len(month) > 100:
        return render_template("error.html",message="Liian pitkä month syöte!")
    if len(note) > 100:
        return render_template("error.html",message="Liian pitkä note syöte!")
    
    if not year.isnumeric():
        return render_template("error.html",message="Vuosi-kentän syöte ei ole luku!")
    
    if len(month) > 3:
        return render_template("error.html",message="Syötä kuukausi tyylillä 'jan', 'feb' jne.")

    if methods.send_book(username,author,title,year,publisher, volume, series, address, edition, month, note):
        return redirect("/")

@app.route("/")
def get_references():
    references = methods.get_references()
    return render_template("index.html", references=references)

@app.route("/postmaster")
def post_master():
    return render_template("postmaster.html")

@app.route("/sendmaster", methods=["POST"])
def send_master():
    username = request.form["username"]
    author = request.form["author"]
    title = request.form["title"]
    school = request.form["school"]
    year = request.form["year"]
    type = request.form["type"]
    address = request.form["address"]
    month = request.form["month"]
    note = request.form["note"]

    if len(username) > 100:
        return render_template("error.html",message="Liian pitkä username syöte!")
    if len(author) > 100:
        return render_template("error.html",message="Liian pitkä author syöte!")
    if len(title) > 100:
        return render_template("error.html",message="Liian pitkä title syöte!")
    if len(school) > 100:
        return render_template("error.html",message="Liian pitkä school syöte!")
    if len(year) > 100:
        return render_template("error.html",message="Liian pitkä year syöte!")
    if len(type) > 100:
        return render_template("error.html",message="Liian pitkä type syöte!")
    if len(address) > 100:
        return render_template("error.html",message="Liian pitkä address syöte!")
    if len(month) > 100:
        return render_template("error.html",message="Liian pitkä month syöte!")
    if len(note) > 100:
        return render_template("error.html",message="Liian pitkä note syöte!")
    
    if not year.isnumeric():
        return render_template("error.html",message="Vuosi-kentän syöte ei ole luku!")
    
    if len(month) > 3:
        return render_template("error.html",message="Syötä kuukausi tyylillä 'jan', 'feb' jne.")

    if methods.send_master(username, author, title, school, year, type, address, month, note):
        return redirect("/")

@app.route("/keylist", methods=["GET"])
def get_keys():
    keys = methods.get_keys()
    return render_template("keylist.html", keys=keys)

@app.route("/keyview/<key>")
def keyview(key):
    view = methods.keyview(key)
    return render_template("keyview.html", view=view)

@app.route("/confirmdelete/<key>", methods=["GET"])
def confirmdelete(key):
    view = methods.keyview(key)
    return render_template("confirmdelete.html", view=view)

@app.route("/deletereference/<key>", methods=["POST"])
def deletereference(key):
    if request.form.get("_method") == "DELETE":
        methods.delete_reference(key)
    return redirect("/")

@app.route("/editbook/<key>", methods=["GET","POST"])
def editbook(key):
    if request.method == "GET":
        view = methods.keyview(key)
        return render_template("postbook.html", view=view, edit=True)
    if request.method == "POST":
        username = request.form["username"]
        author = request.form["author"]
        title = request.form["title"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        volume = request.form["volume"]
        series = request.form["series"]
        address = request.form["address"]
        edition = request.form["edition"]
        month = request.form["month"]
        note = request.form["note"]

        if methods.edit_book(username,key,author,title,year,publisher, volume, series, address, edition, month, note):
            return redirect("/")
        
@app.route("/editmaster/<key>", methods=["GET","POST"])
def editmaster(key):
    if request.method == "GET":
        view = methods.keyview(key)
        return render_template("postmaster.html", view=view, edit=True)
    if request.method == "POST":
        username = request.form["username"]
        author = request.form["author"]
        title = request.form["title"]
        school = request.form["school"]
        year = request.form["year"]
        type = request.form["type"]
        address = request.form["address"]
        month = request.form["month"]
        note = request.form["note"]

        if methods.edit_master(username,key,author,title,school,year,type,address,month,note):
            return redirect("/")

@app.route('/getbibtex') # should maybe call something like "create file" first
def download_bibtex():
    methods.create_bibtex_file()
    return send_file(
        'outputs/references.bib',
        mimetype='text/bib',
        download_name='references.bib',
        as_attachment=True
    )