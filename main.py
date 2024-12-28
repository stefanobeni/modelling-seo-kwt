import numpy as np
import pandas as pd

# Read csv file
file_path = '/Users/stefanobeni/Code_Projects/Misc_Projects/modelling-seo-kwt/keyword-tracker.csv'
df = pd.read_csv(file_path)

# Number of tables to extract
number_tables = 24

# Initialize variables
key_words = []
formatted_key_words = []
tables = []

# Find key-words
i = 2
for index in range(number_tables):
    kw = df.iloc[i, 0]
    formatted_kw = kw.replace(' ', '-')

    key_words.append(kw)
    formatted_key_words.append(formatted_kw)
    i += 8
# print(key_words)

# Select the tables and add them to 'tables'
j = 3
for index in range(number_tables):
    table = df.iloc[j:(j+5), 0:6]
    table.columns = table.iloc[0, 0:6]  # Here it is 0 with respect to the current table (not the whole file)
    tables.append(table)
    j += 8
print(tables)

# Need to change this as this way the first row is duplicated as the column names
# AND as the first row

# Create csv files
# for k, table in enumerate(tables):
#     table.to_csv(f'{formatted_key_words[k]}-table.csv')
