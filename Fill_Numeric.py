# Passing in a csv of a dataframe with only numeric columns, normalizes them with the function in Format_csvs.ColumnFormatter.formatNumerical()

import pandas as pd
from Format_csvs import *

import time

# read cli arguments, clean input
improper_input_reason = ''
if len(sys.argv) == 3:
    numeric_filename = sys.argv[1]
    output_filename = sys.argv[2]
else:
    print('To output dataframes, include 2 filenames as sys args (or import and call the function):\n\tfilename 1: numeric df filename\n\tfilename 2: output filename')
    exit()

t1 = time.time()

total_unique_vals = 0
Formatter = ColumnFormatter(verbose=False)
print('Reading in df...')
sys.stdout.flush()
df = pd.read_csv(numeric_filename)

Y = df[['TransactionID', 'isFraud']].copy()

X = df.drop('TransactionID', axis=1).drop('isFraud', axis=1)

print('Finding numerical/non numerical columns...')
sys.stdout.flush()
non_numerical_cols = get_non_numerical_cols(X)
numerical_cols = [i for i in list(X.columns) if i not in non_numerical_cols]

print('Filling numerical values...')
sys.stdout.flush()
X = Formatter.format_numerical(X, numerical_cols, filename=output_filename)

print('Writing output...')
Formatter.write_output('Changelog_' + output_filename)
Y.to_csv('Y_'+output_filename)

t2 = time.time()
print(f'Finished Formatting, elapsed time: {t2-t1}s')