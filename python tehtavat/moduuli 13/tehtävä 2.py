from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# Function to query the database
def get_airport_info(icao):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='saeidt',
        database='',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            sql = "SELECT ICAO, Name, Location FROM airports WHERE ICAO = %s"
            cursor.execute(sql, (icao,))
            result = cursor.fetchone()
            return result
    finally:
        connection.close()

# API endpoint to get airport information
@app.route('/airport/<icao>', methods=['GET'])
def airport_info(icao):
    airport = get_airport_info(icao)
    if airport:
        return jsonify(airport)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
