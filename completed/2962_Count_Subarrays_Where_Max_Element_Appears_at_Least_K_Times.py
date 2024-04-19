def solution(nums, k):
    sub_arr_count = 0
    max_element = max(nums)
    hash_map = {}
    left, right, end = 0, 0, len(nums)

    print(max_element)
    while right < end:
        print(sub_arr_count)
        num = nums[right]

        hash_map.setdefault(num, 0)
        hash_map[num] += 1
        if hash_map.get(max_element, 0) >= k:
            _left = left
            while _left < right and hash_map.get(max_element, 0) >= k:
                _num = nums[_left]
                # print(_num)
                sub_arr_count += 1

                print(nums[_left : right + 1])
                hash_map[_num] = hash_map[_num] - 1 if hash_map[_num] > 0 else 0
                _left += 1

            # pylint: disable=pointless-string-statement
            """
            When the inner while is over left pointer will be one step ahead
            i.e we missed so far sub array which containes maximum element at least k times. 
            """
            _left -= 1
            hash_map[nums[_left]] += 1

            # sub_arr_count += 1
        right += 1
    print(sub_arr_count)
    return sub_arr_count


def optimized_solution(nums, k):
    max_element = max(nums)

    left, right, end = 0, 0, len(nums)
    count = 0
    while right < end:

        num = nums[right]

        if num == max_element:
            k -= 1
        # print(k)
        while k == 0:
            _num = nums[left]
            # print(nums[left : right + 1])

            if _num == max_element:
                k += 1
            left += 1

        count += left
        # print(left)
        right += 1
    return count
    # mx, ans, l, r, n = max(nums), 0, 0, 0, len(nums)
    # while r < n:
    #     k -= nums[r] == mx
    #     r += 1
    #     while k == 0:
    #         print(nums[l : r + 1], k)
    #         k += nums[l] == mx
    #         l += 1
    #     ans += l
    #     print(l)
    # return ans


if __name__ == "__main__":

    test_cases = [
        [[1, 3, 2, 3, 3], 2, 6],
        # [[1, 4, 2, 1], 3, 0],
        # [
        #     [
        #         61,
        #         23,
        #         38,
        #         23,
        #         56,
        #         40,
        #         82,
        #         56,
        #         82,
        #         82,
        #         82,
        #         70,
        #         8,
        #         69,
        #         8,
        #         7,
        #         19,
        #         14,
        #         58,
        #         42,
        #         82,
        #         10,
        #         82,
        #         78,
        #         15,
        #         82,
        #     ],
        #     2,
        #     224,
        # ],
    ]

    for i, test_case in enumerate(test_cases):
        nums, k, required_output = test_case
        output = optimized_solution(nums=nums, k=k)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")

    def get_test_case():
        import sys

        TEST_CASE_DIR = "./test_cases/"
        file_name = sys.argv[0].split("/")[-1]
        test_case_file_name = file_name[:-2] + "txt"

        with open(TEST_CASE_DIR + test_case_file_name, "r", encoding="utf-8") as file:
            # print(file.readlines())
            for line in file.readlines():
                if line[-1] == "\n":
                    line = line[:-1]
                nums = line[: line.find("]") + 1]
                line = line[line.find("]") + 1 :]
                print(line.split(", "))
                k = list(map(lambda x: x.strip(), line.split(", ")))

                print(nums, k)
