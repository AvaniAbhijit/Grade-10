import pandas as pd

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 41, 29]}
df = pd.DataFrame(data)

excel_file_path = 'data1.xlsx'

#setting mode as "a". This mode appends data to an existing Excel file. It opens the file for writing, but instead of overwriting existing content,
#it appends new data to the end of the file
with pd.ExcelWriter(excel_file_path, engine="openpyxl",mode='a') as writer:
    df.to_excel(writer,sheet_name="Marks Sheet", index=False)

print("DataFrame successfully added to Excel sheet.")
