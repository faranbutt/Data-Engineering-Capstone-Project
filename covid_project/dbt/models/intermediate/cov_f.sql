SELECT
    case_id,
    date_reported,
    location,
    age,
    gender,
    symptoms,
    status
FROM {{ ref('stg_covid_data') }}

