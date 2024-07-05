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
);

/*queries*/

/*display the organizations*/
/*when clicking an organzation*/
cursor.execute(   /*to get names of PIs that are part of the organization*/
    SELECT PI_name
    FROM names
    WHERE organization = "selected_organzation"
    )
data = cursor.fetchall()

/*display corresponding PI_names*/
/*when clicking a PI_names*/

cursor.execute(   /*to get study names that the PIs have worked on*/

    SELECT study_name
    FROM studies
    WHERE id IN (
        SELECT study_id
        FROM name_study
        WHERE name_id IN (
            SELECT id
            FROM names
            WHERE PI_name = "selected_PI_name"
        )
    )
)
data = cursor.fetchall()

/*display the study_names*/

/*after clicking a study, display the info below,
and an option to click "display funding info"*/

cursor.execute(   /*to get study info */
    SELECT * 
    FROM studies
    WHERE study_name = "selected_study_name"
)


/*if clicked "display funding info"*/
cursor.execute(   /*to get study funding info */
    SELECT * 
    FROM funds
    WHERE study_id IN (
        SELECT id 
        FROM studies
        WHERE study_name =  "selected_study_name"
    )
)

/*adding options to sort by revenue or expense, and by revenue/expense category.*/

/*SELECT * FROM studies WHERE revenue_or_expense = "x"
SELECT * FROM studies WHERE fund_category = "x"*/

