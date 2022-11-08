-- Joins


-- write a query in SQL to display the first name, last name,
-- department number, and department name for each employee

SELECT first_name, last_name, department.department_id, department.department_name
FROM employees
JOIN department ON employees.department_id = department.department_id


-- write a query in SQL to display the first and last name,
-- department, city, and state province for each employee

SELECT first_name, last_name, department.department_id, locations.city, locations.state_province
FROM employees
JOIN department ON employees.department_id = department.department_id
JOIN locations ON department.location_id = locations.location_id


-- write a query in SQL to display the first name, last name,
-- department number, and department name, for all employees
-- for departments 80 or 40

SELECT first_name, last_name, department.department_id, department.department_name
FROM employees
JOIN department ON employees.department_id = department.department_id
AND department.department_id IN (80, 40)


-- write a query in SQL to display all departments including
-- those where does not have any employee

SELECT first_name, last_name, department.department_id, department.department_name
FROM department
LEFT JOIN employees ON department.department_id = employees.department_id


-- write a query in SQL to display the first name of all
-- employees including the first name of their manager

SELECT e1.first_name AS employee_name, e2.first_name AS manager_name
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id


-- write a query in SQL to display the job title, full name
-- (first and last name ) of the employee, and the difference
-- between the maximum salary for the job and the salary of the employee

SELECT jobs.job_title, first_name || ' ' || last_name AS full_name, jobs.max_salary - employees.salary AS sal_dif
FROM employees
JOIN jobs ON employees.job_id = jobs.job_id


-- write a query in SQL to display the job title and the average salary of employees

SELECT first_name, last_name, job_title, (min_salary+max_salary)/2 AS avg_salary
FROM employees
JOIN jobs USING(job_id)


-- write a query in SQL to display the full name (first and last name),
-- and salary of those employees who work in any department located in London

SELECT first_name || ' ' || last_name AS full_name, salary
FROM employees
JOIN department USING(department_id)
JOIN locations USING(location_id)
WHERE locations.city = "London"

-- write a query in SQL to display the department name
-- and the number of employees in each department

SELECT department_name, COUNT(employees.employee_id) AS num_of_emp
FROM department
JOIN employees USING(department_id)
GROUP BY department.department_name