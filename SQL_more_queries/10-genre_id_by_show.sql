-- lists all shows contained in database 
-- hbtn_0d_tvshows that have >=1 one genre linked
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id FROM tv_shows 
  JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
  JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;