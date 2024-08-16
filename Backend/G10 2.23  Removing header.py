import pandas as pd

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 41, 29]}
df = pd.DataFrame(data)

excel_file_path = 'data1.xlsx'

with pd.ExcelWriter(excel_file_path, engine="openpyxl",mode='a',if_sheet_exists='replace') as writer:
    df.to_excel(writer,sheet_name="Marks Sheet", index=False,header=False)#removing the header

print("DataFrame successfully added to Excel sheet.")
