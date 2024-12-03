import pandas as pd
from Format_csvs import *
import time

# read cli arguments, clean input
improper_input_reason = ''
if len(sys.argv) == 3:
    combined_filename = sys.argv[1]
    output_filename = sys.argv[2]
else:
    print('To output dataframes, include 2 filenames as sys args (or import and call the function):\n\tfilename 1: combined df filename\n\tfilename 2: output filename')
    exit()

t1 = time.time()


Formatter = ColumnFormatter(verbose=False)
print('Reading in df...')
sys.stdout.flush()
df = pd.read_csv(combined_filename)


# REDUCED SIZE FOR DEBUG
# df = df[:200]
df = df.infer_objects()
# print(f'df: \n{df}')


Y = df[['TransactionID', 'isFraud']].copy()

X = df.drop('isFraud', axis=1)


print('Counting NA values...')
sys.stdout.flush()
X['NA_Count'] = X.isna().sum(axis=1)

print('Finding numerical/non numerical columns...')
sys.stdout.flush()
non_numerical_cols = get_non_numerical_cols(X)

numerical_cols = [i for i in list(X.columns) if i not in non_numerical_cols]
numerical_cols.remove('TransactionID')  # Do not normalize transaction ID
numerical_cols.append('id_33')
numerical_cols.append('id_34')



print('Encoding non numerical values...')
sys.stdout.flush()
X = Formatter.format_non_numerical(X, non_numerical_cols, filename=output_filename)

print('Filling numerical values...')
sys.stdout.flush()
X = Formatter.format_numerical(X, numerical_cols, filename=output_filename)


# THIS SECTION IS NOT WORKING, manually readjusting these columns for now
# add back the columns that are non numerical that get converted into numerical
# print('\tFilling converted categorical variables...')
# sys.stdout.flush()
# new_non_numerical_cols = get_non_numerical_cols(X)
# missed_non_numerical_cols = set(new_non_numerical_cols).difference(set(non_numerical_cols))
# missed_non_numerical_cols = ['id_33', 'id_34']
# print(f'\tMissed_non_numerical_cols: {missed_non_numerical_cols}')
# X = Formatter.format_numerical(X, missed_non_numerical_cols, filename=output_filename)


print('Writing output...')
Formatter.write_output('Changelog_' + output_filename)
Y.to_csv('Y_'+output_filename)

t2 = time.time()
print(f'Finished Formatting, elapsed time: {t2-t1}s')