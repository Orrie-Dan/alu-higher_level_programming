-- Create the 'hbtn_0d_usa' database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Create the 'states' table if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,   
    name VARCHAR(256) NOT NULL           
);

