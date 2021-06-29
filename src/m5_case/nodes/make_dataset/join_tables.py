import pandas as pd
from pandas import DataFrame
from datetime import datetime


def join_tables(df1: DataFrame, df2: DataFrame) -> DataFrame:
    """
    Faz upsample no df2 para 15m,
    interpola linearmente, faz o left join e depois dropa colunas
    que vão ser criadas corretamentas
    """
    df2 = df2.resample('15min').interpolate(method='linear')
    df = df1.join(df2, lsuffix = '', rsuffix = '')
    df.drop(columns=['DATE','HOUR','HOUR_DT'], axis = 1, inplace= True)
    
    return df 
