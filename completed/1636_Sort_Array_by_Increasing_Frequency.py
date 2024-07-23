# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(nums):
    from collections import Counter

    result = []
    for val, times in sorted(Counter(nums).items(), key=lambda x: (x[1], -x[0])):
        result += [val] * times
    return result


def main():
    test_cases = [
        dict(nums=[1, 1, 2, 2, 2, 3], output=[3, 1, 1, 2, 2, 2]),
        dict(nums=[2, 3, 1, 3, 2], output=[1, 3, 3, 2, 2]),
    ]
    for i, test_case in enumerate(test_cases):
        nums, required_output = test_case.values()
        output = solution(nums)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
