import pandas as pd
import numpy as np
from datetime import datetime 
from pandas import DataFrame

def clean_nulls(df: DataFrame) -> DataFrame:
    """ Preenche com pela media ou mediana agrupada por ano, mes e hora.
    
    Args :
        Input: 
        DataFrame
        Output:
        DataFrame
        
    """
    #temp por media
    df['TEMP'] = df.groupby(['YEAR', 'MONTH', 'HOUR'])\
                   .TEMP.transform(lambda x: x.fillna(x.mean()))
    df['TEMP'] = df.groupby(['YEAR', 'MONTH'])\
                   .TEMP.transform(lambda x: x.fillna(x.mean()))
    #chuva por median
    df['PREC_H'] = df.groupby(['YEAR', 'MONTH', 'HOUR'])\
                   .PREC_H.transform(lambda x: x.fillna(x.median()))
    df['PREC_H'] = df.groupby(['YEAR', 'MONTH'])\
                   .PREC_H.transform(lambda x: x.fillna(x.median()))
        
        
    #humidade por mediana
    df['HUM'] = df.groupby(['YEAR', 'MONTH', 'HOUR'])\
                   .HUM.transform(lambda x: x.fillna(x.median()))
    df['HUM'] = df.groupby(['YEAR', 'MONTH'])\
                   .HUM.transform(lambda x: x.fillna(x.median()))
        
    # direcao por media 
    df['W_DIR'] = df.groupby(['YEAR', 'MONTH', 'HOUR'])\
                   .W_DIR.transform(lambda x: x.fillna(x.mean()))
    df['W_DIR'] = df.groupby(['YEAR', 'MONTH'])\
                   .W_DIR.transform(lambda x: x.fillna(x.mean()))
    # velocidade do vento POR MEDIAN
    df['W_VEL'] = df.groupby(['YEAR', 'MONTH', 'HOUR'])\
                   .W_VEL.transform(lambda x: x.fillna(x.median()))
    df['W_VEL'] = df.groupby(['YEAR', 'MONTH'])\
                   .W_VEL.transform(lambda x: x.fillna(x.median()))
    df = df.interpolate(method= 'linear')
    return df