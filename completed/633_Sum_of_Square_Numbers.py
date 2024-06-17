# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def another_solution(c):
    import math

    _c = int(math.sqrt(c))

    for a in range(_c + 1):
        b = math.sqrt(c - a * a)

        if b.is_integer():
            return True
    return False


def solution(c):

    import math

    r = int(math.sqrt(c))
    l = 0

    while l <= r:
        _t = l * l + r * r
        if _t == c:
            return True

        if _t > c:
            r -= 1
        else:
            l += 1

    return False


def main():
    test_cases = [
        dict(c=5, output=True),
        dict(c=3, output=False),
        dict(c=4, output=True),
        dict(c=6, output=False),
        dict(c=1000, output=True),
    ]
    for i, test_case in enumerate(test_cases):
        c, required_output = test_case.values()
        output = another_solution(c)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
