-- lists the ratings for each genre in the database hbtn_0d_tvshows_rate
-- lists every record in a database that is connected to a different table's row
SELECT name, SUM(tv_show_ratings.rate) 'rating'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY name
ORDER BY rating DESC;
