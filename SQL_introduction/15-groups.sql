-- list the number of records with the same score
SELECT score, COUNT(score) As number FROM second_table GROUP BY score ORDER BY number DESC;
