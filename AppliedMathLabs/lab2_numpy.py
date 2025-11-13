import time
import numpy as np
from typing import Union, Iterable


def create_identity_matrix(n: int) -> np.ndarray:
    """
    Example :
            for n=3
            1   0   0
            0   1   0
            0   0   1
    """
    return np.eye(n, dtype=int)

    pass


def scale_array(arr: np.ndarray, factor: Union[int, float]) -> np.ndarray:
    """
    Example:
        arr = [1, 3, 5, 7]
        factor = 2
        -> [2, 6, 10, 14]
    """
    return arr * factor
    pass


def get_column_sum(matrix: np.ndarray, col_index: int) -> Union[int, float, complex]:
    """
    Example:
        matrix =
                  1 3 5
                  2 4 6
                  9 9 9
        col_index = 0
        -> 12
    """
    return matrix[:, col_index].sum()
    pass


def check_positive(arr: np.ndarray) -> np.ndarray:
    """
    Example:
        [1, -3, -5, 9, 0] -> [True, False, False, True, False]
    """
    return arr > 0
    pass


def calculate_mean_rows(matrix: np.ndarray) -> np.ndarray:
    """
    Example:
            1 1 1
            2 2 2
        -> [1, 2]
    """
    return matrix.mean(axis=1)
    pass


def complex_conjugate_vector(arr: np.ndarray) -> np.ndarray:
    return np.conjugate(arr)
    pass


def get_complex_magnitude(arr: np.ndarray) -> np.ndarray:
    return np.abs(arr)
    pass


def check_hermitian(matrix: np.ndarray) -> bool:
    return np.allclose(matrix, matrix.conjugate().T)
    pass


def calculate_dot_product(vector_a: Iterable[Union[int, float, complex]],
                          vector_b: Iterable[Union[int, float, complex]]) \
        -> Union[int, float, complex]:
    """
    throwing exception in python ->  raise ValueError("Vectors must have the same length for dot product.")
    """
    a = np.array(list(vector_a))
    b = np.array(list(vector_b))
    if a.shape != b.shape:
        raise ValueError("Vectors must have the same length for dot product.")
    return np.vdot(a, b)

    pass

c
def compare_performance_dot_product(n: int = 10000) -> tuple[float, float]:
    # כתוב את הקוד שלך כאן
    # 1. Create random values arrays and lists
    np_a = np.random.random(n)
    np_b = np.random.random(n)
    # השוואה 1: List Comprehension
    start_time = time.time()
    # כתוב את הקוד שלך כאן
    start_time = time.time()
    dot_list = sum(a * b for a, b in zip(list_a, list_b))
    list_time = time.time() - start_time

    # השוואה 2: NumPy dot product
    start_time = time.time()
    dot_np = np.dot(np_a, np_b)
    numpy_time = time.time() - start_time

    return list_time, numpy_time


def compare_performance_scalar(n: int = 1_000_000) -> tuple[float, float]:
    np_arr = np.random.random(n)

    list_arr = np_arr.tolist()

    start_time = time.time()
    list_result = [x * 3 for x in list_arr]
    list_time = time.time() - start_time

    start_time = time.time()
    np_result = np_arr * 3
    numpy_time = time.time() - start_time

    return list_time, numpy_time
    pass
