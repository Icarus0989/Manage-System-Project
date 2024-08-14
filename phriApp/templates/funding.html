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

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/index2', methods=['POST'])
def index2():
    global Organization
    Organization = request.form.get('selectedItem')
    return render_template('index2.html', Organization = Organization)

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/contribution')
def contribution():
    return render_template('contribution.html')

@app.route('/funding')
def funding():
    
    return render_template('funding.html')

@app.route('/investigator')
def investigator():
    return render_template('investigator.html')

@app.route('/mentor')
def mentor():
    return render_template('mentor.html')

@app.route('/publication')
def publication():
    return render_template('publication.html')

@app.route('/study')
def study():
    return render_template('study.html')

@app.route('/studyCategory')
def studyCategory():
    return render_template('studyCategory.html')

@app.route('/supervision')
def supervision():
    return render_template('supervision.html')

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

@app.route('/loginRedirect', methods=['POST'])
def loginRedirect():
    return redirect(url_for('login'))
@app.route('/submitSignup', methods=['POST'])
def submitSignup():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    password_hash = generate_password_hash(password)    
    password_confirmation = request.form.get('password_confirmation')
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        flash('Invalid email address', 'error')
        return redirect(url_for('signup'))
    
        # Additional validations can be added here
    if password != password_confirmation:
        flash('Passwords do not match', 'error')
        return redirect(url_for('signup'))
    cursor = mysql.connection.cursor()
    
        # Check if email already exists
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        flash('Email already exists', 'error')
        return redirect(url_for('signup'))
    
        # Insert new user
    cursor.execute("INSERT INTO users (first_name, last_name, email, password_hash) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, password_hash))
    mysql.connection.commit()
    cursor.close()
    
    
        # Process the form data (e.g., save to database)
        
    
    flash('Signup successful', 'success')
    return redirect(url_for('login'))
    
@app.route('/loginSubmit', methods=['POST'])
def login_submit():
    global lastName
    global firstName
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
            cursor.execute("SELECT last_name FROM users WHERE email = %s", [email])
            user = cursor.fetchone()
            lastName = user[0]
            cursor.execute("SELECT first_name FROM users WHERE email = %s", [email])
            user = cursor.fetchone()
            firstName = user[0]
            return redirect(url_for('home'))
        else:
            flash('Invalid password', 'error')
    else:
        flash('Email does not exist', 'error')

    return redirect(url_for('login'))   

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

@app.route('/fundingSubmit')
def fundingSubmit():
    cursor = mysql.connection.cursor()
    query = """
    SELECT 
        last_name AS 'Last Name', 
        organization AS 'Funding Organization',
        program AS 'Program Name', 
        total_funding_ammount AS 'Total Funding', 
        currency AS 'Currency',
        researcherDesignation AS 'Researcher Designation',
        first_name AS 'First Name',
        other_organization AS 'Other Funding Organizations',
        Competitive AS 'Competitive',
        fund_start_date AS 'Funding Start Date',
        fund_end_date AS 'Funding End Date',
        associate AS 'Associate',
        department AS 'Department',
        title AS 'Title',
        fundingRole AS 'Funding Role'
    FROM funds;
    """
    
    """
    WHERE last_name = %s AND first_name = %s;
    """
    
    """
    cursor.execute(query, (lastName, firstName))
    """
    cursor.execute(query)
    data = cursor.fetchall()
    formatted_data = []
    for row in data:
        formatted_row = {
            'Last Name': row[0],
            'Funding Organization': row[1],
            'Program Name': row[2],
            'Total Funding': str(row[3]) if isinstance(row[3], decimal.Decimal) else row[3],
            'Currency':row[4],
            'Researcher Designation': row[5],
            'First Name': row[6],
            'Other Funding Organizations': row[7],
            'Competitive': row[8],
            'Funding Start Date': str(row[9]) if isinstance(row[9], decimal.Decimal) else row[9],
            'Funding End Date': str(row[10]) if isinstance(row[10], decimal.Decimal) else row[10],
            'Associate': row[11],
            'Department': row[12],
            'Title': row[13],
            'Funding Role': row[14]
        }
        formatted_data.append(formatted_row)    

    
    cursor.close()
    
    return render_template('funding.html', data=formatted_data)

@app.route('/get_funds_filters', methods=['GET'])
def get_funds_filters():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT DISTINCT last_name, first_name, organization, program, currency, other_organization FROM funds")
    names = cursor.fetchall()
    cursor.close()

    # Transform the result into separate lists for last names and first names
    lastname_list = [row[0] for row in names]
    firstname_list = [row[1] for row in names]
    organization_list = [row[2] for row in names]
    program_list = [row[3] for row in names]
    currency_list = [row[4] for row in names]
    other_organization_list = [row[5] for row in names]
    return jsonify({'lastnames': lastname_list, 'firstnames': firstname_list,'organizations':organization_list, 'programs':program_list, 'currencies':currency_list, 'other_organizations': other_organization_list})

if __name__ == '__main__':
    app.run(debug=True)
