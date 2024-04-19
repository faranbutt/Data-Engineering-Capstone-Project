SELECT 
    case_id,
    date_reported
FROM 
    {{ ref("stg_covid_cases") }}
