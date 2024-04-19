def solution(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False
    hash_set = set()
    print(s)
    for idx, ch in enumerate(t):
        if ch not in hash_set:
            s = s.replace(s[idx], ch)
            print(s)
            hash_set.add(ch)

    if s == t:
        return True

    return False


def main():
    # [s <str>, t <str>, result <bool>]
    test_cases = [
        # ["egg", "add", True],
        # ["foo", "bar", False],
        # ["paper", "title", True],
        ["egcd", "adfd", False],
    ]

    for i, test_case in enumerate(test_cases):
        s, t, required_output = test_case

        output = solution(s, t)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
