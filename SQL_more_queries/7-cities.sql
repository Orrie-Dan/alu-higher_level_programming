-- Create the 'hbtn_0d_usa' database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the 'hbtn_0d_usa' database
USE hbtn_0d_usa;

-- Create the 'cities' table if it does not exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT PRIMARY KEY,      
    state_id INT NOT NULL,                  
    name VARCHAR(256) NOT NULL,             
    FOREIGN KEY (state_id) REFERENCES states(id)  
);

