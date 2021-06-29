from kedro.pipeline import Pipeline, node

from m5_case.nodes.make_dataset import (
    create_covidfeature,
    join_tables
)



def make_dataset_pipeline(**kwargs):
    return Pipeline(
        [
        node(
            func = join_tables,
            inputs = ['peru_clean', 'lima_clean'],
            outputs = 'dataset_clean',
            tags = ['make_dataset'],
            name = "table_joins"
        ),                
        node(
            func = create_covidfeature,
            inputs = "dataset_clean",
            outputs = "dataset_covid",
            tags = ['make_dataset'],
            name = 'covid'
        )
        ]
    )