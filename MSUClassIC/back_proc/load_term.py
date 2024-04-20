import sqlite3
from pprint import pp as print

def read_database(db_path):
    # Connect to the SQLite database at the specified path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Define the SQL query to fetch required columns
    query = """
    SELECT CRN, SUBJ, CRSE, DAYS, BEGN, ENDING, BLDG, ROOM, PRIMLAST, PRIMFIRST, SEC
    FROM courses
    """
    
    # Execute the query
    cursor.execute(query)
    
    # Fetch all rows from the query result
    rows = cursor.fetchall()
    
    # Convert rows to a list of dictionaries
    columns = ["CRN", "SUBJ", "CRSE", "DAYS", "BEGN", "ENDING", "BLDG", "ROOM", "PRIMLAST", "PRIMFIRST", "SEC"]
    result = []
    for row in rows:
        row_dict = {col: val for col, val in zip(columns, row)}
        result.append(row_dict)
    
    # Close the connection to the database
    cursor.close()
    conn.close()
    
    return result



def get_professors_by_department(db_path, department=None):
    # Connect to the SQLite database at the specified path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Prepare the SQL query to select professors based on the department and the building 'BO'
    if department:
        query = """
        SELECT DISTINCT "PRIMLAST", "PRIMFIRST"
        FROM courses
        WHERE SUBJ = ? AND "BLDG" = 'BO'
        ORDER BY "PRIMLAST", "PRIMFIRST"
        """
    else:
        query = """
        SELECT DISTINCT "PRIMLAST", "PRIMFIRST"
        FROM courses
        WHERE "BLDG" = 'BO'
        ORDER BY "PRIMLAST", "PRIMFIRST"
        """
    
    # Execute the query with department parameter if provided
    if department:
        cursor.execute(query, (department,))
    else:
        cursor.execute(query)
    
    # Fetch all rows from the query result
    rows = cursor.fetchall()
    
    # Convert rows to a list of dictionaries for better readability (optional)
    result = [{"Last Name": last, "First Name": first} for last, first in rows]
    
    # Close the connection to the database
    cursor.close()
    conn.close()

    return result


def fetch_professor_courses(db_path, last_name, first_name):
 
    # Connect to the SQLite database at the specified path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Prepare the SQL query to select courses based on the professor
    query = """
    SELECT "SUBJ", "CRSE", "DAYS", "BEGN", "BLDG", "ROOM", "SEC"
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
        subj, crse, days, begn, bo, room, sec = row
        course_dict = {
            'SUBJ': subj,
            'CRSE': crse,
            'DAYS': days,
            'BEGN': begn,
            'BLDG': bo,
            'ROOM': room,
            'SEC' : sec
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

def layout_professors_courses():
    db_path = r'..\..\Document\Inputs\data_proc\fall2024.sqlite'
    data = read_database(db_path)
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
                details = f"{course_details['DAYS']} {format_time(course_details['BEGN'])} {course_details['BLDG']} {course_details['ROOM']}"
                layout[-1].append({'x': prof_idx+1, 'y': idx+1, 'w': 1, 'h': 1, 'i': details, 'static': True})

    # Print or return layout as needed
    output = []
    for row in layout:
        for entry in row:
            output.append(entry)
    print(output)

def is_time_within_bounds(time_str, start='0800', end='1700'):
    # Converts HHMM string to an integer for comparison
    return int(start) <= int(time_str) <= int(end)

def format_time(time_str):
    # Assuming time_str is in HHMM format for conversion to HH:MM AM/PM
    hour = int(time_str[:2])
    minute = int(time_str[2:])
    am_pm = 'AM' if hour < 12 else 'PM'
    hour = hour if hour <= 12 else hour - 12
    return f'{hour}:{minute:02d} {am_pm}'

def layout_professors_courses_MWF():
    db_path = r'..\..\Document\Inputs\data_proc\fall2024.sqlite'
    data = read_database(db_path)
    professors = []
    for entry in get_professors_by_department(db_path, "CMPS"):
        professor = fetch_professor_courses(db_path, entry['Last Name'], entry['First Name'])
        professors.append(professor)
    
    # Collect all unique courses with time and location details
    unique_courses = {}
    for prof in professors:
        for course in prof['Courses']:
            if course['DAYS'] and any(day in course['DAYS'] for day in ['M', 'W', 'F']) and course['BEGN'] is not None:
                try:
                    formatted_time = int(float(course['BEGN']))
                    time_key = f"{formatted_time}"
                    details_key = f"{course['SUBJ']} {course['CRSE']}.{course['SEC']} {course['BLDG']} {int(course['ROOM'])}"
                    if time_key not in unique_courses:
                        unique_courses[time_key] = []
                    unique_courses[time_key].append(details_key)
                except ValueError:
                    print(f"Skipping course with invalid time data: {course['BEGN']}")

    unique_times = sorted(unique_courses.keys(), key=lambda x: int(x))  # Sort times as integers

    # Map professors to courses with details
    layout = []
    # Header row for professors
    layout.append([{'x': i+1, 'y': 0, 'w': 1, 'h': 1, 'i': prof['Last Name'], 'static': True} for i, prof in enumerate(professors)])

    # Generate grid layout
    for idx, time in enumerate(unique_times):
        # First column for time
        layout.append([{'x': 0, 'y': idx+1, 'w': 1, 'h': 1, 'i': time, 'static': True}])
        # Course details per professor
        for prof_idx, prof in enumerate(professors):
            courses_at_time = [c for c in prof['Courses'] if c['BEGN'] is not None and int(float(c['BEGN'])) == int(time)]
            course_details = next((c for c in courses_at_time), None)
            if course_details:
                details_list = unique_courses[time]
                # Ensure to find the exact course detail
                details = next((d for d in details_list if f"{course_details['SUBJ']} {course_details['CRSE']}.{course_details['SEC']} {course_details['BLDG']} {int(course_details['ROOM'])}" == d), None)
                if details:
                    layout[-1].append({'x': prof_idx+1, 'y': idx+1, 'w': 1, 'h': 1, 'i': details, 'static': True, 'is_dept': True})

    # Print or return layout as needed
    output = []
    for row in layout:
        for idx in range(0, len(row)):
            output.append(row[idx])
    print(output)




def layout_professors_courses_TR():
    db_path = r'..\..\Document\Inputs\data_proc\fall2024.sqlite'
    data = read_database(db_path)
    professors = []
    for entry in get_professors_by_department(db_path, "CMPS"):
        professor = fetch_professor_courses(db_path, entry['Last Name'], entry['First Name'])
        professors.append(professor)
    
    # Collect all unique courses with time and location details
    unique_courses = {}
    for prof in professors:
        for course in prof['Courses']:
            if course['DAYS'] and any(day in course['DAYS'] for day in ['T', 'R']) and course['BEGN'] is not None:
                try:
                    formatted_time = int(float(course['BEGN']))
                    time_key = f"{formatted_time}"
                    details_key = f"{course['SUBJ']} {course['CRSE']}.{course['SEC']} {course['BLDG']} {int(course['ROOM'])}"
                    if time_key not in unique_courses:
                        unique_courses[time_key] = []
                    unique_courses[time_key].append(details_key)
                except ValueError:
                    print(f"Skipping course with invalid time data: {course['BEGN']}")

    unique_times = sorted(unique_courses.keys(), key=lambda x: int(x))  # Sort times as integers

    # Map professors to courses with details
    layout = []
    # Header row for professors
    layout.append([{'x': i+1, 'y': 0, 'w': 1, 'h': 1, 'i': prof['Last Name'], 'static': True} for i, prof in enumerate(professors)])

    # Generate grid layout
    for idx, time in enumerate(unique_times):
        # First column for time
        layout.append([{'x': 0, 'y': idx+1, 'w': 1, 'h': 1, 'i': time, 'static': True}])
        # Course details per professor
        for prof_idx, prof in enumerate(professors):
            courses_at_time = [c for c in prof['Courses'] if c['BEGN'] is not None and int(float(c['BEGN'])) == int(time)]
            course_details = next((c for c in courses_at_time), None)
            if course_details:
                details_list = unique_courses[time]
                # Ensure to find the exact course detail
                details = next((d for d in details_list if f"{course_details['SUBJ']} {course_details['CRSE']}.{course_details['SEC']} {course_details['BLDG']} {int(course_details['ROOM'])}" == d), None)
                if details:
                    layout[-1].append({'x': prof_idx+1, 'y': idx+1, 'w': 1, 'h': 1, 'i': details, 'static': True, 'is_dept': True})

    # Print or return layout as needed
    output = []
    for row in layout:
        for idx in range(0, len(row)):
            output.append(row[idx])
    print(output)



def layout_location_time_MWF():
    db_path = r'..\..\Document\Inputs\data_proc\fall2024.sqlite'
    data = read_database(db_path)
    professors = []
    rooms = set()
    for entry in get_professors_by_department(db_path):
        professor = fetch_professor_courses(db_path, entry['Last Name'], entry['First Name'])
        professors.append(professor)

        for course in professor['Courses']:
            if (course['DAYS']) and (any(day in course['DAYS'] for day in ['M', 'W', 'F'])):
                if course['ROOM'] and course['BLDG'] == 'BO':
                    course['ROOM'] = int(course['ROOM'])  # Convert room to integer for sorting
                    if course['ROOM'] in range(300, 400):  # Example range for room numbers
                        
                        rooms.add(int(course['ROOM']))

    # Sort and prepare room numbers as header row
    sorted_rooms = sorted(list(rooms))
    layout = [{'x': i+1, 'y': 0, 'w': 1, 'h': 1, 'i': int(room), 'static': True} for i, room in enumerate(sorted_rooms)]

    # Unique times and corresponding courses
    time_slots = {}
    for prof in professors:
        for course in prof['Courses']:
            if (course['DAYS']) and (any(day in course['DAYS'] for day in ['M', 'W', 'F'])):
                time = course['BEGN']
                if time not in time_slots:
                    time_slots[time] = []
                time_slots[time].append((course['SUBJ'], course['CRSE'], prof['Last Name'], course['ROOM'], course['SUBJ'] == 'CMPS'))

    sorted_times = sorted(time_slots.keys())
    for idx, time in enumerate(sorted_times):
        layout.append({'x': 0, 'y': idx+1, 'w': 1, 'h': 1, 'i': int(time), 'static': True})  # Time label
        for room in sorted_rooms:
            courses_in_room = [details for details in time_slots[time] if details[3] == room]
            if courses_in_room:
                course_details = courses_in_room[0]  # Pick first course that matches the room
                details = f"{course_details[2]} - {course_details[0]} {course_details[1]}"
                is_dept = course_details[4]
                layout.append({'x': sorted_rooms.index(room)+1, 'y': idx+1, 'w': 1, 'h': 1, 'i': details, 'static': True, 'is_dept': is_dept})
            else:
                pass
    print(layout)

def layout_location_time_TR():
    db_path = r'..\..\Document\Inputs\data_proc\fall2024.sqlite'
    data = read_database(db_path)
    professors = []
    rooms = set()
    for entry in get_professors_by_department(db_path):
        professor = fetch_professor_courses(db_path, entry['Last Name'], entry['First Name'])
        professors.append(professor)

        for course in professor['Courses']:
            if (course['DAYS']) and (any(day in course['DAYS'] for day in ['T', 'R'])):
                if course['BLDG'] == 'BO':
                    if course['ROOM']:
                        course['ROOM'] = int(course['ROOM'])  # Convert room to integer for sorting
                        if course['ROOM'] in range(300, 400):  # Example range for room numbers
                            
                            rooms.add(int(course['ROOM']))

    # Sort and prepare room numbers as header row
    sorted_rooms = sorted(list(rooms))
    layout = [{'x': i+1, 'y': 0, 'w': 1, 'h': 1, 'i': int(room), 'static': True} for i, room in enumerate(sorted_rooms)]

    # Unique times and corresponding courses
    time_slots = {}
    for prof in professors:
        for course in prof['Courses']:
            if (course['DAYS']) and (any(day in course['DAYS'] for day in ['T', 'R'])):
                time = course['BEGN']
                if time not in time_slots:
                    time_slots[time] = []
                time_slots[time].append((course['SUBJ'], course['CRSE'], prof['Last Name'], course['ROOM'], course['SUBJ'] == 'CMPS'))

    sorted_times = sorted(time_slots.keys())
    for idx, time in enumerate(sorted_times):
        layout.append({'x': 0, 'y': idx+1, 'w': 1, 'h': 1, 'i': int(time), 'static': True})  # Time label
        for room in sorted_rooms:
            courses_in_room = [details for details in time_slots[time] if details[3] == room]
            if courses_in_room:
                course_details = courses_in_room[0]  # Pick first course that matches the room
                details = f"{course_details[2]} - {course_details[0]} {course_details[1]}"
                is_dept = course_details[4]
                layout.append({'x': sorted_rooms.index(room)+1, 'y': idx+1, 'w': 1, 'h': 1, 'i': details, 'static': True, 'is_dept': is_dept})
            else:
                pass


    # Print or return layout as needed
    print(layout)

if __name__ == '__main__':
    layout_professors_courses_TR()