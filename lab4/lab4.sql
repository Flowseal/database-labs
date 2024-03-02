-- 3.1a
INSERT INTO client VALUES (DEFAULT, 'Ivan', 'Petrov', NULL, '79240454592');

-- 3.1b
INSERT INTO barber(first_name, last_name, middle_name) VALUES ('Marat', 'Gikov', 'Ivanovich');

-- 3.1c
INSERT INTO barber(first_name, last_name, middle_name) SELECT first_name, last_name, middle_name FROM client;


-- 3.2a
DELETE FROM client;

-- 3.2b
DELETE FROM barber WHERE id_barber = 1;


-- 3.3a
UPDATE barber SET last_name = 'Petrov';

-- 3.3b
UPDATE barber SET first_name = 'Ivan' WHERE id_barber = 2;

-- 3.3c
UPDATE barber SET first_name = 'Andrey', last_name = 'Reznov' WHERE id_barber = 2;


-- 3.4a
SELECT first_name FROM barber;

-- 3.4b
SELECT * FROM barber;

-- 3.4c
SELECT * FROM barber WHERE id_barber = 2;


-- 3.5a
SELECT first_name FROM barber ORDER BY first_name ASC limit 10;

-- 3.5b
SELECT first_name FROM barber ORDER BY first_name DESC;

-- 3.5c
SELECT first_name FROM barber ORDER BY first_name DESC, last_name ASC limit 10;

-- 3.5d
SELECT first_name FROM barber ORDER BY 1 DESC


-- 3.6a
SELECT * FROM "order" WHERE start_time > '2023-01-01';

-- 3.6b
SELECT * FROM "order" WHERE start_time > '2024-01-01' AND start_time < '2024-02-01';

-- 3.6c
SELECT DATE_PART('year', start_time::timestamp) FROM "order";


-- 3.7a
SELECT COUNT(*) FROM barber;

-- 3.7b
SELECT COUNT(*) FROM (SELECT DISTINCT first_name, last_name, middle_name FROM barber) AS temp;

-- 3.7c
SELECT DISTINCT first_name FROM barber;

-- 3.7d
