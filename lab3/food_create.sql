DROP TABLE IF EXISTS food_type CASCADE;
CREATE TABLE food_type (
    id_food_type    SERIAL PRIMARY KEY,
    type            VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS food CASCADE;
CREATE TABLE food (
    id_food         SERIAL PRIMARY KEY,
    id_food_type    INTEGER REFERENCES food_type,
    name            VARCHAR(100) NOT NULL,
    description     TEXT
);

DROP TABLE IF EXISTS product CASCADE;
CREATE TABLE product (
    id_product      SERIAL PRIMARY KEY,
    name            VARCHAR(100) NOT NULL,
    hypoallergenic  BOOLEAN DEFAULT TRUE,
    calorie_100g    INTEGER NOT NULL
);

DROP TABLE IF EXISTS author CASCADE;
CREATE TABLE author (
    id_author   SERIAL PRIMARY KEY,
    first_name  VARCHAR(100) NOT NULL,
    last_name   VARCHAR(100) NOT NULL,
    email       VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS recipe CASCADE;
CREATE TABLE recipe (
    id_recipe   SERIAL PRIMARY KEY,
    id_author   INTEGER REFERENCES author,
    id_food     INTEGER REFERENCES food,
    name        VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    photo_key   VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS recipe_has_product CASCADE;
CREATE TABLE recipe_has_product (
    id_recipe   INTEGER REFERENCES recipe,
    id_product  INTEGER REFERENCES product,
    amount      INTEGER NOT NULL,
    amount_type VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS comment CASCADE;
CREATE TABLE comment (
    id_comment  BIGSERIAL PRIMARY KEY,
    id_recipe   INTEGER REFERENCES recipe,
    content     TEXT,
    rating      NUMERIC(2, 1) NOT NULL
);