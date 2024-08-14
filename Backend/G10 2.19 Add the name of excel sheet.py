import pandas as pd

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 41, 29]}
df = pd.DataFrame(data)

excel_file_path = 'data.xlsx'

with pd.ExcelWriter(excel_file_path, engine="openpyxl") as writer:
    df.to_excel(writer,sheet_name="Marks Sheet", index=False)#adding sheet_name

print("DataFrame successfully added to Excel sheet.")
