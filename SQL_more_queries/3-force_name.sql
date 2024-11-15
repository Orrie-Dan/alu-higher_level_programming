-- Use the provided database
USE hbtn_test_db_3;

-- Create the table if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

