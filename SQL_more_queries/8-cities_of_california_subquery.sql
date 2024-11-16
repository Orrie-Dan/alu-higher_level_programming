-- Use the provided database 
USE hbtn_0d_usa;

-- Retrieve all cities in California, sorted by city id in ascending order
SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California') 
ORDER BY id ASC;

