# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(word):
    def helper(_w):
        if len(_w) == 1:
            return True
        d = {}
        for i in _w:
            d.setdefault(i, 0)

            d[i] += 1

        odd = [v for k, v in d.items() if v % 2 != 0]

        if len(odd) == 1:
            return True
        return False

    def wonderful(w):
        l = len(w)
        cur_l = 0
        total = 0

        while cur_l < l:

            for i in range(l):
                if helper(w[i : i + cur_l + 1]):
                    print(w, i, cur_l, w[i : i + cur_l + 1])
                    total += 1

            cur_l += 1
        return total

    # for i in range(len(word)):
    #     for j in range(i, len(word)):
    #         print("=================")
    #         wonderful(word[i : j + 1])
    print(wonderful(word))


def main():
    test_cases = [
        dict(word="aba", output=4),
        # dict(word="aabb", output=9),
        # dict(word="he", output=2),
    ]
    for i, test_case in enumerate(test_cases):
        word, required_output = test_case.values()
        output = solution(word)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
