# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(s):
    def backtrack(start, path):
        if start == len(s):
            results.append(path)
            return

        for i in range(start + 1, len(s) + 1):
            if s[start:i] == s[start:i][::-1]:
                backtrack(i, path + [s[start:i]])

    results = []
    backtrack(0, [])

    return results


def main():
    test_cases = [
        dict(s="aab", output=[["a", "a", "b"], ["aa", "b"]]),
        dict(s="a", output=[["a"]]),
    ]
    for i, test_case in enumerate(test_cases):
        s, required_output = test_case.values()
        output = solution(s)

        output.sort()
        required_output.sort()

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
