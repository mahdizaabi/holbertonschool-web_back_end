-- SQL script that creates a table users
-- script can be executed on any database

CREATE TABLE IF NOT EXISTS users(
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);