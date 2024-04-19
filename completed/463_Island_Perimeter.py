def solution(grid):

    def find_adjacent(r, c):
        _perimeter = 4
        row_bound = len(grid)
        col_bound = len(grid[0])

        # look down
        if r + 1 < row_bound:
            if grid[r + 1][c] == 1:
                _perimeter -= 1

        # look up
        if r - 1 >= 0:
            if grid[r - 1][c] == 1:
                _perimeter -= 1

        # look left
        if c + 1 < col_bound:
            if grid[r][c + 1] == 1:
                _perimeter -= 1

        # look right
        if c - 1 >= 0:
            if grid[r][c - 1] == 1:
                _perimeter -= 1
        return _perimeter

    perimeter = 0

    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == 1:
                perimeter += find_adjacent(i, j)
    return perimeter


def main():

    test_cases = [
        dict(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], output=16),
        dict(grid=[[1]], output=4),
        dict(grid=[[1, 0]], output=4),
        dict(grid=[[1, 1], [1, 1]], output=8),
    ]

    for i, test_case in enumerate(test_cases):
        grid, required_output = test_case.values()
        output = solution(grid)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
