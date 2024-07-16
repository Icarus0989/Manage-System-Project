import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd = "Ayjz3811!",
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
    organization VARCHAR(255)
);

CREATE TABLE studies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    study_name VARCHAR(255),
    study_category_id INT,
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
    name_id INT,
    study_id INT,
    FOREIGN KEY (name_id) REFERENCES names(id),
    FOREIGN KEY (study_id) REFERENCES studies(id)
);

CREATE TABLE funds (
    id INT PRIMARY KEY AUTO_INCREMENT,
    study_id INT,
    revenue_or_expense VARCHAR(255),
    fund_category VARCHAR(255),
    revenue_expense VARCHAR(255),
    amount INT,
    year INT,
    month INT, 
    quarter VARCHAR(2),
    scenario VARCHAR(255),
    FOREIGN KEY (study_id) REFERENCES studies(id)
);""")