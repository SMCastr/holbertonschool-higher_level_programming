-- 12-no_genre.sql
-- Script to list all shows from the 'hbtn_0d_tvshows' database without a genre linked

-- Use the database 'hbtn_0d_tvshows'
USE hbtn_0d_tvshows;

-- Select shows without a genre linked from the 'tv_shows' table
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;