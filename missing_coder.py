import pandas as pd
import numpy as np

'''inputs to func look something like this:

filename = 'test_dataset.csv'
list_nans = [np.nan, 'na', 88, 999]
new_df = missing_coder(filename=filename, list_nans=list_nans'''

def missing_coder(filename, list_nans):
    df = pd.read_csv(filename, na_values=list_nans)
    cols = df.columns
    
    for col in cols:
        check_null = df[col].isnull()
        
        if check_null.sum() >= 1:
            new_col_name = col + '_miss_flag'
            new_cols_vals = np.zeros(len(df)).astype('float32')
            
            for index in df.index.values[check_null]:
                new_cols_vals[index] = 1.0
            df[new_col_name] = new_cols_vals
    return df
