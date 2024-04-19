def solution(nums, k):
    count = 0
    sub_arrays = [
        nums[i:j]
        for i in range(len(nums))
        for j in range(i, len(nums) + 1)
        if nums[i:j]
    ]

    for array in sub_arrays:
        total = 1
        for num in array:
            total *= num
        if total < k:
            count += 1
    return count


def optimized_solution(nums, k):
    if k <= 1:
        return 0
    left = 0
    right = 0
    end = len(nums)

    product = 1
    count = 0

    while right < end:
        product *= nums[right]

        while product >= k:
            product //= nums[left]
            left += 1
        count += 1 + (right - left)
        right += 1

    print(count)
    return count


nums = [10, 5, 2, 6]
k = 100
optimized_solution(nums, k)
