
import pandas as pd

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 41, 29]}
df = pd.DataFrame(data)

# Specify the file path for the Excel file
excel_file_path = 'data.xlsx'

# Write the DataFrame to an Excel sheet
df.to_excel(excel_file_path)

print("DataFrame successfully added to Excel sheet.")
