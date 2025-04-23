# from dagster import repository
# from .assets import dbt_transformation_job  # Make sure to import the job from your assets.py
# from .assets import my_asset  # If you have assets, import them too
# from .my_jobs import dbt_transformation_job
# @repository
# def my_dagster_project_repo():
#     return [
#         dbt_transformation_job,  # Add your jobs here
#         my_asset,  # Add assets if any
#     ]


from dagster import repository
from .assets import dbt_transformation_job  # assuming job is defined in assets.py

@repository
def my_dagster_project_repo():
    return [dbt_transformation_job]

