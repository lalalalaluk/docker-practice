USE company;

CREATE TABLE IF NOT EXISTS employees (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    salary INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO employees (name, department, salary) VALUES
    ('Alice Chen', 'Engineering', 72000),
    ('Ben Lin', 'Support', 48000),
    ('Cindy Wang', 'Sales', 56000);

SELECT * FROM employees;

SELECT name, department, salary
FROM employees
WHERE salary > 50000;

UPDATE employees
SET department = 'Customer Success'
WHERE name = 'Ben Lin';

SELECT * FROM employees WHERE name = 'Ben Lin';

DELETE FROM employees
WHERE name = 'Cindy Wang';

SELECT * FROM employees;
