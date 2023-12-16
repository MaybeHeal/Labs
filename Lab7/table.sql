CREATE TABLE IF NOT EXISTS 'employee'(
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'firstname' TEXT,
    'secondname' TEXT,
    'age' INT,
    'department_id' INT,
    FOREIGN KEY('department_id') REFERENCES 'department'('id')
);

CREATE TABLE IF NOT EXISTS 'edition'(
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'title' TEXT,
    'circulation' INT,
    'page_count' INT
);

CREATE TABLE IF NOT EXISTS 'department'(
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'department_name' TEXT,
    'employee_number' INT,
    'direction' TEXT
)