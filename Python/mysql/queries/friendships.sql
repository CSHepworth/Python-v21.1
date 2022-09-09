INSERT INTO friendships_schema.users (first_name, last_name, created_at, updated_at)
VALUES
	('Abe', 'Froman', CURRENT_TIMESTAMP(), NOW()),
    ('Ray', 'Mann', CURRENT_TIMESTAMP(), NOW()),
    ('Dolan', 'Trombone', CURRENT_TIMESTAMP(), NOW()),
    ('Arthur', 'Fleck', CURRENT_TIMESTAMP(), NOW()),
	('Cosmo', 'Kramer', CURRENT_TIMESTAMP(), NOW()),
    ('Prescott', 'Bush', CURRENT_TIMESTAMP(), NOW());

INSERT INTO friendships_schema.friendships (user_id, friend_id, created_at, updated_at)
VALUES
    ('1', '2', CURRENT_TIMESTAMP(), NOW()),
    ('1', '4', CURRENT_TIMESTAMP(), NOW()),
    ('1', '6', CURRENT_TIMESTAMP(), NOW()),
    ('2', '1', CURRENT_TIMESTAMP(), NOW()),
    ('2', '3', CURRENT_TIMESTAMP(), NOW()),
    ('2', '5', CURRENT_TIMESTAMP(), NOW()),
    ('3', '2', CURRENT_TIMESTAMP(), NOW()),
    ('3', '5', CURRENT_TIMESTAMP(), NOW()),
    ('5', '1', CURRENT_TIMESTAMP(), NOW()),
    ('5', '6', CURRENT_TIMESTAMP(), NOW()),
    ('6', '2', CURRENT_TIMESTAMP(), NOW()),
    ('6', '3', CURRENT_TIMESTAMP(), NOW());

SELECT users.first_name, users.last_name, users2.first_name AS friend_first_name, users2.last_name AS friend_last_name FROM friendships_schema.users
JOIN friendships_schema.friendships ON users.id = friendships.user_id
LEFT JOIN friendships_schema.users as users2 ON users2.id = friendships.friend_id;

SELECT users2.first_name, users2.last_name FROM friendships_schema.users
JOIN friendships_schema.friendships ON users.id = friendships.user_id
LEFT JOIN friendships_schema.users as users2 ON users2.id = friendships_schema.friend_id
WHERE users.id = 1;