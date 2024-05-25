# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(nums, k):

    def check_subset(s) -> bool:
        if len(s) == 1:
            result.add(tuple(s))
            return True

        r = False
        from itertools import combinations

        for comb in combinations(s, 2):
            x, y = comb
            if abs(x - y) != k:
                result.add(comb)
                r = True
        print(s)
        print(result)
        print("================")
        return r

    def backtrack(start):
        if start == len(nums):
            return
        for end in range(start + 1, len(nums) + 1):
            check_subset(nums[start:end])
            backtrack(end)

    result = set()
    backtrack(0)
    # check_subset(nums)
    # print(result)
    # results = set(map(tuple, result))
    # print(len(results), results)
    print(len(result))
    # print(result)
    return len(result)


def main():
    test_cases = [
        # dict(nums=[2, 4, 6], k=2, output=4),
        # dict(nums=[1], k=1, output=1),
        dict(nums=[4, 2, 5, 9, 10, 3], k=1, output=23),
    ]
    for i, test_case in enumerate(test_cases):
        nums, k, required_output = test_case.values()
        output = solution(nums, k)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
