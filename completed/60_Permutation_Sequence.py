# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(n, k):
    from itertools import permutations

    for j, p in enumerate(permutations([str(i) for i in range(1, n + 1)])):
        if j == k - 1:
            return "".join(p)


def main():
    test_cases = [
        dict(n=3, k=3, output="213"),
        dict(n=4, k=9, output="2314"),
        dict(n=3, k=1, output="123"),
    ]
    for i, test_case in enumerate(test_cases):
        n, k, required_output = test_case.values()
        output = solution(n, k)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
