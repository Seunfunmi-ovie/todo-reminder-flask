from flask import Flask
from flask import render_template,redirect,request
import sqlite3

from routers.todo_router import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint)

def task_db():
    con = sqlite3.connect("task.db")
    con.execute('CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,task  TEXT NOT NULL)')
    con.commit()
    con.close()










if __name__ == "__main__":
    task_db()
    app.run(debug=True)