def multiply(matrix1, matrix2):
    """
    Multiplies two matrices matrix1 * matrix2

    Parameters
    ----------
    matrix1, matrix2: list of list of float
        The two matrices to matiply

    Returns
    -------
    list of list of float
        Result of matrix multiplication: matrix1 * matrix2
    """

    rows1 = len(matrix1)
    columns1 = len(matrix1[0])
    row2 = len(matrix2)
    columns2 = len(matrix2[0])

    if columns1 != row2:
        print("ERROR: Incompatible dimensions")
        return

    result = [[0 for _ in range(columns2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(columns2):
            sum_cell = 0

            for k in range(columns1):
                sum_cell += matrix1[i][k] * matrix2[k][j]

            result[i][j] = sum_cell

    return result