from typing import List


def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    n_rows, n_cols = len(board), len(board[0])
    isLive = [[False] * n_cols for _ in range(n_rows)]

    def count_neighbors(i: int, j: int):
        nonlocal board, isLive, n_rows, n_cols
        return (board[i][j + 1] if j + 1 < n_cols else 0) + (board[i][j - 1] if j > 0 else 0) + (
            board[i + 1][j] if i + 1 < n_rows else 0) + (board[i - 1][j] if i > 0 else 0) + (
            board[i - 1][j - 1] if i > 0 and j > 0 else 0) + (
            board[i - 1][j + 1] if i > 0 and j + 1 < n_cols else 0) + (
            board[i + 1][j - 1] if i + 1 < n_rows and j > 0 else 0) + (
            board[i + 1][j + 1] if i + 1 < n_rows and j + 1 < n_cols else 0)

    for i in range(n_rows):
        for j in range(n_cols):
            n_neighbors = count_neighbors(i, j)
            if board[i][j] == 1 and (n_neighbors == 2 or n_neighbors == 3):
                isLive[i][j] = True
            elif board[i][j] == 0 and n_neighbors == 3:
                isLive[i][j] = True

    for i in range(n_rows):
        for j in range(n_cols):
            board[i][j] = int(isLive[i][j])
