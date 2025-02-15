from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('anime_backlog.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS backlog (id INTEGER PRIMARY KEY, anime_name TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('anime_backlog.db')
    c = conn.cursor()
    c.execute('SELECT * FROM backlog')
    backlog = c.fetchall()
    conn.close()
    return render_template('index.html', backlog=backlog)

@app.route('/add', methods=['POST'])
def add_anime():
    anime_name = request.form['anime_name']
    if anime_name:
        conn = sqlite3.connect('anime_backlog.db')
        c = conn.cursor()
        c.execute('INSERT INTO backlog (anime_name) VALUES (?)', (anime_name,))
        conn.commit()
        conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
