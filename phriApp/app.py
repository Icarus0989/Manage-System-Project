from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_mysqldb import MySQL
import decimal, re
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def signup():
    return render_template('signup.html')

@app.route('/index')
def index():
    
    return render_template('index.html')
@app.route('/index2', methods=['POST'])
def index2():
    global Organization
    Organization = request.form.get('selectedItem')
    
    return render_template('index2.html', Organization = Organization)

@app.route('/login',methods=['POST'])
def login():
    return render_template('login.html')


@app.route('/index3')
def index3():
    return render_template('index3.html')

@app.route('/get_pis', methods=['GET'])
def get_pis():
    cursor = mysql.connection.cursor()
    query = "SELECT PI_name FROM names WHERE organization = %s"
    cursor.execute(query, (Organization,))
    pi_names = [row[0] for row in cursor.fetchall()]
    print(pi_names)
    cursor.close()
    return jsonify(pi_names)


app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '584521george'
app.config['MYSQL_DB'] = 'phri'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)


@app.route('/submitSignup', methods=['POST'])
def submitSignup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    password_hash = generate_password_hash(password)    
    password_confirmation = request.form.get('password_confirmation')
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        flash('Invalid email address', 'error')
        return redirect(url_for('index'))
    
        # Additional validations can be added here
    if password != password_confirmation:
        flash('Passwords do not match', 'error')
        return redirect(url_for('index'))
    cursor = mysql.connection.cursor()
    
        # Check if email already exists
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        flash('Email already exists', 'error')
        return redirect(url_for('index'))
    
        # Insert new user
    cursor.execute("INSERT INTO users (users_name, email, password_hash) VALUES (%s, %s, %s)", (name, email, password_hash))
    mysql.connection.commit()
    cursor.close()
    
    
        # Process the form data (e.g., save to database)
        
    
    flash('Signup successful', 'success')
    return redirect(url_for('login'))
    
@app.route('/loginSubmit', methods=['POST'])
def login_submit():
    email = request.form.get('email')
    password = request.form.get('password')

    cursor = mysql.connection.cursor()

    # Check if email exists
    cursor.execute("SELECT password_hash FROM users WHERE email = %s", [email])
    user = cursor.fetchone()

    if user:
        # Verify password
        password_hash = user[0]
        if check_password_hash(password_hash, password):

            flash('Login successful', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid password', 'error')
    else:
        flash('Email does not exist', 'error')

    return redirect(url_for('index'))   

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
