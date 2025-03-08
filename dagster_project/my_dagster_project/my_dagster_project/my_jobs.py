from dagster import job, op
from dagster_dbt import dbt_run_op
import pandas as pd
import snowflake.connector

@op
def extract_and_load():
    conn = snowflake.connector.connect(
        user="XXXXXXXXXXXXXX",
        password="XXXXXXXXXXXXXX",
        account="XXXXXXXXXXXXXX",
        warehouse="COMPUTE_WH",
        database="MY_DB",
        schema="MY_SCHEMA"
    )
    
    df = pd.read_csv("data/raw_users.csv")
    for _, row in df.iterrows():
        conn.cursor().execute(
            "INSERT INTO my_schema.my_first_dbt_model (id) VALUES (%s)", 
            (row["id"])
        )
    
    conn.close()

@job
def my_pipeline():
    extract_and_load()
    dbt_run_op.configured({"project_dir": "dbt_project"})
