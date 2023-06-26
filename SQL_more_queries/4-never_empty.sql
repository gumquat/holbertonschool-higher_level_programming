-- creates a table called id not null with id default 1 and a name variable
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);