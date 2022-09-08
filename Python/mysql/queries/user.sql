INSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES
    ('Cooper', 'Hepworth', 'cooperhepworth@hotmail.com', CURRENT_TIMESTAMP(), NOW()),
    ('Turd', 'Ferguson', 'tferg@hotmail.com', CURRENT_TIMESTAMP(), NOW()),
    ('Abe', 'Froman', 'ssgkingochicago@hotmail.com', CURRENT_TIMESTAMP(), NOW());

SELECT * FROM users;

SELECT first_name, email FROM users;

SELECT * FROM users WHERE id = 3;

UPDATE users SET last_name = 'Pancakes' WHERE id = 3;

DELETE FROM users WHERE id = 2;

SELECT * FROM users ORDER BY first_name ASC;

SELECT * FROM users ORDER BY first_name DESC;
