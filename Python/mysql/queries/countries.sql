--1
SELECT countries.name AS country_name, languages.language, languages.percentage FROM world.countries
JOIN world.languages ON countries.code = languages.country_code
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;
--2
SELECT countries.name AS country_name, COUNT(cities.country_id) AS total_cities FROM world.countries
JOIN world.cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.country_id) DESC;
--3
SELECT cities.name, cities.population FROM world.cities
WHERE cities.country_id = (SELECT id FROM world.countries WHERE countries.name = 'Mexico') AND cities.population >= 500000;
--4
SELECT countries.name AS country, languages.language, languages.percentage FROM world.languages
JOIN world.countries ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;
--5
SELECT name AS country, surface_area, population FROM world.countries
WHERE surface_area < 501 AND population > 100000;
--6
SELECT name AS country, capital, government_form, life_expectancy FROM countries
WHERE
	capital > 200 AND
    government_form = 'Constitutional Monarchy' AND
    life_expectancy > 75;
--7
SELECT countries.name AS country, cities.name AS city, cities.district, cities.population FROM world.cities
JOIN world.countries ON countries.id = cities.country_id
WHERE
	cities.country_id = (SELECT countries.id FROM world.countries WHERE countries.name = 'Argentina') AND
    cities.district = 'Buenos Aires' AND
    cities.population > 500000;
--8
SELECT region, COUNT(id) AS total_countries FROM world.countries
GROUP BY region
ORDER BY COUNT(id) DESC;