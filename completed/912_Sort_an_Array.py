# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(nums):
    def merge_sorted_list(left, right):
        result = []

        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        while left:
            result.append(left.pop(0))

        while right:
            result.append(right.pop(0))

        return result

    def merge_sort(nums):
        N = len(nums)

        if N == 1:
            return nums

        mid = N // 2
        left = nums[:mid]
        right = nums[mid:]

        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)

        return merge_sorted_list(sorted_left, sorted_right)

    return merge_sort(nums)


def main():
    test_cases = [
        dict(nums=[5, 2, 3, 1], output=[1, 2, 3, 5]),
        dict(nums=[5, 1, 1, 2, 0, 0], output=[0, 0, 1, 1, 2, 5]),
        dict(nums=[1], output=[1]),
    ]
    for i, test_case in enumerate(test_cases):
        nums, required_output = test_case.values()
        output = solution(nums)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
