# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(rowSum, colSum):
    m = len(rowSum)
    n = len(colSum)

    X = []

    for i in range(m):
        c = []
        for j in range(n):
            _min = min(rowSum[i], colSum[j])
            c.append(_min)
            rowSum[i] -= _min
            colSum[j] -= _min
        X.append(c)
    return X


def check_output(matrix, rowSum, colSum):
    # compute row sum
    _rowSum = [sum(row) for row in matrix]

    # compute col sum
    _colSum = []
    for c in range(len(colSum)):
        temp = 0
        for r in range(len(rowSum)):
            temp += matrix[r][c]
        _colSum.append(temp)

    return _rowSum == rowSum and colSum == _colSum


def main():
    test_cases = [
        dict(rowSum=[3, 8], colSum=[4, 7], output=[[3, 0], [1, 7]]),
        dict(
            rowSum=[5, 7, 10],
            colSum=[8, 6, 8],
            output=[[0, 5, 0], [6, 1, 0], [2, 0, 8]],
        ),
    ]
    for i, test_case in enumerate(test_cases):
        rowSum, colSum, _ = test_case.values()
        output = solution(rowSum[:], colSum[:])
        _output = check_output(output, rowSum, colSum)

        print(f"Test {i+1}: {'pass' if _output else 'failed'}")


if __name__ == "__main__":
    main()
