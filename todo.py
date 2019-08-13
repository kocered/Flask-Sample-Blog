from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key= "ybblog"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/kocer/Desktop/ToDoAPP/todo.db'
db = SQLAlchemy(app)


#Database Oluşturuyoruz.
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)


#index sayfasını yükleyelim

@app.route("/")
def index():
    todo_data = Todo.query.all()
    
    return render_template("index.html",todo_data=todo_data)

#todo ekleme
@app.route("/add",methods=["POST"])
def addtodo():
    title = request.form.get("title")
    data = Todo(title=title, complete=False ) 

    
    
    db.session.add(data)
    db.session.commit()
    flash('New entry was successfully posted')
    
    return redirect(url_for("index"))



if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)