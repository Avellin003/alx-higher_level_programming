-- 102_rating_shows.sql
SELECT `title`, SUM (`rate`) AS `rating`
FROM `tv_shows` AS a
	INNER JOIN `tv_show_ratings` AS b
	ON a.`id` = b.`show_id`
GROUP BY `title`
ORDER BY `rating` DESC;
