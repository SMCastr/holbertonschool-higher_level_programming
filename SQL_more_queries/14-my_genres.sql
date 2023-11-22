-- 14-my_genres.sql
-- Script to list all genres of the show Dexter from the 'hbtn_0d_tvshows' database

-- Use the database 'hbtn_0d_tvshows'
USE hbtn_0d_tvshows;

-- Select genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;