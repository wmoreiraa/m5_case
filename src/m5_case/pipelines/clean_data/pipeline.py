from kedro.pipeline import Pipeline, node

from m5_case.nodes import (
        clean_date_hour
        )

def clean_data_pipeline(**kwargs):
    return Pipeline([
        node(
            func = clean_date_hour,
            inputs = "lima",
            outputs "lima_clean",
            tags = ["clean_data"],
            name = "clean_date_hour"
        ),
        node(
            func =,
            inputs = ,
            outputs = ,
            tags = ,
            name = ,
            )

