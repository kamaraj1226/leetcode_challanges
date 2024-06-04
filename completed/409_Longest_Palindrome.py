# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(s):
    visited = set()
    total = 0
    for c in s:
        if c in visited:
            total += 2
            visited.remove(c)
        else:
            visited.add(c)

    if visited:
        return total + 1
    return total


def main():
    test_cases = [dict(s="abccccdd", output=7), dict(s="a", output=1)]
    for i, test_case in enumerate(test_cases):
        s, required_output = test_case.values()
        output = solution(s)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
