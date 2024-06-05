# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(words):

    res = []
    for c in set(tuple(words[0])):
        _count = float("inf")
        for word in words:
            _count = min(_count, word.count(c))

        res += [c] * _count

    return res


def main():
    test_cases = [
        dict(words=["bella", "label", "roller"], output=["e", "l", "l"]),
        dict(words=["cool", "lock", "cook"], output=["c", "o"]),
    ]
    for i, test_case in enumerate(test_cases):
        words, required_output = test_case.values()
        output = solution(words)

        required_output.sort()
        output.sort()

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
