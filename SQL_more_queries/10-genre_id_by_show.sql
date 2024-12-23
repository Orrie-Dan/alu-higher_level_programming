-- List all shows that have at least one genre linked, sorted by title and genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

