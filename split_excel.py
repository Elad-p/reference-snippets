import pandas as pd
data = pd.read_excel('countries.xlsx')
continents = data['continent'].unique()
file = pd.ExcelWriter('New_Countries.xlsx')
for continent in continents:
    data[data['continent'] == continent].sort_values(by = ['country', 'year']).to_excel(file, sheet_name = continent, index = False)
file.save()