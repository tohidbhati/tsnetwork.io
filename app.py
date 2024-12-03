from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import os
import mysql.connector

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# MySQL Database Connection
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='student_network'
    )
    return connection

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and user['password'] == password:
            session['user_id'] = user['id']
            return redirect(url_for('home'))

        cursor.close()
        connection.close()

    return render_template('login.html')

@app.route('/send-request', methods=['POST'])
def send_request():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'})

    data = request.get_json()
    message = data.get('message')

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO requests (user_id, request_message) VALUES (%s, %s)", (session['user_id'], message))
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
