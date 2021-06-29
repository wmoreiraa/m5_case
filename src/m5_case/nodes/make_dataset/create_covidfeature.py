
import pandas as pd
from pandas import DataFrame



def create_covidfeature(df: DataFrame) -> DataFrame:
    """Cria feature dizendo o dia que começou covid binario"""
    df.loc['2020-03-16':,'pos_covid'] = 1
    df.fillna(0, inplace = True)
    df['pos_covid'] = df['pos_covid'].astype(int)
    
    return df