-- linked to show Dexter
SELECT DISTINCT `name`
 FROM `tv_genres` AS a
	INNER JOIN `tv_show_genres` AS b
	ON a.`id` = b.`genre_id`
	INNER JOIN `tv_shows` AS c
	ON b.`show_id` = c.`id`
	WHERE a.`name` NOT IN
	(
		SELECT `name`
		FROM `tv_genres` AS b
			INNER JOIN `tv_show_genres` AS b
			ON a.`id` = b.`genre_id`
			INNER JOIN `tv_shows` AS c
			ON b.`show_id` = c.`id`
			WHERE c.`title` = "Dexter"
	)
ORDER BY a.`name`;
