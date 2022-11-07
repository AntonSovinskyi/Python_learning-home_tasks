-- Select queries
-- Use the sample SQLite database hr.db


-- write a query to display the names (first_name, last_name)
-- using alias name "First Name", "Last Name" from the table of employees
import sqlite3 as sq


with sq.connect("hr.db") as con:
    cur = con.cursor()

    cur.execute("SELECT first_name AS First_Name, last_name AS Last_Name FROM employees")

-- write a query to get the unique department ID from the employee table
SELECT * FROM employees WHERE department_id = 80

-- write a query to get all employee details from the employee table ordered by first name, descending
SELECT * FROM employees ORDER BY first_name DESC

-- write a query to get the names (first_name, last_name), salary,
-- PF of all the employees (PF is calculated as 12% of salary)
SELECT first_name, last_name, salary, salary*.12 PF FROM employees

-- write a query to get the maximum and minimum salary from the employees table
SELECT MIN(salary), MAX(salary) FROM employees

-- write a query to get a monthly salary (round 2 decimal places) of each and every employee
SELECT first_name, last_name, round(salary/12,2) FROM employees
