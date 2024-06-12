CREATE TABLE names (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    PI_name VARCHAR(255),
    organization VARCHAR(255)
);

CREATE TABLE studies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    study_name VARCHAR(255)
);

CREATE TABLE name_study (
    id INT PRIMARY KEY AUTOINCREMENT,
    name_id INT REFERENCES names(id),
    study_id INT REFERENCES studies(id),
);

CREATE TABLE funds (
    id INT PRIMARY KEY AUTOINCREMENT,
    study_id INT REFERENCES name_study(id),
    revenue_or_expense VARCHAR(255),
    fund_category VARCHAR(255),
    revenue_expense VARCHAR(255),
    amount INT,
    year INT,
    month INT, 
    quarter VARCHAR(2),
    scenario VARCHAR(255)
);

SELECT PI_name FROM names WHERE organization = "x";
SELECT study_name FROM studies WHERE study_name = "x";

SELECT ANY FROM studies WHERE revenue_or_expense = "x";
SELECT ANY FROM studies WHERE fund_category = "x";

SELECT funds.revenue_or_expense, funds.fund_category, funds.revenue_expense, funds.amount, funds.year, funds.month, funds.quarter
FROM name_study
INNER JOIN funds ON name_study.id = funds.id;