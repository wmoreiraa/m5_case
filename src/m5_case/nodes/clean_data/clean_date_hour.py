import pandas as pd
from pandas import DataFrame
from datetime import datetime

def _combine_date_time(df, datecol, timecol):
    """Aux function to combine datetime"""
    return pd.to_datetime(df[datecol].dt.date.astype(str)+ ' '+ df[timecol].astype(str))
    

def clean_date_hour(df: DataFrame) -> DataFrame:
    """Preenche a coluna de hora com a parte de hora que está no date e deixa date só date,
    cria uma nova coluna com datetime
    Input:
        - df: DataFrame
    Output:
        - df:DataFrame        
    """
    #dropando uma linha errada
    df = df.drop(61564)
    
    temp_date = pd.DataFrame([date.split(' ') for date in df.DATE])
    temp_date.columns = ['DATE','HOUR']
    
    df['HOUR'] = df['HOUR'].fillna(temp_date['HOUR'])
    df['DATE'] = temp_date['DATE']
    df['DATE'] = pd.to_datetime(df['DATE'], infer_datetime_format = True)
    df = df[df['DATE'].notna()]
    df['MONTH'] = df['DATE'].dt.month
    df['MONTH'] = df['MONTH'].astype(int)
    
    df['YEAR'] = df['DATE'].dt.year
    df['YEAR'] = df['YEAR'].astype(int)
    df['HOUR_DT'] = pd.to_datetime(df['HOUR'], format = '%H:%M:%S')
    df['HOUR_DT'] = df['HOUR_DT'].dt.time
    
    df['DATETIME'] = _combine_date_time(df, 'DATE', 'HOUR_DT')
    df.set_index('DATETIME', inplace = True)
   
    return df
