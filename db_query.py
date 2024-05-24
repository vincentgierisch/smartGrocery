import sqlite3
from  application.src.fill_mapping import create_shopping_tour


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

def del_mapping_entries(db_path):
    conn = sqlite3.connect(db_path)  # Replace with your database file or connection string
    cursor = conn.cursor()

    # Delete all entries from the Mapping table
    cursor.execute("DELETE FROM Mapping")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
def add_mapping_entries(db_path, supermarked_id):
    conn = sqlite3.connect(db_path)  # Replace with your database file or connection string
    cursor = conn.cursor()

    # Fetch all ProductIDs from ProductList
    cursor.execute("SELECT ProductID FROM ProductList")
    product_ids = [row[0] for row in cursor.fetchall()]

    # Insert mappings into the Mapping table
    for product_id_1 in product_ids:
        for product_id_2 in product_ids:
            if product_id_1 != product_id_2:  # Skip self-mapping if not needed
                cursor.execute("INSERT INTO Mapping (ProductID1, ProductID2, SupermarketID, Counter) VALUES (?, ?, ?, ?)",
                               (product_id_1, product_id_2, supermarked_id, 0))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # Example usage
    db_path = 'smartGrocery.db'  #Path to your SQLite database file
    query = 'SELECT * FROM ProductList;'  # Replace with your SQL query

    # Read data from the SQLite database
    data = read_from_sqlite(db_path, query)

    # Print the fetched data
    for row in data:
        print(row)

    product_ids = [2001,3001,3002,4001,4002,5001,5002,6001,6002,7001,7002,7003,8001,9001]
    tour = create_shopping_tour(order_products=[i for i in range(len(product_ids))], min_products=3, max_products=len(product_ids), randomness=0.9)

    del_mapping_entries(db_path)
    add_mapping_entries(db_path, 1)
    add_mapping_entries(db_path, 2)

    print(tour)

