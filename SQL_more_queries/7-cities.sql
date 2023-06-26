-- creates a database named hbtn_0d_usa and a table
-- called cities with id, state_id, and name (varchar 256) not null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);