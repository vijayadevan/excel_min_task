import pandas as pd
import re

concat_val = ''
tbl = pd.read_excel('Sample_data.xlsx', header=None)
row = 0
cycle_complete = True

for i in tbl.values:
    if cycle_complete:
        if tbl.size == row + 1:
            concat_val += i[0]
        if tbl.at[row + 1, 0].startswith('-'):
            concat_val += f'{i[0]}{tbl.at[row+1, 0]}'
            cycle_complete = False
        if re.match('^[A-Za-z]', tbl.at[row + 1, 0]):
            concat_val += f'{i[0]} {tbl.at[row + 1, 0]}'
            cycle_complete = False
        if re.match('^[0-9]', tbl.at[row + 1, 0]):
            concat_val += f'{i[0]}\n'
            cycle_complete = True
    elif tbl.size != row + 1:
        if re.match('^[A-Za-z]', tbl.at[row + 1, 0]):
            concat_val += f' {tbl.at[row + 1, 0]}'
        elif re.match('^[0-9]', tbl.at[row + 1, 0]):
            concat_val += '\n'
            cycle_complete = True
    row += 1

with open('Output.txt', 'w') as fh:
    fh.write(concat_val)
