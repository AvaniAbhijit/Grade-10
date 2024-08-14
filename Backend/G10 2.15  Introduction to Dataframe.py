
import pandas as pd

# Creating a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 41, 29]}#data is given using dictionary
df = pd.DataFrame(data)#converts the data into table with Name and Age as headers
print(df)
