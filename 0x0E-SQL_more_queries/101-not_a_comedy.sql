-- show title
SELECT DISTINCT `title`
 FROM `tv_shows` AS t
	LEFT JOIN `tv_show_genres` as B
	ON B.`show_id` = t.`id`
	LEFT JOIN `tv_genres` AS C
	ON C.`id` = B.`genre_id`
	WHERE t.`title` NOT IN
		(SELECT `title`
		   FROM `tv_shows` AS t
			INNER JOIN `tv_show_genres` AS B
			ON B.`show_id` = t.`id`
			INNER JOIN `tv_genres` AS C
			ON C.`id` = B.`genre_id`
			WHERE C.`genre_id`
			WHERE C.`name` = "Comedy")
ORDER BY `title`;
