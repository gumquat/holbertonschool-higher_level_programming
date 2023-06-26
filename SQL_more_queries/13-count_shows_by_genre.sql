-- list all genres from hbtn_0d_tvshows and display 
-- the number of shows linked to each
SELECT DISTINCT genre, COUNT(*) AS number_of_shows FROM hbtn_0d_tvshows
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre;
ORDER BY number_of_shows DESC;