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

    try:
        methods.send_book(username,author,title,year,publisher, volume, series, address, edition, month, note)
        return redirect("/")
    except methods.InvalidInputError as e:
        return render_template(
            "postbook.html", 
            error=str(e), 
            username=username, 
            author=author, 
            title=title, 
            year=year, 
            publisher=publisher, 
            volume=volume, 
            series=series, 
            address=address, 
            edition=edition, 
            month=month, 
            note=note
        )

@app.route("/")
def get_references():
    filter = request.args.get("filter", "author")
    query = request.args.get("query","")
    sort_by = request.args.get("sort_by", "author")

    if query:
        references = methods.get_reference_search(query)
    else:
        if sort_by == "author":
            references = methods.get_references_by_author()
        elif sort_by == "year":
            references = methods.get_references_by_year()
        else:
            references = methods.get_references()

    return render_template("index.html", references=references, sort_by=sort_by, filter=filter)

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

    try:
        methods.send_master(username, author, title, school, year, type, address, month, note)
        return redirect("/")
    except methods.InvalidInputError as e:
        return render_template(
            "postmaster.html",
            error=str(e),
            username=username,
            author=author,
            title=title,
            school=school,
            year=year,
            type=type,
            address=address,
            month=month,
            note=note
        )

        

@app.route("/postphdthesis")
def post_phdthesis():
    return render_template("postphdthesis.html")

@app.route("/sendphdthesis", methods=["POST"])
def send_phdthesis():
    username = request.form["username"]
    author = request.form["author"]
    title = request.form["title"]
    school = request.form["school"]
    year = request.form["year"]
    type = request.form["type"]
    address = request.form["address"]
    month = request.form["month"]
    note = request.form["note"]

    try:
        methods.send_phdthesis(username, author, title, school, year, type, address, month, note)
        return redirect("/")
    except methods.InvalidInputError as e:
        return render_template(
            "postphdthesis.html",
            error=str(e),
            username=username,
            author=author,
            title=title,
            school=school,
            year=year,
            type=type,
            address=address,
            month=month,
            note=note
        )


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
    view = methods.keyview(key)
    if request.method == "GET":
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
        
        try:
            if methods.edit_book(username,key,author,title,year,publisher, volume, series, address, edition, month, note):
                return redirect("/")
        except methods.InvalidInputError as e:
            return render_template("postbook.html", view=view, edit=True, error=str(e))
        
@app.route("/editmaster/<key>", methods=["GET","POST"])
def editmaster(key):
    view = methods.keyview(key)
    if request.method == "GET":
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

        try:
            if methods.edit_master(username,key,author,title,school,year,type,address,month,note):
                return redirect("/")
        except methods.InvalidInputError as e:
            return render_template("postmaster.html",view=view, edit=True, error=str(e))

@app.route("/editphdthesis/<key>", methods=["GET","POST"])
def editphdthesis(key):
    view = methods.keyview(key)
    if request.method == "GET":
        return render_template("postphdthesis.html", view=view, edit=True)
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

        try:
            if methods.edit_phdthesis(username,key,author,title,school,year,type,address,month,note):
                return redirect("/")
        except methods.InvalidInputError as e:
            return render_template("postphdthesis.html", view=view, edit=True, error=str(e))

@app.route('/getbibtex') # should maybe call something like "create file" first
def download_bibtex():
    methods.create_bibtex_file()
    return send_file(
        'outputs/references.bib',
        mimetype='text/bib',
        download_name='references.bib',
        as_attachment=True
    )

@app.route("/postarticle")
def post_article():
    return render_template("postarticle.html")

@app.route("/sendarticle", methods=["POST"])
def send_article():
    username = request.form["username"]
    author = request.form["author"]
    title = request.form["title"]
    journal = request.form["journal"]
    year = request.form["year"]
    volume = request.form["volume"]
    number = request.form["number"]
    pages = request.form["pages"]
    month = request.form["month"]
    note = request.form["note"]

    try:
        methods.send_article(username, author, title, journal, year, volume, number, pages, month, note)
        return redirect("/")
    except methods.InvalidInputError as e:
        return render_template(
            "postarticle.html",
            error=str(e),
            username=username,
            author=author,
            title=title,
            journal=journal,
            year=year,
            volume=volume,
            number=number,
            pages=pages,
            month=month,
            note=note
        )

    
@app.route("/editarticle/<key>", methods=["GET","POST"])
def editarticle(key):
    view = methods.keyview(key)
    if request.method == "GET":
        return render_template("postarticle.html", view=view, edit=True)
    if request.method == "POST":
        username = request.form["username"]
        author = request.form["author"]
        title = request.form["title"]
        journal = request.form["journal"]
        year = request.form["year"]
        volume = request.form["volume"]
        number = request.form["number"]
        pages = request.form["pages"]
        month = request.form["month"]
        note = request.form["note"]

        try:
            if methods.edit_article(username, key, author, title, journal, year, volume, number, pages, month, note):
                return redirect("/")
        except methods.InvalidInputError as e:
            return render_template("postarticle.html", view=view, edit=True, error=str(e))


@app.route("/error")
def error():
    return render_template("error.html")