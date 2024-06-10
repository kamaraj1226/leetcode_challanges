# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(heights):
    result = 0

    for i, j in zip(heights, sorted(heights)):
        if i != j:
            result += 1

    return result


def main():
    test_cases = [
        dict(heights=[1, 1, 4, 2, 1, 3], output=3),
        dict(heights=[5, 1, 2, 3, 4], output=5),
        dict(heights=[1, 2, 3, 4, 5], output=0),
    ]
    for i, test_case in enumerate(test_cases):
        heights, required_output = test_case.values()
        output = solution(heights)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
