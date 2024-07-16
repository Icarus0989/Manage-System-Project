from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def create_connection():
    return mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd = "password",
    database="phri"
    )

@app.route('/api/query', methods=['POST'])

def select_org():
    try:
        data = request.json
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""SELECT PI_name, 
                       FROM names, 
                       WHERE organization = %s""", (data))
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred"}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def select_PI_name():
    try:
        data = request.json
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT study_name
            FROM studies
            WHERE id IN (
                SELECT study_id
                FROM name_study
                WHERE name_id IN (
                    SELECT id
                    FROM names
                    WHERE PI_name = %s))""", (data))
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred"}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def select_study_name():
    try:
        data = request.json
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT * 
            FROM studies
            WHERE study_name = %s""", (data))
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred"}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def select_display_funding():
    try:
        data = request.json
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT * 
            FROM funds
            WHERE study_id IN (
                SELECT id 
                FROM studies
                WHERE study_name = %S""", (data))
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred"}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


#adding options to sort by revenue or expense, and by revenue/expense category.

#SELECT * FROM studies WHERE revenue_or_expense = "x"
#SELECT * FROM studies WHERE fund_category = "x"

