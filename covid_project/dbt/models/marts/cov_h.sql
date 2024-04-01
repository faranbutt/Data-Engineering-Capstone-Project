SELECT
    cc.case_id,
    pl.location,
    AVG(cc.deaths) AS average_deaths
FROM
    {{ ref('covid_cases') }} AS cc
JOIN
    {{ ref('covid_locations') }} AS pl
ON
    cc.location = pl.location_id
GROUP BY
    cc.case_id, pl.location
ORDER BY
    average_deaths DESC
