-- List all genres and the number of shows linked to each genre
SELECT tv_genres.name, COUNT(tv_show_genres.show_id)
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY COUNT(tv_show_genres.show_id) DESC;

