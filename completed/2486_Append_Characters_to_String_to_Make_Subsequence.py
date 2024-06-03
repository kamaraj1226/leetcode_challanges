# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(s, t):

    i = 0
    N = len(t)

    for ch in s:
        if i < N and ch == t[i]:
            i += 1
    return N - i


def main():
    test_cases = [
        dict(s="coaching", t="coding", output=4),
        dict(s="abcde", t="a", output=0),
        dict(s="z", t="abcde", output=5),
        dict(s="lbg", t="g", output=0),
        dict(s="vrykt", t="rkge", output=2),
    ]
    for i, test_case in enumerate(test_cases):
        s, t, required_output = test_case.values()
        output = solution(s, t)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
