![CI_workflow](https://github.com/thefakejj/miniprojekti/workflows/CI/badge.svg)
# miniprojekti
This is **Nelosen oppilaat** group's repository for Ohjelmistotuotanto course

[**Project backlog**](https://docs.google.com/spreadsheets/d/1rMa7GUguUNTL2GxiPYZAxfzeGfuaFnNYY5xCVqZGXGg/edit?usp=sharing)

## Definition of Done
* All tasks required for implementing the user story have been finished
* Automated test implemented for the feature

# Installation
* [Install python 3.8+](https://www.python.org/about/gettingstarted/)
* [Install poetry 1.7.0+](https://python-poetry.org/docs/#installation)
```
git clone git@github.com:thefakejj/miniprojekti.git
```
```
poetry install
```
```
cd src
```
```
sqlite3 site.db
```
```
CREATE TABLE book (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, key TEXT NOT NULL, author TEXT NOT NULL, title TEXT NOT NULL, year INTEGER NOT NULL, publisher TEXT NOT NULL);
```
```
cd  ..
```
```
poetry run flask run
```

# User Guide
After starting the application open the following url with a browser: http://127.0.0.1:5000

* _Lisää kirjaviite_ link allows adding book references into database.
  * Input book reference details into corresponding form fields and click _Lisää_
* Existing book references are displayed on the bottom of the page in Bibtex format






