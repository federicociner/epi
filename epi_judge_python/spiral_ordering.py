from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    spiral_ordering = []
    direction = 0
    x = 0
    y = 0

    for _ in range(len(square_matrix) ** 2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x = x + SHIFT[direction][0]
        next_y = y + SHIFT[direction][1]

        if (
            next_x not in range(len(square_matrix))
            or next_y not in range(len(square_matrix))
            or square_matrix[next_x][next_y] == 0
        ):
            direction = (direction + 1) & 3
            next_x = x + SHIFT[direction][0]
            next_y = y + SHIFT[direction][1]

        x = next_x
        y = next_y

    return spiral_ordering


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "spiral_ordering.py", "spiral_ordering.tsv", matrix_in_spiral_order
        )
    )
