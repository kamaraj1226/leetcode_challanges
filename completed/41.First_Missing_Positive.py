def solution(nums):
    maximimum_number = max(nums)  # O(n) so far: O(n)
    hash_set = set(nums)
    # print(f"{minimum_number=}, {maximimum_number=}")
    # find first min positive number
    first_small_positive = nums[0]
    for num in nums:
        if first_small_positive < 0 and num > 0:
            first_small_positive = num
        if num > 0:
            first_small_positive = min(first_small_positive, num)
    # print(first_small_positive)
    if first_small_positive < 0 or first_small_positive > 1:
        # print("got here", first_small_positive)
        return 1
    for i in range(first_small_positive + 1, maximimum_number):
        if i not in hash_set:
            return i

    return maximimum_number + 1


def optimized_solution(nums):
    maximimum_number = max(nums)

    hash_set = set(nums)
    if maximimum_number < 0:
        return 1

    for i in range(1, maximimum_number):
        if i not in hash_set:
            return i
    return maximimum_number + 1


test_cases = [
    [[3, 4, -1, 1], 2],
    [[1, 2, 0], 3],
    [[7, 8, 9, 11, 12], 1],
    [[-5], 1],
    [[-1, 4, 2, 1, 9, 10], 3],
]
# required_output = 2
for case in test_cases:
    nums, required_out = case
    output = optimized_solution(nums=nums)
    print(f"{required_out==output}: {required_out=}, {output=},  {case=}")
