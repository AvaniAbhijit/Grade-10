
import pandas as pd

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 41, 29]}
df = pd.DataFrame(data)

excel_file_path = 'data1.xlsx'

#Instead of raising an error when the sheet already exists, you can choose to overwrite the existing sheet by using if_sheet_exists.
with pd.ExcelWriter(excel_file_path, engine="openpyxl",mode='a',if_sheet_exists='replace') as writer:
    df.to_excel(writer,sheet_name="Marks Sheet", index=False)

print("DataFrame successfully added to Excel sheet.")
