-- 10-genre_id_by_show.sql
-- Script to list all shows from the 'hbtn_0d_tvshows' database that have at least one genre linked

-- Use the database 'hbtn_0d_tvshows'
USE hbtn_0d_tvshows;
-- Select shows and their corresponding genre IDs from the 'tv_shows' and 'tv_show_genres' tables
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
