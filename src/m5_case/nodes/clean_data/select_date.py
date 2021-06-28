from pandas import DataFrame
import pandas as pd
from typing import Any, Dict, Iterable, Optional




def select_date(df: DataFrame, date) -> DataFrame:
    """ Seleciona data catalogada como parametro """
    df = df.loc[date:]
    return df