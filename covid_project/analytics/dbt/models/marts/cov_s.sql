SELECT
    cc.case_id,
    cc.severity_rank,
    cc.location
FROM
    {{ ref('covid_cases') }} AS cc
JOIN
    {{ ref('covid_locations') }} AS cl
ON
    cc.location = cl.location_id
GROUP BY
    cc.case_id,
    cc.severity_rank,
    cc.location
ORDER BY
    cc.severity_rank DESC
