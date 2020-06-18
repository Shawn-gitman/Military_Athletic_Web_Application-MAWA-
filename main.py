from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
app.secret_key ="hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.permanent_session_lifetime = timedelta(minutes=5)

app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True)
    password = db.Column(db.String(80))
    month = db.Column(db.String(80))
    year = db.Column(db.String(80))
    level = db.Column(db.String(80))
    def __init__(self, username, password, month, year, level):
        self.username = username
        self.password = password
        self.month = month
        self.year = year
        self.level = level

class Bulletin(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(80))
    writer = db.Column(db.String(80))
    def __init__(self, title, content, writer):
        self.title = title
        self.content = content
        self.writer = writer


@app.route("/")
def home():
    session['logged_in'] = False
    return redirect(url_for('main'))

@app.route("/view")
def view():
    return render_template("view.html", values=User.query.all())

@app.route("/main", methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        new_user = User(username = request.form['username'], password = request.form['password'], month = request.form['month'], year = request.form['year'], level = request.form['level'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('index.html')
    if session['logged_in'] == False:
        return render_template("index.html")
    elif session['logged_in'] == True:
        name = session['name']
        session.permanent = True
        return render_template("index.html", usr = name)
    else:
        return render_template("index.html")
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login2.html')
	else:
		name = request.form['username']
		passw = request.form['password']
		try:
			data = User.query.filter_by(username = name, password=passw).first()
			if data is not None:
				session['logged_in'] = True
				session['name'] = name
				session.permanent = True
				return render_template('index.html', usr = name)
			else:
				return redirect(url_for('login'))
		except:
			return "Dont Login"

@app.route('/bulletin')
def bulletin():
    if session['logged_in'] == False:
        return render_template("bulletin.html")
    elif session['logged_in'] == True:
        name = session['name']
        session.permanent = True
        return render_template("bulletin.html", usr = name, values=Bulletin.query.all())
    else:
        return render_template('bulletin.html', values=Bulletin.query.all())

@app.route('/bulletin/bulletin_see/<id>/', methods=['GET', 'POST'])
def bulletin_see(id):
    data = Bulletin.query.get(id)
    d_title = data.title
    d_content = data.content
    return render_template('bulletin_see.html', values=Bulletin.query.all(), d_title=d_title, id = id, d_content=d_content)

@app.route('/bulletin/create', methods = ['GET', 'POST'])
def create():
    if session['logged_in'] == False:
        return render_template("create.html")
    elif session['logged_in'] == True:
        if request.method == 'POST':
            writer = session['name']
            new_post = Bulletin(title = request.form['title'], content = request.form['content'], writer=writer)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('bulletin'))
    return render_template('create.html')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template("index.html")

@app.route('/bulletin/update/<id>/', methods = ['GET', 'POST'])
def update(id):
    login_account = session['name']
    writer_id = Bulletin.query.get(id)
    writer_account = writer_id.writer
    note = Bulletin.query.get(id)
    if login_account != writer_account:
        return redirect(url_for('bulletin'))
    else:
        if request.method == 'POST':
            note.title = request.form['title']
            note.content = request.form['content']
            db.session.commit()
            return redirect(url_for('bulletin'))
    return render_template("update.html", item = note, note=note)
    
    

@app.route("/bulletin/delete/<id>/", methods = ['GET', 'POST'])
def delete(id):
    login_account = session['name']
    writer_id = Bulletin.query.get(id)
    writer_account = writer_id.writer
    if login_account != writer_account:
        return redirect(url_for('bulletin'))
    else:
        data = Bulletin.query.get(id)
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for('bulletin'))

@app.route("/lottery")
def lottery():
    if session['logged_in'] == False:
        return render_template("lottery.html")
    elif session['logged_in'] == True:
        name = session['name']
        session.permanent = True
        return render_template("lottery.html", usr = name)

@app.route("/towleague")
def towleague():
    if session['logged_in'] == False:
        return render_template("towleague.html")
    elif session['logged_in'] == True:
        name = session['name']
        session.permanent = True
        return render_template("towleague.html", usr = name)


if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)
    #app.run(host='0.0.0.0')