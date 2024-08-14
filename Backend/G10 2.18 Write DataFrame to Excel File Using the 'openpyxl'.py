
import pandas as pd

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 41, 29]}
df = pd.DataFrame(data)

excel_file_path = 'data.xlsx'

# Create ExcelWriter object with openpyxl engine
with pd.ExcelWriter(excel_file_path, engine="openpyxl") as writer:
    df.to_excel(writer, index=False)
#The above code saves DataFrame df to an Excel file specified by excel_file_path using the
#'openpyxl' engine for writing, ensuring proper file handling with the with statement

print("DataFrame successfully added to Excel sheet.")
