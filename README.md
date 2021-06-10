# missingness_dummy_coder
This function takes a filename for a csv, reads it in as a pandas dataframe and creates a list of missing symbols and creates dummy variables with a missingess flag


```python
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
```

Example usage:

```python
filename = 'df.csv'
list_nans = [np.nan, 'na', '888', 999]

df_with_flags = missing_coder(filename=filename, list_nans=list_nans)
```
