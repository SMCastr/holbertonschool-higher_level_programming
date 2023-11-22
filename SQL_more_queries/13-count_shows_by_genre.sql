-- 13-count_shows_by_genre.sql
-- Script to list all genres from 'hbtn_0d_tvshows' and display the number of shows linked to each genre

-- Use the database 'hbtn_0d_tvshows'
USE hbtn_0d_tvshows;

-- Select genres and the count of shows linked to each genre
SELECT tv_genres.name AS genre, 
COUNT(tv_show_genres.genres_id) AS number_of_shows
FROM tv_show_genres
INNER JOIN tv_genres ON tv_show_genres.genres_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;