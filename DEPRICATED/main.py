import pandas as pd
from Format_csvs import *
from Combine_Analyze_csvs import *
import os
import time

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


combined_filename='combined_training_data.csv'

outputs = read_Cols(combined_filename=combined_filename)
df = outputs['combined_df']
dfx = df.drop('isFraud', axis=1)

non_numerical_cols = outputs['non_numerical_cols']
numerical_cols = [x for x in df.columns if x not in non_numerical_cols]
Formatter = ColumnFormatter()

t1 = time.time()
print('Formatting...')
sys.stdout.flush()
df = Formatter.format_non_numerical(df, non_numerical_cols)
df = Formatter.format_numerical(df, numerical_cols.append('id33'), 'Formatted_df') # ID 33 resolution-> number of pixels
Formatter.write_output('Translations.csv')
t2 = time.time()

print(f'Formatting time: {t2-t1}')
