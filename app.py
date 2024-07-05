from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_mysqldb import MySQL
import decimal
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index3')
def index3():
    return render_template('index3.html')

@app.route('/level1')
def level1():
    return render_template('level1.html')

@app.route('/level2E')
def level2E():
    return render_template('level2E.html')

@app.route('/level2R')
def level2R():
    return render_template('level2R.html')

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '584521george'
app.config['MYSQL_DB'] = 'phri'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)


    

@app.route('/submit', methods=['POST'])
def submit():
    cursor = mysql.connection.cursor()
    '''
    cursor.execute('SELECT * FROM names')
    result = cursor.fetchall()
    cursor.close()
    selected_item = request.form.get('selectedItem')
    print(f'Selected item: {selected_item}')
    return redirect(url_for('index2'))
    '''
    query = """
    SELECT 
        organization_type AS 'Organization Type', 
        education AS 'Education', 
        amount AS 'Amount', 
        year AS 'Year', 
        month AS 'Month', 
        quarter AS 'Quarter', 
        scenario AS 'Scenario' 
    FROM demoTable;
    """
    
    cursor.execute(query)
    data = cursor.fetchall()
    formatted_data = []
    for row in data:
        formatted_row = {
            'Organization Type': row[0],
            'Education': row[1],
            'Amount': str(row[2]) if isinstance(row[2], decimal.Decimal) else row[2],
            'Year': row[3],
            'Month': row[4],
            'Quarter': row[5],
            'Scenario': row[6]
        }
        formatted_data.append(formatted_row)

    
    cursor.close()
    
    return render_template('tableG.html', data=formatted_data)


if __name__ == '__main__':
    app.run(debug=True)
