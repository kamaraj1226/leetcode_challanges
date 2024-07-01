# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(arr):
    N = len(arr)
    if N < 3:
        return False

    if N == 3:
        return sum(arr) & 1

    i = 0
    while i < N - 3:
        if sum(arr[i : i + 3]) & 1:
            return True
        i += 1

    return False


def main():
    test_cases = [
        dict(arr=[2, 6, 4, 1], output=False),
        dict(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12], output=True),
    ]
    for i, test_case in enumerate(test_cases):
        arr, required_output = test_case.values()
        output = solution(arr)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
