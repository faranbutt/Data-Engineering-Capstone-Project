SELECT
    case_id,
    location
FROM {{ ref("stg_cov_data") }}

