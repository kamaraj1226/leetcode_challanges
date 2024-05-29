# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(s: str, word_dict):
    # for word in word_dict:
    #     print(word, s.find(word))
    word_dict = set(word_dict)
    i = 0

    end = len(s)

    while i < end:
        word = s[:i]
        if word in word_dict:
            print(word, s.find(word))
        i += 1

    return []


def main():
    test_cases = [
        dict(
            s="catsanddog",
            wordDict=["cat", "cats", "and", "sand", "dog"],
            output=["cats and dog", "cat sand dog"],
        ),
        # dict(
        #     s="pineapplepenapple",
        #     wordDict=["apple", "pen", "applepen", "pine", "pineapple"],
        #     output=[
        #         "pine apple pen apple",
        #         "pineapple pen apple",
        #         "pine applepen apple",
        #     ],
        # ),
    ]
    for i, test_case in enumerate(test_cases):
        s, word_dict, required_output = test_case.values()
        output = solution(s, word_dict)

        required_output.sort()
        output.sort()

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
