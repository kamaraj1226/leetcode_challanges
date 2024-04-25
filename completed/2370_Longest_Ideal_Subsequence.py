# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(s, k):
    d = [0] * 26

    for ch in s:
        i = ord(ch) - ord("a")
        _s, _e = max(0, i - k), min(25, i + k)

        d[i] = 1 + max(d[_s : _e + 1])
        # print(d, ch, _s, _e)

    return max(d)


def main():
    test_cases = [
        dict(s="acfgbd", k=2, output=4),
        dict(s="abcd", k=3, output=4),
        dict(s="pvjcci", k=4, output=2),
        dict(s="eduktdb", k=15, output=5),
    ]
    for i, test_case in enumerate(test_cases):
        s, k, required_output = test_case.values()
        output = solution(s, k)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
