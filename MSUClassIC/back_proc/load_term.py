import sqlite3
from pprint import pp as print

def read_database(db_path):
    # Connect to the SQLite database at the specified path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Define the SQL query to fetch required columns
    query = """
    SELECT CRN, SUBJ, CRSE, DAYS, BEGN, ENDING, BLDG, ROOM, PRIMLAST, PRIMFIRST
    FROM courses
    """
    
    # Execute the query
    cursor.execute(query)
    
    # Fetch all rows from the query result
    rows = cursor.fetchall()
    
    # Convert rows to a list of dictionaries
    columns = ["CRN", "SUBJ", "CRSE", "DAYS", "BEGN", "ENDING", "BO", "ROOM", "PRIMLAST", "PRIMFIRST"]
    result = []
    for row in rows:
        row_dict = {col: val for col, val in zip(columns, row)}
        result.append(row_dict)
    
    # Close the connection to the database
    cursor.close()
    conn.close()
    
    return result

def get_professors_by_department(db_path, department):
    # Connect to the SQLite database at the specified path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Prepare the SQL query to select professors based on the department
    query = """
    SELECT DISTINCT "PRIMLAST", "PRIMFIRST"
    FROM courses
    WHERE SUBJ = ?
    ORDER BY 1, 2
    """
    
    # Execute the query with department parameter
    cursor.execute(query, (department,))
    
    # Fetch all rows from the query result
    rows = cursor.fetchall()
    
    # Convert rows to a list of dictionaries for better readability (optional)
    result = [{"Last Name": last, "First Name": first} for last, first in rows]
    
    # Close the connection to the database
    cursor.close()
    conn.close()
    

    return result

def boxes():
    pass

if __name__ == '__main__':
    db_path = r'..\..\Document\Inputs\data_proc\fall2024.sqlite'
    data = read_database(db_path)
    #print(data)
    print(get_professors_by_department(db_path, "BIOL"))