-- Displays 3 cities of high average
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDRE BY `avg_tmep` DESC
LIMIT 3;
