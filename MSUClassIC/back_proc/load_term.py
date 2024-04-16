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

def fetch_professor_courses(db_path, last_name, first_name):
    """
    Fetches course details for a given professor from an SQLite database and organizes them into a structured dictionary.
    
    Args:
        db_path (str): The path to the SQLite database file.
        last_name (str): The last name of the professor.
        first_name (str): The first name of the professor.
    
    Returns:
        dict: A dictionary containing the professor's name and a list of their courses.
    """
    # Connect to the SQLite database at the specified path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Prepare the SQL query to select courses based on the professor
    query = """
    SELECT "SUBJ", "CRSE", "DAYS", "BEGN", "BO", "ROOM"
    FROM courses
    WHERE "PRIMLAST" = ? AND "PRIMFIRST" = ?
    ORDER BY "SUBJ", "CRSE"
    """
    
    # Execute the query with professor parameters
    cursor.execute(query, (last_name, first_name))
    
    # Fetch all rows from the query result
    rows = cursor.fetchall()
    
    # Convert rows to a list of dictionaries for better readability
    result = []
    for row in rows:
        subj, crse, days, begn, bo, room = row
        course_dict = {
            'SUBJ': subj,
            'CRSE': crse,
            'DAYS': days,
            'BEGN': begn,
            'BO': bo,
            'ROOM': room
        }
        result.append(course_dict)
    
    # Close the connection to the database
    cursor.close()
    conn.close()
    
    # Prepare the final dictionary for this professor
    professor_info = {
        'Last Name': last_name,
        'First Name': first_name,
        'Courses': result
    }
    
    return professor_info

def get_courses_by_department(db_path):
    # Connect to the SQLite database at the specified path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Prepare the SQL query to select courses based on the department
    query = """
    SELECT DISTINCT "CRSE"
    FROM courses
    WHERE "SUBJ" = "CMPS"
    ORDER BY 1
    """
    
    # Execute the query with department parameter
    cursor.execute(query)
    
    # Fetch all rows from the query result
    rows = cursor.fetchall()
    
    # Convert rows to a list of dictionaries for better readability (optional)
    result = [{"CMPS": course} for course in rows]
    
    # Close the connection to the database
    cursor.close()
    conn.close()
    
    return result

def format_time(time):
    """ Helper function to format time for display. """
    if time is None:
        return ''
    hour = int(time) // 100
    minute = int(time) % 100
    return f'{hour}:{minute:02}'

def main():
    professors = []
    for entry in get_professors_by_department(db_path, "CMPS"):
        professor = fetch_professor_courses(db_path, entry['Last Name'], entry['First Name'])
        professors.append(professor)

    # Find all unique courses
    unique_courses = set()
    for prof in professors:
        for course in prof['Courses']:
            if course['DAYS'] and course['BEGN']:
                unique_courses.add((course['SUBJ'], course['CRSE']))

    unique_courses = sorted(list(unique_courses), key=lambda x: (x[0], x[1]))  # Sort courses

    # Map professors to courses with details
    layout = []
    # Header row for professors
    layout.append([{'x': i+1, 'y': 0, 'w': 1, 'h': 1, 'i': prof['Last Name'], 'static': True} for i, prof in enumerate(professors)])

    # Generate grid layout
    for idx, (subj, crse) in enumerate(unique_courses):
        # First column for courses
        layout.append([{'x': 0, 'y': idx+1, 'w': 1, 'h': 1, 'i': f'{subj} {crse}', 'static': True}])
        # Course details per professor
        for prof_idx, prof in enumerate(professors):
            course_details = next((c for c in prof['Courses'] if c['SUBJ'] == subj and c['CRSE'] == crse and c['DAYS'] and c['BEGN']), None)
            if course_details:
                details = f"{course_details['DAYS']} {format_time(course_details['BEGN'])} {course_details['BO']} {course_details['ROOM']}"
                layout[-1].append({'x': prof_idx+1, 'y': idx+1, 'w': 1, 'h': 1, 'i': details, 'static': True})

    # Print or return layout as needed
    output = []
    for row in layout:
        for entry in row:
            output.append(entry)
    print(output)


if __name__ == '__main__':
    db_path = r'..\..\Document\Inputs\data_proc\fall2024.sqlite'
    data = read_database(db_path)
    #print(data)
    
    # professors = get_professors_by_department(db_path, "CMPS")
    # print(professors)
    # for professor in professors:
    #     courses = get_courses_by_professor(db_path, professor)
    #     print(professor)
    #     print(courses)
    
    

    # courses = get_courses_by_department(db_path)
    # print(courses)

    main()