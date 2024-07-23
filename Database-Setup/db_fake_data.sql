/*names*/
INSERT INTO names VALUES (1, 'Aminah Nicholson', 'PHRI')
INSERT INTO names VALUES (2, 'Caiden Villa', 'PHRI')
INSERT INTO names VALUES (3, 'Judy Burns', 'PHRI')
INSERT INTO names VALUES (4, 'Kimberly Hoffman', 'PHRI')
INSERT INTO names VALUES (5, 'Felicity Poole', 'WHRI')
INSERT INTO names VALUES (6, 'Madeline Walton', 'WHRI')
INSERT INTO names VALUES (7, 'Owain Atkins', 'McMaster')
INSERT INTO names VALUES (8, 'Lawrence Sanchez', 'McMaster')
INSERT INTO names VALUES (9, 'Brayden Winter', 'HHS')
INSERT INTO names VALUES (10, 'Zakir Cohen', 'HHS')

/*studies*/
INSERT INTO studies VALUES (1, '416858-CS4', '1', 'Renal', 'Publication', 'Interventional - Drug', 2015, 2016, 'IONIS Pharmaceuticals', 1,8,49)
INSERT INTO studies VALUES (2, 'A Clinical Platform for Discovering Novel Regulators of Energy Expenditure', '1', 'Childhood Risk Factors', 'New', 'Interventional - Procedure', 2023, 2025, 'PHRI', 0, 1, 180)
INSERT INTO studies VALUES (3, 'ACCORD', '3', 'Diabetes', 'Publication', 'Interventional - Drug', 2001, 2009, 'None', 2, 77, 10251)
INSERT INTO studies VALUES (4, '416858-CS4', '3', 'Diabetes', 'Publication', 'Interventional - Drug', 2011, 2015, 'NHLBI', 2, 72, 8601)
INSERT INTO studies VALUES (5, '416858-CS4', '1', 'Renal', 'Recruitment', 'Interventional - Drug', 2017, 2025, 'PHRI', 12, 157, 3628)

/*name_study*/

/*funds*/
INSERT INTO funds (study_id, revenue_or_expense, fund_category, revenue_expense, amount, year, month, quarter, scenario) VALUES
(1, 'Revenue', 'Grants', 'Research Grant', 50000, 2023, 1, 'Q1', 'Baseline'),
(2, 'Expense', 'Salaries', 'Staff Salary', 30000, 2023, 2, 'Q1', 'Baseline'),
(3, 'Revenue', 'Donations', 'Private Donation', 20000, 2023, 3, 'Q1', 'Optimistic'),
(4, 'Expense', 'Equipment', 'Lab Equipment', 15000, 2023, 4, 'Q2', 'Baseline'),
(5, 'Revenue', 'Tuition', 'Student Tuition', 100000, 2023, 5, 'Q2', 'Pessimistic'),
(6, 'Expense', 'Maintenance', 'Building Maintenance', 10000, 2023, 6, 'Q2', 'Baseline'),
(7, 'Revenue', 'Sponsorship', 'Corporate Sponsorship', 25000, 2023, 7, 'Q3', 'Optimistic'),
(8, 'Expense', 'Utilities', 'Electricity', 5000, 2023, 8, 'Q3', 'Baseline'),
(9, 'Revenue', 'Consulting', 'Consulting Fees', 30000, 2023, 9, 'Q3', 'Pessimistic'),
(10, 'Expense', 'Supplies', 'Office Supplies', 2000, 2023, 10, 'Q4', 'Baseline');

