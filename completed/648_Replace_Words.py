# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(dictionary, sentence):

    new_string = ""
    # dictionary = ((word, len(word)) for word in dictionary)

    for word in sentence.split():
        _possible = ""
        _len = float("inf")
        for dict_word in dictionary:
            dict_word_len = len(dict_word)
            if word[:dict_word_len] == dict_word:
                if dict_word_len < _len:
                    _possible = dict_word
                    _len = dict_word_len

        if _possible:
            new_string += _possible + " "
        else:
            new_string += word + " "
    return new_string.strip()


def optimized(dictionary, sentence):

    hash_map = {}
    for word in dictionary:
        hash_map.setdefault(word[0], [])
        hash_map[word[0]].append(word)

    new_string = ""
    for word in sentence.split():
        _possible = ""
        _len = float("inf")
        if word[0] in hash_map:
            for dict_word in hash_map[word[0]]:
                dict_word_len = len(dict_word)
                if word[:dict_word_len] == dict_word:
                    if dict_word_len < _len:
                        _possible = dict_word
                        _len = dict_word_len

        if _possible:
            new_string += _possible + " "
        else:
            new_string += word + " "
    return new_string.strip()


def main():
    test_cases = [
        dict(
            dictionary=["cat", "bat", "rat"],
            sentence="the cattle was rattled by the battery",
            output="the cat was rat by the bat",
        ),
        dict(
            dictionary=["a", "b", "c"],
            sentence="aadsfasf absbs bbab cadsfafs",
            output="a a b c",
        ),
    ]
    for i, test_case in enumerate(test_cases):
        dictionary, sentence, required_output = test_case.values()
        output = optimized(dictionary, sentence)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
