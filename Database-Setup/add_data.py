import mysql.connector
import pandas as pd 

#replace with your database information
db = mysql.connector.connect( 
    host ="localhost",
    user ="root",
    passwd = "password",
    database="phri"
    )

#define functions to add data to database
def add_names(conn, PI_info):
    sql = '''INSERT INTO names (PI_name,last_name,first_name,organization)
            VALUES(%s, %s, %s, %s)'''
    cur = db.cursor()
    cur.execute(sql, PI_info)
    db.commit()
    return cur.lastrowid

def add_study(conn, study_info):
    sql = '''INSERT INTO studies(study_name,study_category,study_status,study_type,start_year,end_year,sponsor_names,no_of_countries,no_of_sites,no_of_participants)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cur = db.cursor()
    cur.execute(sql, study_info)
    db.commit()
    return cur.lastrowid

def add_name_study(conn, name_study_info):
    mysql = '''INSERT INTO name_study(study_id,PI_name,last_name,first_name)
             VALUES(%s,%s,%s,%s)'''
    cur = db.cursor()
    cur.execute(mysql, name_study_info)
    db.commit()
    return cur.lastrowid

def add_funding(conn, funding_info):
    sql = '''INSERT INTO funds (last_name,first_name,organization,program,total_funding_ammount,currency,other_organization,fund_start_date,fund_end_date)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cur = db.cursor()
    cur.execute(sql, funding_info)
    db.commit()
    return cur.lastrowid

#add to names table
publications_dataframe = pd.read_csv("Database-Setup/input_files/contribution.csv")
prev_PI = ()
for row in publications_dataframe.itertuples(index=None):
    values = list(row)
    last_name = values[0]
    first_name = values[1]
    PI_name = values[3]
    organization = values[6]

    PI_info = (PI_name,last_name,first_name,organization)
    if prev_PI != PI_info:
        add_names(db, PI_info)
    prev_PI = PI_info

#add to studies table
publications_dataframe = pd.read_csv("Database-Setup/input_files/study.csv")
for row in publications_dataframe.fillna(0).itertuples(index=None):
    values = list(row)
    study_name = values[0]
    study_category = values[3]
    study_status = values[5]
    study_type = values[6]
    start_year = values[7]
    end_year = values[8]
    sponsor_names = values[9]
    no_of_countries = values[11]
    no_of_sites = values[12]
    no_of_participants = values[13]

    study_info = (study_name,study_category,study_status,study_type,start_year,end_year,sponsor_names,no_of_countries,no_of_sites,no_of_participants)
    add_study(db, study_info)

#add to name_study table
publications_dataframe = pd.read_csv("Database-Setup/input_files/contribution.csv")
for row in publications_dataframe.itertuples(index=None):
    values = list(row)
    last_name = values[0]
    first_name = values[1]
    PI_name = values[3]
    study_id = values[7]
    
    name_study_info = (study_id,PI_name,last_name,first_name) 
    add_name_study(db,name_study_info)

#add to funding table
publications_dataframe = pd.read_csv("Database-Setup/input_files/funding.csv")
for row in publications_dataframe.fillna(0).itertuples(index=None):
    values = list(row)
    last_name = values[0]
    first_name = values[6]
    organization = values[1]
    program = values[2]
    total_funding_ammount = values[3]
    currency = values[4]
    other_organization = values[7]
    fund_start_date = values[9]
    fund_end_date = values[10]

    funding_info = (last_name,first_name,organization,program,total_funding_ammount,currency,other_organization,fund_start_date,fund_end_date)
    add_funding(db,funding_info)