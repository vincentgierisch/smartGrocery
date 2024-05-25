import numpy as np
from .query_mapping import get_product_mappings_for_supermarket, calculate_comparison_matrix
def get_sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

"""
Returns sorted indices of the products with the one having the most incoming edges being the smallest one
"""
def get_sorting(matrix):
    sums = [sum([get_sign(entry) for entry in row]) for row in matrix]
    sums = np.array(sums)
    sorted_indices = np.argsort(sums)[::-1]
    return sorted_indices

def sort_shopping_list(db_path, supermarket_id, product_ids):
    product_ids, product_mappings = get_product_mappings_for_supermarket(db_path, supermarket_id, product_ids)
    product_mappings = calculate_comparison_matrix(product_mappings)
    print(np.array(product_mappings))
    sorting = get_sorting(product_mappings)
    print(f"sorting:{sorting}")
    sorted_product_ids = [product_ids[index] for index in sorting]
    print(sorted_product_ids)
    return sorted_product_ids



if __name__ == '__main__':
    db_path = '../../smartGrocery.db'  # Path to your SQLite database file
    supermarket_id = 1  # Replace with the desired SupermarketID

    # Get product mappings for the specified SupermarketID
    product_ids, product_mappings = get_product_mappings_for_supermarket(db_path, supermarket_id,
                                                                         [ 2001,3001, 3002, 4001, 4002, 5001, 5002,
                                                                          6001, 6002, 7001, 7002, 7003, 8001, 9001])
    print(product_ids)
    print(np.array(product_mappings))
    product_mappings = calculate_comparison_matrix(product_mappings)

    print(np.array(product_mappings))
    sorting = get_sorting(product_mappings)
    print(f"sorted_shopping_list: {sorting}")
    print([product_ids[index] for index in sorting])

    exit(0)
    # Define the size of the square matrix
    n = 5  # For example, a 5x5 matrix

    # Generate a random square matrix with values between -10 and 10
    matrix = np.random.randint(-10, 11, size=(n, n))

    # Print the matrix
    print(matrix)
    sort_shopping_list(matrix)
