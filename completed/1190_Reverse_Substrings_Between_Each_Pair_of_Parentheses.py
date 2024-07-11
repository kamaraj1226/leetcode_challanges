# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(s: str):

    # base case if ( not in s
    # then there is no sub strings to be reversed
    # so return reversed of the string
    rp = s.find(")")
    if rp == -1:
        if s:
            return s
        return ""

    lp = None
    i = rp
    while lp is None:
        if s[i] == "(":
            lp = i
        i -= 1

    left = s[:lp]
    center = s[lp + 1 : rp]
    if center:
        center = center[::-1]
    right = s[rp + 1 :]
    res = solution(left + center + right)
    return res


def main():
    test_cases = [
        # dict(s="(abcd)", output="dcba"),
        # dict(s="(u(love)i)", output="iloveu"),
        # dict(s="(ed(et(oc))el)", output="leetcode"),
        dict(s="ta()usw((((a))))", output="tauswa"),
    ]
    for i, test_case in enumerate(test_cases):
        s, required_output = test_case.values()
        output = solution(s)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
