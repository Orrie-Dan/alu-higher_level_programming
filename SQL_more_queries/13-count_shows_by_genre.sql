-- List all genres and the number of shows linked to each genre
-- Results are ordered by the number of shows linked, in descending order
SELECT g.name AS genre, COUNT(s.id) AS number_of_shows
FROM genres g
LEFT JOIN tv_show_genres tg ON g.id = tg.genre_id
LEFT JOIN tv_shows s ON tg.tv_show_id = s.id
GROUP BY g.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;

