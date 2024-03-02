DROP TABLE IF EXISTS address CASCADE;
CREATE TABLE address (
    id_address  SERIAL PRIMARY KEY,
    country     VARCHAR(100) NOT NULL,
    city        VARCHAR(100) NOT NULL,
    street      VARCHAR(300) NOT NULL,
    building    VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS barbershop CASCADE;
CREATE TABLE barbershop (
    id_barbershop   SERIAL PRIMARY KEY,
    id_address      INTEGER references address,
    name            VARCHAR(200) NOT NULL,
    rating          NUMERIC(2, 1)
);

DROP TABLE IF EXISTS barber CASCADE;
CREATE TABLE barber (
    id_barber       SERIAL PRIMARY KEY,
    id_barbershop   INTEGER REFERENCES barbershop,
    first_name      VARCHAR(50) NOT NULL,
    last_name       VARCHAR(50) NOT NULL,
    middle_name     VARCHAR(50)
);

DROP TABLE IF EXISTS service CASCADE;
CREATE TABLE service (
    id_service  SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    price       NUMERIC(12, 2) NOT NULL,
    photo_key   VARCHAR(50)
);

DROP TABLE IF EXISTS client CASCADE;
CREATE TABLE client (
    id_client   SERIAL PRIMARY KEY,
    first_name  VARCHAR(50) NOT NULL,
    last_name   VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    phone       VARCHAR(20) NOT NULL
);

DROP TABLE IF EXISTS "order" CASCADE;
CREATE TABLE "order" (
    id_order    SERIAL PRIMARY KEY,
    id_client   INTEGER REFERENCES client,
    id_barber   INTEGER REFERENCES barber,
    price       NUMERIC(12, 2) NOT NULL,
    finished    BOOLEAN DEFAULT FALSE,
    start_time  TIMESTAMP NOT NULL
);

DROP TABLE IF EXISTS order_has_service CASCADE;
CREATE TABLE order_has_service (
    id_order    INTEGER REFERENCES "order",
    id_service  INTEGER REFERENCES service
);