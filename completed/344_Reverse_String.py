# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(s):
    l, r = 0, len(s) - 1

    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1


def optimized(s):
    s[:] = s[-1::-1]


def main():
    test_cases = [
        dict(s=["h", "e", "l", "l", "o"], output=["o", "l", "l", "e", "h"]),
        dict(s=["H", "a", "n", "n", "a", "h"], output=["h", "a", "n", "n", "a", "H"]),
    ]
    for i, test_case in enumerate(test_cases):
        s, required_output = test_case.values()
        output = solution(s)
        output = s
        # print("==>", output)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
