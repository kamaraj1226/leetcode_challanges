def solution(s):
    open_parenthesis = 0
    max_depth = 0
    for ch in s:
        if ch == "(":
            open_parenthesis += 1
        if ch == ")":
            open_parenthesis -= 1

        max_depth = max(open_parenthesis, max_depth)

    return max_depth


def main():
    test_cases = [["(1+(2*3)+((8)/4))+1", 3], ["(1)+((2))+(((3)))", 3]]

    for i, test_case in enumerate(test_cases):
        s, required_output = test_case

        output = solution(s)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
