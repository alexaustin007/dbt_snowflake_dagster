from dagster import repository
from .my_jobs import my_pipeline  # Import the job from my_jobs.py

@repository
def my_dagster_project_repo():
    return [my_pipeline]  # Add your job here
