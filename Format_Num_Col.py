# Formats one column given the file and dataframe name
import pandas as pd
from Format_csvs import *
import time

# read cli arguments, clean input
improper_input_reason = ''
if len(sys.argv) == 3:
    filename = sys.argv[1]
    col = sys.argv[2]
else:
    print('Include the following system args(or import and call the function):\n\tfilename: combined df filename\n\tcolumn name: name of the column to format')
    exit()


# add back the columns that are non numerical that get converted into numerical
Formatter = ColumnFormatter(verbose=False)


print('Reading csv...')
sys.stdout.flush()
X = pd.read_csv(filename)


# for i in X.columns: 
#     print(f'\t{i}')
#     sys.stdout.flush()

print(f'id_33:\n{X[col]}')

print(f'Formatting {col} column...')
sys.stdout.flush()
X = Formatter.format_numerical(X, [col], filename=filename)