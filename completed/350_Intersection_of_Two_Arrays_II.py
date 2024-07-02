# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(nums1, nums2):
    from collections import Counter

    nums1 = Counter(nums1)
    nums2 = Counter(nums2)

    res = []

    for key, val in nums1.items():
        if nums2.get(key, None):
            times = min(nums2[key], val)
            res += [key] * times

    return res


def main():
    test_cases = [
        dict(nums1=[1, 2, 2, 1], nums2=[2, 2], output=[2, 2]),
        dict(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4], output=[4, 9]),
    ]
    for i, test_case in enumerate(test_cases):
        nums1, nums2, required_output = test_case.values()
        output = solution(nums1, nums2)
        required_output.sort()
        output.sort()
        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
