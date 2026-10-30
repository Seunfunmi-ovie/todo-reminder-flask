
from flask import Flask, render_template, request, redirect
import sqlite3
from flask import Blueprint
blueprint = Blueprint("todo_router", __name__)


@blueprint.route('/to-do', methods=["POST","GET"])
def home():
    if request.method == "POST":
        new_task = request.form["title"].strip()
        if new_task:
         con = sqlite3.connect("task.db")
         con.execute('INSERT INTO tasks(task) VALUES(?)',(new_task,))
         con.commit()
         con.close()
        return redirect("/to-do")
    con = sqlite3.connect("task.db")
    rows = con.execute('SELECT id, task FROM tasks').fetchall()
    con.close()
    return render_template("index.html", tasks = rows)



@blueprint.route('/delete/<int:task_id>',methods=["POST"])
def delete_task(task_id):
    con = sqlite3.connect("task.db")
    con.execute('DELETE FROM tasks WHERE id = ?',(task_id,))
    con.commit()
    con.close()
    return redirect("/to-do")