def matrix_divided(matrix, divisor):
    """
    Divides all the numbers in a matrix by a specified divisor.

    Parameters:
    - matrix (list of lists): A matrix containing integers or floats.
    - divisor (number): The number by which each element in the matrix is divided.

    Returns:
    list of lists: A new matrix with each element rounded to 2 decimal places.

    Raises:
    - TypeError: If the matrix is not a list of lists of integers or floats,
                 or if each row in the matrix does not have the same size,
                 or if the divisor is not a number.
    - ZeroDivisionError: If the divisor is equal to 0.
    """

    # Check if the matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("The matrix must be a list of lists of integers or floats")

    # Check if each row in the matrix has the same size
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row in the matrix must have the same size")

    # Check if the divisor is a number
    if not isinstance(divisor, (int, float)):
        raise TypeError("The divisor must be a number")

    # Check if the divisor is not equal to 0
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    # Divide each element in the matrix by the divisor, rounding to 2 decimal places
    result_matrix = [[round(element / divisor, 2) for element in row] for row in matrix]

    return result_matrix

