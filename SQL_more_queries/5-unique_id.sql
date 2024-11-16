-- Use the provided database 
USE hbtn_test_db_3;

-- Create the 'unique_id' table if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1,          
    name VARCHAR(256),                  
    PRIMARY KEY (id)                   
);

-- Insert a new row into the 'unique_id' table 
INSERT INTO unique_id (id, name) 
VALUES (1, 'Sample Name');  

-- Insert another row with different data 
INSERT INTO unique_id (id, name) 
VALUES (2, 'Another Name');  

