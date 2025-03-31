{{ config(alias='users_view') }}

SELECT *
FROM {{ source('duckdb_sources', 'users') }}
WHERE age > 25