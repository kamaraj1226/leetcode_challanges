# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=use-dict-literal
# pylint: disable=import-outside-toplevel


def solution(grid):
    total_island = 0

    def find_connected_islands(row, col):
        if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]):
            return
        if grid[row][col] == "0":
            return

        grid[row][col] = "0"
        find_connected_islands(row + 1, col)  # down
        find_connected_islands(row - 1, col)  # up
        find_connected_islands(row, col - 1)  # left
        find_connected_islands(row, col + 1)  # right

    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == "1":
                total_island += 1
                find_connected_islands(i, j)

    return total_island


def optimized_solution(grid):
    from collections import deque

    total_island = 0
    queue = deque()
    re, ce = len(grid), len(grid[0])

    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == "1":
                total_island += 1
                queue.append((i, j))

                while len(queue) > 0:
                    _r, _c = queue.pop()
                    grid[_r][_c] = "0"

                    # left
                    if 0 <= _c - 1 < ce and 0 <= _r < re and grid[_r][_c - 1] == "1":
                        queue.append((_r, _c - 1))

                    if 0 <= _c + 1 < ce and 0 <= _r < re and grid[_r][_c + 1] == "1":
                        queue.append((_r, _c + 1))

                    if 0 <= _c < ce and 0 <= _r + 1 < re and grid[_r + 1][_c] == "1":
                        queue.append((_r + 1, _c))
                    if 0 <= _c < ce and 0 <= _r - 1 < re and grid[_r - 1][_c] == "1":
                        queue.append((_r - 1, _c))

    return total_island


def main():
    test_cases = [
        dict(
            grid=[
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            output=1,
        ),
        dict(
            grid=[
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            output=3,
        ),
    ]
    for i, test_case in enumerate(test_cases):
        grid, required_output = test_case.values()
        output = optimized_solution(grid)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
