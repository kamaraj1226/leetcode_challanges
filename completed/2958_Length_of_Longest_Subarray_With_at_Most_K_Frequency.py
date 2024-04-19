def solution(nums, k):

    if len(nums) <= 1:
        return 1

    frequency = {}

    left, right = 0, 0
    end = len(nums)
    max_longest = 0

    while right < end:
        num = nums[right]
        frequency.setdefault(num, 0)
        frequency[num] += 1

        while frequency[num] > k and left < right:

            current_longest = right - left
            left_num = nums[left]
            frequency[left_num] -= 1
            max_longest = max(current_longest, max_longest)
            left += 1

        right += 1

    return (
        max_longest
        if max_longest > 0 and (right - left) < max_longest
        else right - left
    )


# format [nums, k, output]
test_cases = [
    [[1, 2, 3, 1, 2, 3, 1, 2], 2, 6],
    [[1, 2, 1, 2, 1, 2, 1, 2], 1, 2],
    [[5, 5, 5, 5, 5, 5, 5], 4, 4],
    [[1], 1, 1],
    [[1, 11], 2, 2],
    [[2, 2, 3], 1, 2],
]

for i, test_case in enumerate(test_cases):
    nums, k, required_output = test_case
    output = solution(nums=nums, k=k)

    print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")
