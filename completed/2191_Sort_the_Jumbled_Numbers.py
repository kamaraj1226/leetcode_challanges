# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(mapping, nums):
    mapped_nums = []

    for num in nums:
        s = ""
        for c in str(num):
            s += str(mapping[int(c)])
        mapped_nums.append(int(s))

    return [
        val[0]
        for val in sorted(
            zip(nums, mapped_nums, range(len(nums))), key=lambda x: (x[1], x[-1])
        )
    ]


def main():
    test_cases = [
        dict(
            mapping=[8, 9, 4, 0, 2, 1, 3, 5, 7, 6],
            nums=[991, 338, 38],
            output=[338, 38, 991],
        ),
        dict(
            mapping=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            nums=[789, 456, 123],
            output=[123, 456, 789],
        ),
    ]
    for i, test_case in enumerate(test_cases):
        mapping, nums, required_output = test_case.values()
        output = solution(mapping, nums)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
