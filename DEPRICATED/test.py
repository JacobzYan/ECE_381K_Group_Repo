import pandas as pd
from Format_csvs import *
from Combine_Analyze_csvs import *
import os
import time


total_unique_vals = 0
Formatter = ColumnFormatter(verbose=True)
df = pd.read_csv('non_numerical_columns.csv')
print('df read in')
sys.stdout.flush()

for col in df.columns:
    if col != 'index':
        t1 = time.time()
        df_test = pd.DataFrame()
        df_test[col] = df[col]
        
        print(f'Column: {col}')
        sys.stdout.flush()
        unique_vals =set(df_test[col])
        print(f'\tUnique values: {unique_vals}\n\tNumber of unique values: {len(unique_vals)}')
        
        sys.stdout.flush()

        

        df_test = Formatter.format_non_numerical(df_test, [col])
        t2 = time.time()
        total_unique_vals += len(unique_vals)
        print(f'\tElapsed time: {t2-t1}s')
        sys.stdout.flush()
    
    
print(f'TOTAL NUMBER OF UNIQUE VALUES: {total_unique_vals}')



# d = {'c1': ['T', 'F', 'F', 'T'], 'c2': [3, 4, 0, 2], 'c3':['NA', 'NA', '1920x1080', '3x4'], 'F_NF': ['Found', 'NotFound', 'NotFound', 'NA'], 'N_F_U': ['New', 'Found', 'Unknown', 'NA']}
# df = pd.DataFrame(data=d)

# non_num_cols = df.drop('c2', axis=1).columns


# print(f'df pre ohe: \n{df}')

# df = Formatter.format_non_numerical(df, non_num_cols)

# print(f'df post ohe: \n{df}')





