# Only used for exploratory data analysis, not used in overall data cleaning pipeline

import pandas as pd
import time
from sklearn.preprocessing import StandardScaler
import sys


def read_Cols(combined_filename='', non_numerical_filename='', verbose=False):
    
    # Read in provided csvs
    print('Reading in...')
    sys.stdout.flush()
    t1 = time.time()
    df_trans = pd.read_csv('train_transaction.csv')
    df_id = pd.read_csv('train_identity.csv')


    # Combine csvs
    print('Packaging Data...')
    sys.stdout.flush()
    t2 = time.time()
    df_total = pd.merge(df_id, df_trans, how='outer')
    X_train = df_total.drop(columns=['TransactionID', 'isFraud'])
    Y_train = df_total['isFraud']


    # Pull non numerical columns
    print('Analyzing columns...')
    sys.stdout.flush()
    t3 = time.time()
    print('cols in X, types ')
    non_numerical_cols = get_non_numerical_cols(df_total, verbose=False)



    # Export combined sets to new files
    t4 = time.time()
    if combined_filename:
        df_total.to_csv(combined_filename)
        print(f'Combined data exported to {combined_filename}')
    if non_numerical_filename:
        output_df = df_total[non_numerical_cols]
        output_df.to_csv(non_numerical_filename)
        print(f'Non-numerical columns exported to {non_numerical_filename}')

    # Print output
    print(df_total.head())
    print(f'Elapsed Reading time: {t2-t1:.2f}s')
    print(f'Elapsed Data manipulation time: {t3-t2:.2f}s')
    print(f'Elapsed Column typing time: {t4-t3:.2f}s')

    return {'combined_df': df_total, 'non_numerical_cols': non_numerical_cols}

def get_non_numerical_cols(df, verbose=False):
    non_numerical_cols = []
    for col in df.columns:
        data_type = set(type(i) for i in df[col])
        if data_type.__contains__(type(' ')):
            non_numerical_cols.append(col)
        
        if verbose:
            print(f"\t{col}: {data_type}")
    return non_numerical_cols


if __name__ == '__main__': 
    # read cli arguments, clean input
    improper_input_reason = ''
    if len(sys.argv) == 2:
        combined_filename = sys.argv[1]
        non_numerical_filename = ''
    elif len(sys.argv) == 3:
        combined_filename = sys.argv[1]
        non_numerical_filename = sys.argv[2]
    else:
        print('To output dataframes, include 1 or 2 filenames as sys args (or import and call the function)')
        combined_filename = ''
        non_numerical_filename = ''
    
    
    read_Cols(combined_filename=combined_filename, non_numerical_filename=non_numerical_filename, verbose=True)