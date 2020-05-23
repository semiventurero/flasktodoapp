from flask import Flask,render_template,redirect,url_for,request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Semi/Desktop/TodoApp/todo.db'#en sondaki todo.db yi ben yazıyorum yoksa olmuyor
db = SQLAlchemy(app)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add",methods = ["POST"])
def addTodo():
    title = request.form.get("title")
    newTodo = Todo(title = title,complete = False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)#ya 0 ya 1 değerini alacak

if __name__ == "__main__":
    db.create_all()#uygulamadan çalışmadan bir önceki aşamada yap
    app.run(debug=True)

