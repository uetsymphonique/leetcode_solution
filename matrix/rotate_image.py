from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n - 2 * i - 1):
            matrix[i][i + j], matrix[i + j][-(1 + i)], matrix[-(1 + i)][-(1 + i + j)], matrix[-(1 + i + j)][i] = \
                matrix[-(1 + i + j)][i], matrix[i][i + j], matrix[i + j][-(1 + i)], matrix[-(1 + i)][-(1 + i + j)]


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
[print(mat) for mat in matrix]
print("---")
rotate(matrix)
[print(mat) for mat in matrix]
