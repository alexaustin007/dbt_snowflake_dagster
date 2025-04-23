# # from dagster import job, op, Definitions
# # from dagster_dbt import dbt_cli_resource, dbt_run_op

# # # Path to your dbt project (adjust if different)
# # DBT_PROJECT_PATH = "/Users/alexaustinchettiar/Downloads/dbt_snowflake_dagster/dbt_project"

# # # Define the dbt resource
# # dbt_resource = dbt_cli_resource.configured({
# #     "project_dir": DBT_PROJECT_PATH,
# #     "profiles_dir": DBT_PROJECT_PATH,  # adjust if your profiles.yml is elsewhere
# # })

# # # Use prebuilt op from dagster-dbt to run dbt
# # @job
# # def dbt_transformation_job():
# #     dbt_run_op()

# # # Register the job and dbt resource in Definitions
# # defs = Definitions(
# #     jobs=[dbt_transformation_job],
# #     resources={
# #         "dbt": dbt_resource,
# #     },
# # )


# from dagster import job, Definitions
# from dagster_dbt import dbt_cli_resource, dbt_run_op

# # Path to your dbt project (adjust if different)
# DBT_PROJECT_PATH = "/Users/alexaustinchettiar/Downloads/dbt_snowflake_dagster/dbt_project"

# # Define the dbt resource
# dbt_resource = dbt_cli_resource.configured({
#     "project_dir": DBT_PROJECT_PATH,
#     "profiles_dir": DBT_PROJECT_PATH,  # Ensure this path is correct
# })

# # Use prebuilt op from dagster-dbt to run dbt
# @job
# def dbt_transformation_job():
#     dbt_run_op(dbt=dbt_resource)  # Pass the resource to the dbt_run_op

# # Register the job and dbt resource in Definitions
# defs = Definitions(
#     jobs=[dbt_transformation_job],
#     resources={
#         "dbt": dbt_resource,
#     },
# )


# from dagster import Definitions
# from dagster_dbt import dbt_cli_resource
# from .assets import dbt_transformation_job

# # Path to your dbt project
# DBT_PROJECT_PATH = "/Users/alexaustinchettiar/Downloads/dbt_snowflake_dagster/dbt_project"

# # Define the dbt resource
# dbt_resource = dbt_cli_resource.configured({
#     "project_dir": DBT_PROJECT_PATH,
#     "profiles_dir": DBT_PROJECT_PATH,
# })

# # Register your job and resource
# defs = Definitions(
#     jobs=[dbt_transformation_job],
#     resources={"dbt": dbt_resource},  # Here is where you pass the resource
# )


from dagster_dbt import dbt_cli_resource

DBT_PROJECT_PATH = "/Users/alexaustinchettiar/Downloads/dbt_snowflake_dagster/dbt_project"

dbt_resource = dbt_cli_resource.configured({
    "project_dir": DBT_PROJECT_PATH,
    "profiles_dir": DBT_PROJECT_PATH,
})

