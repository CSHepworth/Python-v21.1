INSERT INTO books.users (first_name, last_name, created_at, updated_at)
VALUES
    ('Jane', 'Amsden', CURRENT_TIMESTAMP(), NOW()),
    ('Emily', 'Dixon', CURRENT_TIMESTAMP(), NOW()),
    ('Theodore', 'Dostoevsky', CURRENT_TIMESTAMP(), NOW()),
    ('William', 'Shapiro', CURRENT_TIMESTAMP(), NOW()),
    ('Lao', 'Xiu', CURRENT_TIMESTAMP(), NOW());

INSERT INTO books.books (title, created_at, updated_at)
VALUES
    ('C Sharp', CURRENT_TIMESTAMP(), NOW()),
    ('Java', CURRENT_TIMESTAMP(), NOW()),
    ('Python', CURRENT_TIMESTAMP(), NOW()),
    ('PHP', CURRENT_TIMESTAMP(), NOW()),
    ('Ruby', CURRENT_TIMESTAMP(), NOW());

UPDATE books.books SET title = 'C#' WHERE id = 1;

UPDATE books.users SET first_name = 'Bill' WHERE id = 4;

INSERT INTO books.favorites (users_id, books_id)
VALUES
	(1, 1),
    (1, 2);
	(2, 1),
    (2, 2),
    (2, 3),
    (3, 1),
	(3, 2),
    (3, 3),
    (3, 4),
    (4, 1),
    (4, 2),
    (4, 3),
    (4, 4),
    (4, 5);


SELECT first_name, last_name FROM users
JOIN favorites ON users.id = favorites.users_id
WHERE favorites.books_id = 3;

DELETE FROM favorites WHERE users_id = 2 AND books_id = 3;

INSERT INTO books.favorites (users_id, books_id)
VALUES (5, 2);

SELECT title FROM books.books
JOIN books.favorites on favorites.users_id = users.id
WHERE favorites.users_id = 3;

SELECT first_name, last_name FROM books.users
JOIN books.favorites ON favorites.users_id = users.id
WHERE favorites.books_id = 5;