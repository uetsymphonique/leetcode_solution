from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    ans, spiral_matrix, m, n = [], [[-1] * len(matrix[0]) for _ in range(len(matrix))], len(matrix), len(matrix[0])

    def generate_spiral_matrix(top_left_col, top_left_row, m_rows, n_cols):
        print(
            f'Generating spiral matrix(top_left_col={top_left_col}, top_left_row={top_left_row}, m_rows={m_rows}, n_cols={n_cols})')
        if m_rows > 0 and n_cols > 0:

            for i in range(top_left_col, top_left_col + n_cols):
                if spiral_matrix[top_left_row][i] == -1:
                    spiral_matrix[top_left_row][i] = 1
                    ans.append(matrix[top_left_row][i])

            for i in range(top_left_row + 1, top_left_row + m_rows - 1):
                if spiral_matrix[i][top_left_col + n_cols - 1] == -1:
                    spiral_matrix[i][top_left_col + n_cols - 1] = 1
                    ans.append(matrix[i][top_left_col + n_cols - 1])

            for i in range(top_left_col + n_cols - 1, top_left_col - 1, -1):
                if spiral_matrix[top_left_row + m_rows - 1][i] == -1:
                    spiral_matrix[top_left_row + m_rows - 1][i] = 1
                    ans.append(matrix[top_left_row + m_rows - 1][i])

            for i in range(top_left_row + m_rows - 2, top_left_row, -1):
                if spiral_matrix[i][top_left_col] == -1:
                    spiral_matrix[i][top_left_col] = 1
                    ans.append(matrix[i][top_left_col])

            print(spiral_matrix)
            generate_spiral_matrix(top_left_col + 1, top_left_row + 1, m_rows - 2, n_cols - 2)

    generate_spiral_matrix(0, 0, m, n)
    return ans


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiralOrder(matrix))
