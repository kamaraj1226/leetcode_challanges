def worst_solution(nums, k):

    def isValid(arr):
        hash_map = {}

        for num in arr:
            hash_map.setdefault(num, 0)
            hash_map[num] += 1

            if len(hash_map) == k:
                print("==========> ", hash_map)
                return True
        return False

    for _i in range(len(nums)):
        for _j in range(_i, len(nums) + 1):
            if _i == _j:
                continue

            if isValid(nums[_i:_j]):
                print(f"{nums[_i:_j]}")


def solution(nums, k):

    left, right, total, end = 0, 0, 0, len(nums)

    hash_set = set()

    while right < end:
        num = nums[right]

        if num not in hash_set and len(hash_set) < k:
            hash_set.add(num)
            print(f"{nums[left:right+1]}, {hash_set=}")
        else:
            while len(hash_set) >= k:
                print(f"==>{nums[left:right+1]}, {hash_set=}")
                hash_set.remove(nums[left])

                left += 1
        # print(f"{left=}, {total=}")

        if k == len(hash_set):
            total += 1
            print(f"{left=}")
        right += 1
    print(total)
    return total


if __name__ == "__main__":
    test_cases = [
        [[1, 2, 1, 2, 3], 2, 7],
        # [[1, 2, 1, 3, 4], 3, 3]
    ]

    for i, test_case in enumerate(test_cases):
        nums, k, required_output = test_case
        output = worst_solution(nums=nums, k=k)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")
