import mysql.connector

#replace with your database information
db = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd = "password",
    database="phri"
    )

cursor = db.cursor()

cursor.execute("""
DROP Table if EXISTS name_study;
DROP Table if EXISTS funds;
DROP Table if EXISTS names;
DROP Table if EXISTS studies;
                 
CREATE TABLE names (
    id INT PRIMARY KEY AUTO_INCREMENT,
    PI_name VARCHAR(255),
    last_name VARCHAR(255),
    first_name VARCHAR(255),
    organization VARCHAR(255)
);

CREATE TABLE studies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    study_name VARCHAR(255),
    study_category VARCHAR(255),
    study_status VARCHAR(255),
    study_type VARCHAR(255),
    start_year INT,
    end_year INT,
    sponsor_names VARCHAR(255),
    no_of_countries INT,
    no_of_sites INT,
    no_of_participants INT
);

CREATE TABLE name_study (
    id INT PRIMARY KEY AUTO_INCREMENT,
    study_id INT,
    PI_name VARCHAR(255),
    last_name VARCHAR(255),
    first_name VARCHAR(255)
);

CREATE TABLE funds (
    id INT PRIMARY KEY AUTO_INCREMENT,
    last_name VARCHAR(255),
    first_name VARCHAR(255),
    organization VARCHAR(255),
    program VARCHAR(255),
    total_funding_ammount INT,
    currency VARCHAR(255),
    other_organization VARCHAR(255),
    fund_start_date VARCHAR(255),
    fund_end_date VARCHAR(255)
);""")

