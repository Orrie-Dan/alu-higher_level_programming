-- Use the provided database 
USE hbtn_test_db_3;

-- Create the 'unique_id' table if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1,          
    name VARCHAR(256),                  
    PRIMARY KEY (id)                   
);

