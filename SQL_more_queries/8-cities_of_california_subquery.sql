-- cities of california subquery
SELECT id, name FROM cities WHERE state_id = (SELECT id From states WHERE name = 'California') ORDER BY ASC;
