# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(n):

    if n == 0:
        return 0

    if n in (1, 2):
        return 1

    d = {}
    d[0] = 0
    d[1] = 1
    d[2] = 1

    for i in range(3, n + 1):
        d[i] = d[i - 3] + d[i - 2] + d[i - 1]

    return d[n]


def recursive_solution(n):
    def recursive(n, d={0: 0, 1: 1, 2: 1}):
        if n < 0:
            return 0

        if n in d:
            return d[n]

        if d is not None and n in d:
            return d[n]

        val1 = recursive(n - 1, d)
        val2 = recursive(n - 2, d)
        val3 = recursive(n - 3, d)
        d[n - 1] = val1
        d[n - 2] = val2
        d[n - 3] = val3
        d[n] = val1 + val2 + val3
        return d[n]

    return recursive(n)


def main():
    test_cases = [dict(n=4, output=4), dict(n=25, output=1389537)]
    for i, test_case in enumerate(test_cases):
        n, required_output = test_case.values()
        output = recursive_solution(n)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
