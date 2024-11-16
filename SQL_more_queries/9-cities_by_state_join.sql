--  script that lists all cities contained in the database
USE hbtn_0d_usa;
SELECT cities.id, cities.name,
    (SELECT name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;

