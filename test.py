import pandas as pd
from Format_csvs import *
# from Format_csvs import *
import os
import time


# total_unique_vals = 0
Formatter = ColumnFormatter(verbose=True)

# df = pd.read_csv('non_numerical_columns.csv')
# print('df read in')
# sys.stdout.flush()

# for col in df.columns:
#     if col != 'index':
#         t1 = time.time()
#         df_test = pd.DataFrame()
#         df_test[col] = df[col]
        
#         print(f'Column: {col}')
#         sys.stdout.flush()
#         unique_vals =set(df_test[col])
#         print(f'\tUnique values: {unique_vals}\n\tNumber of unique values: {len(unique_vals)}')

        
#         sys.stdout.flush()

        

#         df_test = Formatter.format_non_numerical(df_test, [col])
#         t2 = time.time()
#         total_unique_vals += len(unique_vals)
#         print(f'\tElapsed time: {t2-t1}s')
#         sys.stdout.flush()
    
    
# print(f'TOTAL NUMBER OF UNIQUE VALUES: {total_unique_vals}')
try:
    testing_case = int(sys.argv[1])
except:
    testing_case = -1
print(f'test case {testing_case}')

if testing_case ==1:
    d = {'c1': ['T', 'F', 'F', 'T'], 'c2': [3, 4, 0, 2], 'resolution':['1x1', '2x2', '1920x1080', '3x4'], 'F_NF': ['Found', 'NotFound', 'NotFound', np.nan], 'MATCH_STATUS': ['match_status:2', 'match_status:2', 'match_status:0', 'match_status:1']}
    df = pd.DataFrame(data=d)

    non_num_cols = df.drop('c2', axis=1).columns


    print(f'df pre ohe: \n{df}')

    df = Formatter.format_non_numerical(df, non_num_cols)

    print(f'df post ohe: \n{df}')

if testing_case==2:
    Formatter2 = ColumnFormatter(verbose=True)
    df = pd.read_csv('combined_output.csv')
    df = df[['id_30']]
    print(df)

    df = Formatter2.format_non_numerical(df, ['id_30'])
    print(df)

if testing_case == 3:
    Formatter2 = ColumnFormatter(verbose=True)
    df = pd.read_csv('combined_output.csv')
    df = df[['DeviceInfo']]
    print(df)

    df = Formatter2.format_non_numerical(df, ['DeviceInfo'])
    print(df)


if testing_case == 4:
    Formatter2 = ColumnFormatter(verbose=True)
    df = pd.read_csv('combined_output.csv')
    df = df[['P_emaildomain']]
    print(df)

    df = Formatter2.format_non_numerical(df, ['P_emaildomain'])
    print(df)


if testing_case == 5:
    Formatter2 = ColumnFormatter(verbose=True)
    df = pd.read_csv('combined_output.csv')
    df = df[['R_emaildomain']]
    print(df)

    df = Formatter2.format_non_numerical(df, ['R_emaildomain'])
    print(df)

