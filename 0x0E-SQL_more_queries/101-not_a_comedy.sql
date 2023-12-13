-- show title
SELECT DISTINCT `title`
 FROM `tv_shows` AS A
	LEFT JOIN `tv_show_genres` as B
	ON B.`show_id` = A.`id`
	LEFT JOIN `tv_genres` AS C
	ON C.`id` = B.`genre_id`
	WHERE t.`title` NOT IN
		(SELECT `title`
			FROM `tv_shows` AS A
				INNER JOIN `tv_show_genres` AS B
				ON B.`show_id` = A.`id`
				INNER JOIN `tv_genres` AS C
				ON C.`id` = B.`genre_id`
				WHERE C.`genre_id`
				WHERE C.`name` = "Comedy")
ORDER BY `title`;
