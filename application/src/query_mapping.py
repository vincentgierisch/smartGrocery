import sqlite3
import copy

def get_product_mappings_for_supermarket(db_path, supermarket_id, product_ids):
    """
    Retrieves mappings for a specific supermarket ID and stores referenced product IDs in a two-dimensional array.

    Parameters:
    db_path (str): Path to the SQLite database file.
    supermarket_id (int): The ID of the supermarket.

    Returns:
    list of list: Two-dimensional array of product IDs.
    """
    # Connect to the SQLite database
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Create placeholders for filters
    product_id1_placeholders = ','.join('?' for _ in product_ids)
    product_id2_placeholders = ','.join('?' for _ in product_ids)

    # SQL query to select and sort mappings for the given supermarket ID with additional filters
    query = f'''
    SELECT ProductID1, ProductID2, Counter 
    FROM Mapping 
    WHERE SupermarketID = ?
    AND ProductID1 IN ({product_id1_placeholders})
    AND ProductID2 IN ({product_id2_placeholders})
    ORDER BY ProductID1, ProductID2
    '''

    # Combine all parameters for the query
    parameters = [supermarket_id] + product_ids + product_ids

    # Execute the query with the given parameters
    cursor.execute(query, parameters)
    # Fetch all results
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Process the results into a dictionary grouped by ProductID1
    grouped_mappings = {}
    product_ids_list = []
    for product_id1, product_id2, Counter in rows:
        if product_id1 not in grouped_mappings:
            product_ids_list.append(product_id1)
            grouped_mappings[product_id1] = []
        grouped_mappings[product_id1].append(Counter)

    # Convert the dictionary into a two-dimensional array
    product_mappings = [product_id2_list for product_id1, product_id2_list in grouped_mappings.items()]

    return product_ids_list, product_mappings

def calculate_comparison_matrix(mapping_matrix):
    copy_matrix = copy.deepcopy(mapping_matrix)

    for i in range(len(mapping_matrix)):
        for j in range(len(mapping_matrix[i])):
            copy_matrix[i][j] = mapping_matrix[i][j] - mapping_matrix[j][i]
    return copy_matrix


if __name__ == '__main__':
    # Example usage
    db_path = '../../smartGrocery.db'  # Path to your SQLite database file
    supermarket_id = 1  # Replace with the desired SupermarketID

    # Get product mappings for the specified SupermarketID
    product_ids, product_mappings = get_product_mappings_for_supermarket(db_path, supermarket_id, [7002, 3001,3002,2001,4001,4002,5001,5002,6001,6002,7001,7003,8001,9001])

    product_mappings = calculate_comparison_matrix(product_mappings)
    # Print the two-dimensional array of product mappings
    print(product_ids)
    for mapping in product_mappings:
        print(mapping)
