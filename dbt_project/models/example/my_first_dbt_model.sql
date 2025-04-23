{{ config(materialized='table') }}

with source_data as (
    select 5 as id, 'John Doe' as name, 'john.doe@example.com' as email
    union all
    select 2 as id, 'Jane Smith' as name, 'jane.smith@example.com' as email
    union all
    select 3 as id, 'Bob Johnson' as name, 'bob.johnson@example.com' as email
    union all
    select 4 as id, 'Alice Brown' as name, 'alice.brown@example.com' as email
    union all
    select 1 as id, 'Bob Johnson' as name, 'bob.johnson@example.com' as email
)

select 
    id,
    name,
    email
from source_data
where id is not null
-- /*
--     Welcome to your first dbt model!
--     Did you know that you can also configure models directly within SQL files?
--     This will override configurations stated in dbt_project.yml

--     Try changing "table" to "view" below
-- */

-- {{ config(materialized='table') }}

-- with source_data as (

--     select 1 as id
--     union all
--     select null as id

-- )

-- select *
-- from source_data

-- /*
--     Uncomment the line below to remove records with null `id` values
-- */

-- -- where id is not null

