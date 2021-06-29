import pandas as pd
import numpy as np
from datetime import datetime

from pandas import DataFrame

def setindex_peru(df: DataFrame) -> DataFrame:
    """Muda a coluna data para datetime e depois coloca como index """
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
    df.set_index('date',inplace = True)
    return df