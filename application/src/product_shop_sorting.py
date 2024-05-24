import numpy as np
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
def sort(matrix):
    sums = [sum([get_sign(entry) for entry in row]) for row in matrix]
    sums = np.array(sums)
    sorted_indices = np.argsort(sums)
    return sorted_indices

if __name__ == '__main__':
    # Define the size of the square matrix
    n = 5  # For example, a 5x5 matrix

    # Generate a random square matrix with values between -10 and 10
    matrix = np.random.randint(-10, 11, size=(n, n))

    # Print the matrix
    print(matrix)
    sort(matrix)
