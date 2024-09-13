import pandas as pd
import numpy as np

def performDataProcessing(data_fpath:str,output_dir:str)-> None:
    #Reading data
    df=pd.read_csv(data_fpath)

    # Feature Engineering
    df['log_resistance_ohm'] = np.log(df['resistance_ohm'])
    df['resistance_humidity'] = df['resistance_ohm'] * df['humidity_ppmv']
    df['resistance_temperature'] = df['resistance_ohm'] * df['temperature_celsius']

    # Removing irrelevent attirbutes and the attributes with high multicolinearity
    df.drop(
        columns=[
            'temperature_celsius',
            'resistance_ohm',
            'humidity_ppmv','time_s','operator'
            ],inplace=True
        )
    
    df.to_csv(f'{output_dir}/processed_data.csv',index=False)
    return

if __name__=='__main__':
    data_fp='hydrogen_concentration/data/data.csv'
    output_dir='hydrogen_concentration/data'
    performDataProcessing(data_fp,output_dir)
    print('Data Processing Completed!!!')