import numpy as np

A = [[1, 2, 3], [4, 5, 6]]


def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    if not A or not A[0]:
        raise ValueError("A must be a non-empty matrix.")

    array = np.array(A)
    n_rows, n_columns = array.shape
    transposed_matrix = np.zeros(shape=(n_columns, n_rows), dtype=array.dtype)

    for i in range(n_rows):
        for j in range(n_columns):
            transposed_matrix[j, i] = array[i, j]

    return transposed_matrix


matrix_transpose(A)

# pure-python version
import numpy as np

A = [
    ["a", "b", "c", "d"],
    ["e", "f", "g", "h"],
    ["i", "j", "k", "l"],
]


def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    n_rows = len(A)
    n_columns = len(A[0])

    # list comprehension
    # [0] * n_rows: creates a single row with n_rows columns filled with zeros
    # for _ in range(n_columns) repeat that n_columns times
    # So, if input have 3 rows and 4 columns
    # [0] * n_rows creates a single row with 3 columns (n_rows) that have 3 zeros in it
    # for _ in range(n_columns) creates this row 4 times (n_columns)
    transposed_matrix = [[0] * n_rows for _ in range(n_columns)]

    for i in range(n_rows):
        for j in range(n_columns):
            transposed_matrix[j][i] = A[i][j]

    transposed_matrix = np.array(transposed_matrix)

    return transposed_matrix


matrix_transpose(A)
