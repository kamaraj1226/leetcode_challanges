# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name


def solution(divisor1, divisor2, uniqueCnt1, uniqueCnt2):

    def get_array(_len, divisor):
        arr_len = 0
        arr = []
        i = 0
        while arr_len < _len:

            if i % divisor != 0:
                arr.append(i)
                arr_len += 1
            i += 1
        return arr

    arr1 = get_array(uniqueCnt1 + uniqueCnt2, divisor1)
    arr2 = get_array(uniqueCnt1 + uniqueCnt2, divisor2)
    print(arr1)
    print(arr2)


def main():
    test_cases = [
        dict(divisor1=2, divisor2=7, uniqueCnt1=1, uniqueCnt2=3, output=4),
        # dict(divisor1=3, divisor2=5, uniqueCnt1=2, uniqueCnt2=1, output=3),
        # dict(divisor1=2, divisor2=4, uniqueCnt1=8, uniqueCnt2=2, output=15),
    ]
    for i, test_case in enumerate(test_cases):
        divisor1, divisor2, uniqueCnt1, uniqueCnt2, required_output = test_case.values()
        output = solution(divisor1, divisor2, uniqueCnt1, uniqueCnt2)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
