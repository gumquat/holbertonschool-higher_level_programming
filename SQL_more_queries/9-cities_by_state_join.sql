-- list all cities in database hbtn_0d_usa
-- display all cities.id/name/name

SELECT cities.id, cities.name, states.name
  FROM cities LEFT JOIN states
    ON cities.state_id = states.id;