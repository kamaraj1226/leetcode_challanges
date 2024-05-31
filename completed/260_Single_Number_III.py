# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(nums):

    from collections import Counter

    return [num for num, count in Counter(nums).items() if count == 1]


def main():
    test_cases = [
        dict(nums=[1, 2, 1, 3, 2, 5], output=[3, 5]),
        dict(nums=[-1, 0], output=[-1, 0]),
        dict(nums=[0, 1], output=[1, 0]),
    ]
    for i, test_case in enumerate(test_cases):
        nums, required_output = test_case.values()
        output = solution(nums)

        required_output.sort()
        output.sort()

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
