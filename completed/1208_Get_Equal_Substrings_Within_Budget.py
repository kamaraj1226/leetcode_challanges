# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(s, t, maxCost):
    def cost(x, y):
        return abs(ord(x) - ord(y))

    i, j = 0, 0
    N = len(s)

    max_len = 0
    cur_cost = 0

    while i < N:

        x, y = s[i], t[i]
        cur_cost += cost(x, y)

        while cur_cost > maxCost:
            _x, _y = s[j], t[j]
            cur_cost -= cost(_x, _y)
            j += 1

        max_len = max(max_len, abs(i - j + 1))
        i += 1
    return max_len


def main():
    test_cases = [
        dict(s="abcd", t="bcdf", maxCost=3, output=3),
        dict(s="abcd", t="cdef", maxCost=3, output=1),
        dict(s="abcd", t="acde", maxCost=0, output=1),
        dict(s="krpgjbjjznpzdfy", t="nxargkbydxmsgby", maxCost=14, output=4),
    ]
    for i, test_case in enumerate(test_cases):
        s, t, maxCost, required_output = test_case.values()
        output = solution(s, t, maxCost)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
