from dagster import asset

@asset
def my_first_asset():
    return "Hello, Dagster!"
