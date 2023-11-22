from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import sqlite3

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
print(getenv("DATABASE_URL"))
db = SQLAlchemy(app)

def read_schema(path):
    with open(path, 'r') as file:
        commands = file.read().split(';')
        connection = sqlite3.connect('src/instance/site.db')
        cursor = connection.cursor()
        for command in commands:
            print(command)
            cursor.execute(command)
        connection.commit()
        cursor.close()
        connection.close()

read_schema('src/schema.sql')

if __name__ == "__main__":
    app.run(debug=True)

import routes