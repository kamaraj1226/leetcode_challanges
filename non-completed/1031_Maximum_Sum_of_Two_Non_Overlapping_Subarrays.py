# pylint: disable=use-dict-literal
def solutiion(nums, firstLen, secondLen):

    end = len(nums)
    left = 0
    """
    maximum sun rendukum ena varum ni oru array la potute varalam
    then andha array va itterate pani find panidalam 
    """
    first_max = []
    second_max = []

    while left < end:
        first_arr = nums[left - firstLen : left]

        second_arr = nums[left - secondLen : left]

        print(first_arr, second_arr)

        left += 1


def main():
    test_cases = [
        # dict(nums=[0, 6, 5, 2, 2, 5, 1, 9, 4], firstLen=1, secondLen=2, output=20),
        dict(nums=[3, 8, 1, 3, 2, 1, 8, 9, 0], firstLen=3, secondLen=2, output=29),
        # dict(nums=[2, 1, 5, 6, 0, 9, 5, 0, 3, 8], firstLen=4, secondLen=3, output=31),
    ]

    for i, test_case in enumerate(test_cases):
        nums, firstLen, secondLen, required_output = test_case.values()
        output = solutiion(nums, firstLen, secondLen)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
