from flask import Flask
import pymysql

app = Flask(__name__)

def get_message_from_db():
    connection = pymysql.connect(
        host='mariadb',
        user='user',
        password='password',
        database='test_db'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT content_message FROM messages LIMIT 1;")
    message = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return message

@app.route('/')
def index():
    message = get_message_from_db()
    return f"Message from DB: {message}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
