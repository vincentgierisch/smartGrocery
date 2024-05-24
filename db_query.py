import sqlite3


def read_from_sqlite(db_path, query):
    """
    Connects to an SQLite database and reads data using the specified query.

    Parameters:
    db_path (str): Path to the SQLite database file.
    query (str): SQL query to execute.

    Returns:
    list of tuple: Retrieved rows from the database.
    """
    # Connect to the SQLite database
    connection = sqlite3.connect(db_path)

    # Create a cursor object
    cursor = connection.cursor()

    # Execute the query
    cursor.execute(query)

    # Fetch all results from the executed query
    results = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return results


# Example usage
db_path = 'smartGrocery.db'  # Path to your SQLite database file
query = 'SELECT * FROM ProductList;'  # Replace with your SQL query

# Read data from the SQLite database
data = read_from_sqlite(db_path, query)

# Print the fetched data
for row in data:
    print(row)
