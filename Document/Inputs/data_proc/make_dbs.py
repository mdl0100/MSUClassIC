import os
import pandas as pd
from sqlalchemy import create_engine

# Path to the directory containing Excel files
directory_path = r'C:\Users\Marcos\Dropbox\CMPS\5153_SE\MSUClassiC\Document\Inputs\Rolled'

# Database connection string
# For SQLite, it looks like: ''
# For MySQL, it looks like: 'mysql+pymysql://user:password@localhost/dbname'
# For PostgreSQL, it looks like: 'postgresql://user:password@localhost/dbname'
fall_url = 'sqlite:///fall2024.sqlite'
fall_engine = create_engine(fall_url)

sum_1_url = 'sqlite:///summer_1_2024.sqlite'
sum_1_engine = create_engine(sum_1_url)

sum_2_url = 'sqlite:///summer_2_2024.sqlite'
sum_2_engine = create_engine(sum_2_url)

# Name of the table to which data will be written
table_name = 'courses'

endings = [
    '202430.xlsx' ,
    '202440.xlsx',
    '202510.xlsx',
]

# Loop through each file in the directory
for file_name in os.listdir(directory_path):
    for ending in endings:
        if file_name.endswith(ending):
            # Read the Excel file into a DataFrame
            df = pd.read_excel(os.path.join(directory_path, file_name))
            
            # Write the DataFrame to the database
            if ending == '202430.xlsx':
                df.to_sql(table_name, sum_1_engine, if_exists='append', index=False)
            elif ending == '202440.xlsx':
                df.to_sql(table_name, sum_2_engine, if_exists='append', index=False)
            elif ending == '202510.xlsx':
                df.to_sql(table_name, fall_engine, if_exists='append', index=False)