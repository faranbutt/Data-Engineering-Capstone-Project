SELECT
    case_id, 
    location, 
    age, 
    gender
FROM {{ ref('stg_covid_cases') }}

