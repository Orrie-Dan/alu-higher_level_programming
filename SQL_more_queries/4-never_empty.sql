-- Use the provided database 
USE hbtn_test_db_3;

-- Create the table if it does not already exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

