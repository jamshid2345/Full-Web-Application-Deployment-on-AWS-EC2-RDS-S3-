from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Connect to your PostgreSQL RDS DB (Jamshiddin)
conn = psycopg2.connect(
    host='db-jamshiddin.clyucs4e44b4.ap-northeast-2.rds.amazonaws.com',
    database='postgres',
    user='postgres',
    password='postgres1'  # ← replace with your actual password
)

@app.route('/socialmedia', methods=['GET'])
def get_socialmedia():
    cur = conn.cursor()
    cur.execute("""
        SELECT platform, owner, primary_usage, country,
               daily_time_spent_min, verified_account, date_joined
        FROM socialmedia_data
    """)
    rows = cur.fetchall()
    data = [
        {
     'platform': r[0],
            'owner': r[1],
            'primary_usage': r[2],
            'country': r[3],
            'daily_time_spent_min': r[4],
            'verified_account': r[5],
            'date_joined': r[6].isoformat() if r[6] else None
        }
        for r in rows
    ]
    cur.close()
    return jsonify(data)

@app.route('/add', methods=['POST'])
def add_entry():
    data = request.json
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO socialmedia_data (
            platform, owner, primary_usage, country,
            daily_time_spent_min, verified_account, date_joined
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        data['platform'],
        data['owner'],
        data['primary_usage'],
        data['country'],
        data['daily_time_spent_min'],
        data['verified_account'],
        data['date_joined']
    ))
    conn.commit()
    cur.close()
    return jsonify({'message': 'Added successfully'})

@app.route('/delete', methods=['POST'])
def delete_entry():
    data = request.json
    cur = conn.cursor()
    cur.execute("DELETE FROM socialmedia_data WHERE owner = %s", (data['owner'],))
    conn.commit()
    cur.close()
    return jsonify({'message': 'Deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
