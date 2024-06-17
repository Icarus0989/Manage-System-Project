from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index3')
def index3():
    return render_template('index3.html')
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'changeThisToYourPassword'
app.config['MYSQL_DATABASE_DB'] = 'phri'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)


    

@app.route('/submit', methods=['POST'])
def submit():
    selected_item = request.form.get('selected_item')
    # Connect to MySQL
    conn = mysql.connect()
    cursor = conn.cursor()

    # Example query
    cursor.execute("SELECT name_id, study_id FROM names WHERE study_id = selected_item")
    data = cursor.fetchall()

    # Close connection
    cursor.close()
    conn.close()

    return jsonify(data)    


if __name__ == '__main__':
    app.run(debug=True)
