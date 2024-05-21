# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(nums):
    from itertools import combinations

    return list(
        map(
            list,
            {comb for i in range(len(nums) + 1) for comb in combinations(nums, i)},
        )
    )


def main():
    test_cases = [
        dict(
            nums=[1, 2, 3],
            output=[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
        )
    ]
    for i, test_case in enumerate(test_cases):
        nums, required_output = test_case.values()
        output = solution(nums)
        output.sort()
        required_output.sort()

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
