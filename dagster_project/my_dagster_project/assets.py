from dagster import job, op
from .my_jobs import dbt_resource

@op(required_resource_keys={"dbt"})
def my_dbt_op(context):
    context.log.info("Running dbt command")

    # Properly specify both project_dir and profiles_dir
    result = context.resources.dbt.run(
        project_dir="/Users/alexaustinchettiar/Downloads/dbt_snowflake_dagster/dbt_project",
        profiles_dir="/Users/alexaustinchettiar/Downloads/dbt_snowflake_dagster/dbt_project"
    )

    context.log.info(f"DBT result: {result}")

@job(resource_defs={"dbt": dbt_resource})
def dbt_transformation_job():
    my_dbt_op()
