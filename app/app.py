from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
import time

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'rootpassword',
    'database': 'feedback_db'
}

# ✅ Wait until MySQL is ready
for i in range(10):
    try:
        test_conn = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password']
        )
        if test_conn.is_connected():
            print("✅ MySQL is ready!")
            test_conn.close()
            break
    except Error as e:
        print(f"⏳ Waiting for MySQL... Attempt {i+1}/10")
        time.sleep(5)
else:
    print("❌ Could not connect to MySQL after 10 attempts.")
    exit(1)


# ✅ Initialize database and table
def init_db():
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password']
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS feedback_db")
    conn.database = db_config['database']
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedbacks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            message TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedbacks (name, message) VALUES (%s, %s)", (name, message))
        conn.commit()
        cursor.close()
        conn.close()

        return render_template('index.html', success=True)

    return render_template('index.html')


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
