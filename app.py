import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database="service_db", user="postgres", password="Aat8912000!", host="localhost", port="5432")
cursor = conn.cursor()

@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    if username == '':
        return render_template('login.html', error_msg1='enter username')
    password = request.form.get('password')
    if password == '':
        return render_template('login.html', error_msg2='enter password')
    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())
    if len(records) == 0:
        return render_template('login.html', error_msg='user is not found')
    return render_template('account.html', full_name=records[0][1], username=records[0][2], password=records[0][3])

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')