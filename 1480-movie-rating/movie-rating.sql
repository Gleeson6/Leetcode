# Write your MySQL query statement below
(SELECT u.name AS results FROM MovieRating Mr
JOIN Users u ON u.user_id=Mr.user_id
GROUP BY u.name
ORDER BY COUNT(*) DESC, u.name ASC
LIMIT 1)

UNION ALL

(SELECT m.title AS results
FROM MovieRating Mr 
JOIN Movies m ON m.movie_id=Mr.movie_id
WHERE DATE_FORMAT(Mr.created_at, '%Y-%m') = '2020-02'
GROUP BY m.title
ORDER BY AVG(Mr.rating) DESC, m.title ASC
LIMIT 1)