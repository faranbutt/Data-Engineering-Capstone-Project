SELECT
    de.baseId,
    dc.baseSymbol,
    SUM(fmd.tradesCount24Hr) AS total_trading
FROM
    {{ ref('fact_market_data') }} AS fmd
JOIN
    {{ ref('dim_exchange') }} AS de
ON
    fmd.baseId = de.baseId
JOIN
    {{ ref('dim_currency') }} AS dc
ON
    dc.baseId = de.baseId
GROUP BY
    de.baseId,
    dc.baseSymbol
ORDER BY
    SUM(fmd.tradesCount24Hr) DESC
