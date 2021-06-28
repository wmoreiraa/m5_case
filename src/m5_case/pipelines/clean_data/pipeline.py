from kedro.pipeline import Pipeline, node

from m5_case.nodes.clean_data import (
        clean_date_hour,
        clean_nulls,
        select_date
        )

def clean_data_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func = clean_date_hour,
                inputs = "lima",
                outputs = "lima_v1",
                tags = ["clean_data"],
                name = "clean_date_hour"
            ),
            node(
                func = clean_nulls,
                inputs = "lima_v1",
                outputs = "lima_nulls",
                tags = ["clean_data"],
                name = "clean_nulls"
            ),
            node(
                func = select_date,
                inputs = ["lima_nulls", "params:start_date"],
                outputs = "lima_clean",
                tags = ["clean_data"],
                name = "select_date"
            )
        ]
    )


