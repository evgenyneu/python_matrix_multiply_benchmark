from multiply import multiply, multiply_numpy
from pytest import approx
import numpy as np
import random
from timeit import default_timer as timer


def test_matrix_multiply():
    matrix1 = [[1, 2], [4.2, 5], [7, 8]]
    matrix2 = [[2.1, 1.1], [4.1, -1.1]]

    result = multiply(matrix1, matrix2)

    assert len(result) == 3
    assert len(result[0]) == 2

    assert result[0][0] == approx(10.3, rel=1e-5)
    assert result[0][1] == approx(-1.1, rel=1e-5)

    assert result[1][0] == approx(29.32, rel=1e-5)
    assert result[1][1] == approx(-0.88, rel=1e-5)

    assert result[2][0] == approx(47.5, rel=1e-5)
    assert result[2][1] == approx(-1.1, rel=1e-5)


def test_matrix_multiply_1000x1000_benchmark():
    size = 1000
    rows1 = size
    columns1 = size
    columns2 = size

    matrix1 = [[random.uniform(-1, 1) for _ in range(columns1)] for _ in range(rows1)]
    matrix2 = [[random.uniform(-1, 1) for _ in range(columns2)] for _ in range(columns1)]

    start = timer()

    result = multiply(matrix1, matrix2)

    end = timer()

    print(f"\nMultiply {size}x{size} matrices with three loops: {end - start} s\n")
    assert result[0][0] != 42


def test_matrix_multiply_with_numpy():
    matrix1 = [[1, 2], [4.2, 5], [7, 8]]
    matrix2 = [[2.1, 1.1], [4.1, -1.1]]

    result = multiply_numpy(matrix1, matrix2)

    assert len(result) == 3
    assert len(result[0]) == 2

    assert result[0][0] == approx(10.3, rel=1e-5)
    assert result[0][1] == approx(-1.1, rel=1e-5)

    assert result[1][0] == approx(29.32, rel=1e-5)
    assert result[1][1] == approx(-0.88, rel=1e-5)

    assert result[2][0] == approx(47.5, rel=1e-5)
    assert result[2][1] == approx(-1.1, rel=1e-5)


def test_matrix_multiply_500x500_with_numpy():
    size = 1000
    rows1 = size
    columns1 = size
    columns2 = size

    matrix1 = [[random.uniform(-1, 1) for _ in range(columns1)] for _ in range(rows1)]
    matrix2 = [[random.uniform(-1, 1) for _ in range(columns2)] for _ in range(columns1)]

    start = timer()

    result = multiply_numpy(np.array(matrix1), np.array(matrix2))

    end = timer()

    print(f"\nMultiply {size}x{size} matrices with numpy: {end - start} s\n")
    assert result[0][0] != 42