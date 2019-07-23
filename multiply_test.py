from multiply import multiply
from pytest import approx
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


def test_matrix_multiply_benchmark():
    rows1 = 1000
    columns1 = 1000
    columns2 = 1000

    matrix1 = [[random.uniform(-1, 1) for _ in range(columns1)] for _ in range(rows1)]
    matrix2 = [[random.uniform(-1, 1) for _ in range(columns2)] for _ in range(columns1)]

    start = timer()

    result = multiply(matrix1, matrix2)

    end = timer()

    print(f"\nMultiply with three loops: {end - start} s\n")
    assert result[0][0] != 42