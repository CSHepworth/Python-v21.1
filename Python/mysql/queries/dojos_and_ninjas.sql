INSERT INTO dojos (name, created_at, updated_at)
VALUES 
	('Tokyo', CURRENT_TIMESTAMP(), NOW()),
    ('Iwo Jima', CURRENT_TIMESTAMP(), NOW()),
    ('Kyoto', CURRENT_TIMESTAMP(), NOW());

SET SQL_SAFE_UPDATES = 0;

DELETE FROM dojos;

INSERT INTO dojos (name, created_at, updated_at)
VALUES 
	('Santa Monica', CURRENT_TIMESTAMP(), NOW()),
    ('Sri Lanka', CURRENT_TIMESTAMP(), NOW()),
    ('San Diego', CURRENT_TIMESTAMP(), NOW());

INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
VALUES
	('Wang', 'Chung', 34, 4, CURRENT_TIMESTAMP(), NOW()),
    ('Chuck', 'Norris', 68, 4, CURRENT_TIMESTAMP(), NOW()),
    ('Brock', 'Lee', 27, 4, CURRENT_TIMESTAMP(), NOW()),
    ('Mace', 'Windu', 43, 5, CURRENT_TIMESTAMP(), NOW()),
    ('Dick', 'Nickson', 55, 5, CURRENT_TIMESTAMP(), NOW()),
    ('Arsenio', 'Hall', 41, 5, CURRENT_TIMESTAMP(), NOW()),
    ('Toby', 'Flenderson', 36, 6, CURRENT_TIMESTAMP(), NOW()),
    ('Dwide', 'Schrude', 47, 6, CURRENT_TIMESTAMP(), NOW()),
    ('B.M.', 'Fahrtz', 38, 6, CURRENT_TIMESTAMP(), NOW());

SELECT * FROM dojos_and_ninjas_schema.ninjas WHERE dojo_id = (SELECT max(dojo_id) FROM dojos_and_ninjas_schema.ninjas);

SELECT name FROM dojos_and_ninjas_schema.dojos WHERE id = (SELECT dojo_id FROM dojos_and_ninjas_schema.ninjas WHERE id = (SELECT max(id) FROM dojos_and_ninjas_schema.ninjas));