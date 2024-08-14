import pandas as pd

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 41, 29]}
df = pd.DataFrame(data)

excel_file_path = 'data1.xlsx'

#setting mode as "w". It creates a new Excel file or overwrites an existing file if it already exists. If the file already exists, it will be replaced with a new one.
with pd.ExcelWriter(excel_file_path, engine="openpyxl",mode='w') as writer:
    df.to_excel(writer,sheet_name="Marks Sheet", index=False)

print("DataFrame successfully added to Excel sheet.")
