
  
  create view "my_database"."main"."users_view__dbt_tmp" as (
    

SELECT *
FROM "my_database"."main"."users"
WHERE age > 25
  );
