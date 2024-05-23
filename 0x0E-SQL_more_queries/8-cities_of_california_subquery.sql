-- Use the database hbtn_0d_usa
SELECT c.id, c.name
FROM cities AS c
WHERE c.state_id = (
  SELECT id
    FROM states
      WHERE name = 'California'
      );

ORDER BY c.id ASC;
