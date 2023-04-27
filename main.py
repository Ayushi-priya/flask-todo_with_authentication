from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from project.models import Todo
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method=='POST':
        title= request.form['title']
        desc= request.form['desc']
        todo=Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo=Todo.query.all()
    return render_template('home.html', name=current_user.name, allTodo=allTodo)

@main.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title= request.form['title']
        desc= request.form['desc']
        todo=Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/home")
    todo=Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', name=current_user.name, todo=todo)

@main.route('/delete/<int:sno>')
def delete(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/home")