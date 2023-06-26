-- list all genres from hbtn_0d_tvshows and display 
-- the number of shows linked to each
SELECT genre, COUNT(*) AS number_of_shows FROM hbtn_0d_tvshows
GROUP BY genre;
ORDER BY number_of_shows DESC;