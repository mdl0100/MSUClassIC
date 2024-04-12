import sqlite3

def create_database(db_name):
    # Connect to SQLite database (create if not exists)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS Fall24 (
                        
                    )''')

    

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"Database '{db_name}' created successfully!")

if __name__ == "__main__":
    # Specify the name of the database file
    db_name = "MSUCLASSIC.db"

    # Create the database
    create_database(db_name)
