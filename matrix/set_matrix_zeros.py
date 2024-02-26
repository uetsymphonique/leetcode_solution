from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = set()
    cols = set()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for row in rows:
        for j in range(0, len(matrix[0])):
            matrix[row][j] = 0

    for col in cols:
        for i in range(0, len(matrix)):
            matrix[i][col] = 0
