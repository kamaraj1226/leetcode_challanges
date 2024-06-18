# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(difficulty, profit, worker):

    works = sorted(list(zip(difficulty, profit)))

    worker.sort()

    total = 0

    i = 0
    N = len(works)

    _max = 0
    for _worker in worker:
        while i < N and works[i][0] <= _worker:
            _max = max(_max, works[i][1])
            i += 1

        total += _max

    return total


def main():
    test_cases = [
        dict(
            difficulty=[2, 4, 6, 8, 10],
            profit=[10, 20, 30, 40, 50],
            worker=[4, 5, 6, 7],
            output=100,
        ),
        dict(
            difficulty=[85, 47, 57], profit=[24, 66, 99], worker=[40, 25, 25], output=0
        ),
        dict(
            difficulty=[13, 37, 58], profit=[4, 90, 96], worker=[34, 73, 45], output=190
        ),
        dict(
            difficulty=[68, 35, 52, 47, 86],
            profit=[67, 17, 1, 81, 3],
            worker=[92, 10, 85, 84, 82],
            output=324,
        ),
        dict(
            diff=[
                66,
                1,
                28,
                73,
                53,
                35,
                45,
                60,
                100,
                44,
                59,
                94,
                27,
                88,
                7,
                18,
                83,
                18,
                72,
                63,
            ],
            profit=[
                66,
                20,
                84,
                81,
                56,
                40,
                37,
                82,
                53,
                45,
                43,
                96,
                67,
                27,
                12,
                54,
                98,
                19,
                47,
                77,
            ],
            worker=[
                61,
                33,
                68,
                38,
                63,
                45,
                1,
                10,
                53,
                23,
                66,
                70,
                14,
                51,
                94,
                18,
                28,
                78,
                100,
                16,
            ],
            output=1392,
        ),
    ]
    for i, test_case in enumerate(test_cases):
        difficulty, profit, worker, required_output = test_case.values()
        output = solution(difficulty, profit, worker)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
