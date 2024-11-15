-- This script lists the records (score, name) from second_table where score >= 10
-- The records are ordered by score in descending order (top first)
SELECT score, name 
FROM second_table 
WHERE score >= 10
ORDER BY score DESC;

