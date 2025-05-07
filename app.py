from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)  

conn = psycopg2.connect(
    dbname='postgres', 
    user='postgres',
    password='postgres',
    host='db-jamshiddin.clyucs4e44b4.ap-northeast-2.rds.amazonaws.com',
    port='5432'
)
cursor = conn.cursor()

@app.route('/')
def home():
    return "Welcome to Jamshiddin's Flask App"

@app.route('/socialmedia', methods=['GET'])
def get_socialmedia():
    cursor.execute("SELECT * FROM tbl_jamshiddin_socialmedia")
    rows = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    result = [dict(zip(colnames, row)) for row in rows]
    return jsonify(result)

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
