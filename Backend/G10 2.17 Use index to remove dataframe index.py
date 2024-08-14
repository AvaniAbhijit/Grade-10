import pandas as pd

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 41, 29]}
df = pd.DataFrame(data)

excel_file_path = 'data.xlsx'

df.to_excel(excel_file_path,index=False) #adding index to remove the index of dataframe

print("DataFrame successfully added to Excel sheet.")
