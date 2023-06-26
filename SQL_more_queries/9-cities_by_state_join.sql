-- list all cities in database hbtn_0d_usa
-- display all cities.id/name/name

SELECT cities.id, cities.name, states.name; 
FROM cities JOIN states ON cities.states_id = states.id;
ORDER BY cities.id ASC;