# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(arr1, arr2):

    from collections import Counter

    result = []

    hash_map = Counter(arr1)

    not_present = sorted(set(arr2) ^ set(hash_map.keys()))
    for val in arr2:
        result += [val] * hash_map[val]

    for val in not_present:
        result += [val] * hash_map[val]

    return result


def main():
    test_cases = [
        dict(
            arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
            arr2=[2, 1, 4, 3, 9, 6],
            output=[2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
        ),
        dict(
            arr1=[28, 6, 22, 8, 44, 17],
            arr2=[22, 28, 8, 6],
            output=[22, 28, 8, 6, 17, 44],
        ),
        dict(
            arr1=[
                2,
                21,
                43,
                38,
                0,
                42,
                33,
                7,
                24,
                13,
                12,
                27,
                12,
                24,
                5,
                23,
                29,
                48,
                30,
                31,
            ],
            arr2=[2, 42, 38, 0, 43, 21],
            output=[
                2,
                42,
                38,
                0,
                43,
                21,
                5,
                7,
                12,
                12,
                13,
                23,
                24,
                24,
                27,
                29,
                30,
                31,
                33,
                48,
            ],
        ),
    ]
    for i, test_case in enumerate(test_cases):
        arr1, arr2, required_output = test_case.values()
        output = solution(arr1, arr2)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
