from flask import Flask
import os
from datetime import datetime
import mysql.connector # type: ignore

app = Flask(__name__)

@app.route('/')
def hello_world():
    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_DATABASE')
    )

    cursor = db.cursor()
    cursor.execute('SELECT DATABASE()')
    data = cursor.fetchone()
    return f'Hello, Docker! Database: {data[0]}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



