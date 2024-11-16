-- List all shows and their genres (including NULL for shows with no genre)
SELECT tv_shows.title, tv_show_genres.genre_id AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title , tv_show_genres.genre_id ;

