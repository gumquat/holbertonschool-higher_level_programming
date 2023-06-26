-- list all shows contained in hbtn_0d_tvshows without 
-- a genre link
SELECT genre, COUNT(*) AS number_of_shows FROM hbtn_0d_tvshows
GROUP BY genre HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;