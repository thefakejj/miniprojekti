from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from db_connection import get_database_connection

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

def read_schema(path):
    with open(path, 'r') as file:
        commands = file.read().split(';')
        connection = get_database_connection()
        cursor = connection.cursor()
        for command in commands:
            cursor.execute(command)
        connection.commit()
        cursor.close()
        connection.close()

read_schema('src/schema.sql')

if __name__ == "__main__":
    app.run(debug=True)

import routes