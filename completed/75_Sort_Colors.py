# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(nums):
    hash_map = {0: 0, 1: 0, 2: 0}

    for num in nums:
        hash_map[num] += 1

    current = 0
    N = len(nums)
    i = 0

    while i < N:
        if hash_map[current] == 0:
            current += 1
            continue
        nums[i] = current
        hash_map[current] -= 1
        i += 1


def optimized(nums):

    low, mid = 0, 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1

    # low,mid=0,0
    # high = len(nums)-1

    # while mid<=high:
    #     if nums[mid] == 0:
    #         nums[low],nums[mid] = nums[mid],nums[low]
    #         low+=1
    #         mid+=1
    #     elif nums[mid] == 1:
    #         mid+=1
    #     else:
    #         nums[mid],nums[high] = nums[high],nums[mid]
    #         high -=1


def main():
    test_cases = [
        dict(nums=[2, 0, 2, 1, 1, 0], output=[0, 0, 1, 1, 2, 2]),
        dict(nums=[2, 0, 1], output=[0, 1, 2]),
        dict(nums=[2], output=[2]),
        dict(nums=[1, 2, 0], output=[0, 1, 2]),
    ]
    for i, test_case in enumerate(test_cases):
        nums, required_output = test_case.values()
        optimized(nums)
        output = nums

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
