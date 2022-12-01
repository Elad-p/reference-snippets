import pandas as pd

source = ? # Your source file name
target = ? # Your target file name
sort_col = ? # By which column do you want your output to be sorted by

data = pd.read_excel(source, sheet_name = None)
data = pd.concat(data).reset_index().drop(columns = 'level_1').rename({'level_0' 'new_col'}, axis = 1)
data.sort_values(sort_col).to_excel(target, index = False, sheet_name = 'All_Data')