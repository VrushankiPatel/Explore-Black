from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session  # For session management
import os


app = Flask(__name__, template_folder=".")


@app.route('/')
def landingpage():
    return render_template("landing.html")


@app.route('/home')
def homepage():
    return render_template("home.html")


@app.route('/achieve')
def achieve():
    return render_template("Achievements.html")


@app.route('/movies')
def movies():
    return render_template("movies.html")


@app.route('/books')
def books():
    return render_template("books.html")


@app.route('/events')
def events():
    return render_template("events.html")


@app.route('/blogs')
def blogs():
    return render_template("blogs.html")


@app.route('/chat')
def chat():
    return render_template("chat.html")


app.secret_key = os.urandom(24)

# Configuring Flask session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

users = {}  # A simple "database" to store user credentials


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password  # Storing the user
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('events'))
        return 'Invalid username or password'
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run(debug=True)
