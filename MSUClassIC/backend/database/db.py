import sqlite3
import pandas as pd
import os



def read_excel_files(folder_path):
    # Initialize an empty dictionary to store data from each Excel file
    excel_data = {}

    # Iterate through each file in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the file is an Excel file
        if filename.endswith('.xlsx'):
            # Read the Excel file into a DataFrame
            file_path = os.path.join(folder_path, filename)
            df = pd.read_excel(file_path)
            
            # Store the rows of the DataFrame as arrays in the dictionary
            excel_data[filename] = df.values.tolist() 
    
    #columns we want 
    chosen_ones = {1,2,7,8,9,12, 26,27,28,29,30,46,47}

    filtered_excel_data = {}

    for filename in excel_data:
        filtered_excel_data[filename] = []
        for row in excel_data[filename]:
            new_row = []
            for i in chosen_ones:
                new_row.append(row[i])
            filtered_excel_data[filename].append(new_row)
            
            

    print (filtered_excel_data)


   # print(excel_data)
    #return excel_data



'''def create_database(db_name):
    # Creates SQLite database 
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"Database '{db_name}' created successfully!")'''

def create_table(db_name, tb_name):
    # Connect to SQLite database (creates a new database if it doesn't exist)
    conn = sqlite3.connect(db_name)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table   
    cursor.execute('''CREATE TABLE ''' + tb_name + ''' (
                        COL TEXT,
                        SUBJ TEXT,
                        CRSE INTEGER,
                        SEC TEXT,
                        TITLE TEXT,
                        DAYS TEXT,
                        BEGN INTEGER,
                        ENDING INTEGER,
                        BLDG TEXT,
                        ROOM INTEGER,
                        PRIM_FIRST TEXT,
                        PRIM_LAST TEXT
                    )''')

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()


if __name__ == "__main__":
    # Specify the name of the database file
    db_name = "MSUCLASSIC.db"

    # Create the database
    #create_database(db_name)

    #create_table(db_name,"Fall2024")

    read_excel_files("C:\\Users\\User\\Downloads\\Rolled\\Rolled")
