-- This script lists all records from second_table where name is not NULL or empty
-- The results are ordered by score in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

