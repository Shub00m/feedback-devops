import time
import mysql.connector
from mysql.connector import Error

for attempt in range(1, 11):
    try:
        print(f"⏳ Waiting for MySQL... Attempt {attempt}/10")
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="rootpassword",
            database="feedback_db"
        )
        if conn.is_connected():
            print("✅ MySQL is ready!")
            conn.close()
            break
    except Error as e:
        time.sleep(5)
else:
    print("❌ Could not connect to MySQL after 10 attempts.")
    exit(1)
