# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(nums, n):
    missing = 1
    patch = 0
    i =0
    N = len(nums)
    
    while missing <= n:
        if i < N and nums[i] <= missing:
            missing += nums[i]
            i += 1
        else:
            missing += missing
            patch += 1
    return patch
    


def main():
    test_cases = [
        dict(nums=[1, 3], n=6, output=1),
        dict(nums=[1, 5, 10], n=20, output=2),
        dict(nums=[1, 2, 2], n=5, output=0),
        dict(nums=[1, 2, 31, 33], n=2147483647, output=28)
    ]
    for i, test_case in enumerate(test_cases):
        nums, n, required_output = test_case.values()
        output = solution(nums, n)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
