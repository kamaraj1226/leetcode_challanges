# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
def solution(board, word):
    """
    Find first word char position
    Add position to stack
    Until stack is empty search for other words
    """

    # find first char location
    stack = []
    # stack = [(sr, sc, 0, word[0], {(sr, sc)})]
    for ri, r in enumerate(board):
        for ci, c in enumerate(r):
            if c == word[0]:
                stack.append((ri, ci, 0, word[0], {(ri, ci)}))
    final_word = ""

    def check(r, c, pos, used):
        if not 0 <= r < len(board) or not 0 <= c < len(board[0]):
            return False

        if (r, c) in used:
            return False

        return board[r][c] == word[pos]

    while len(stack) > 0:
        # print(stack)

        r, c, p, chrs, used = stack.pop(0)

        if p + 1 == len(word):
            final_word = chrs
            break
        # check left
        if check(r, c + 1, p + 1, used):
            _r = r
            _c = c + 1
            _p = p + 1
            _used = used.copy()
            _used.add((_r, _c))
            _wrd = chrs + word[p + 1]

            stack.append((_r, _c, _p, _wrd, _used))

        # check right
        if check(r, c - 1, p + 1, used):
            _r = r
            _c = c - 1
            _p = p + 1
            _used = used.copy()
            _used.add((_r, _c))
            _wrd = chrs + word[p + 1]

            stack.append((_r, _c, _p, _wrd, _used))

        # check down
        if check(r + 1, c, p + 1, used):
            _r = r + 1
            _c = c
            _p = p + 1
            _used = used.copy()
            _used.add((_r, _c))
            _wrd = chrs + word[p + 1]

            stack.append((_r, _c, _p, _wrd, _used))

        # check up
        if check(r - 1, c, p + 1, used):
            _r = r - 1
            _c = c
            _p = p + 1
            _used = used.copy()
            _used.add((_r, _c))
            _wrd = chrs + word[p + 1]

            stack.append((_r, _c, _p, _wrd, _used))

    return final_word == word


def optimized_solution(board, word):

    def backtrack(r, c, p):
        if p == len(word):
            return True

        if (
            not 0 <= r < len(board)
            or not 0 <= c < len(board[0])
            or board[r][c] != word[p]
        ):
            return False

        _temp = board[r][c]
        board[r][c] = ""

        if any(
            [
                backtrack(r, c + 1, p + 1),  # right
                backtrack(r, c - 1, p + 1),  # left
                backtrack(r + 1, c, p + 1),  # down
                backtrack(r - 1, c, p + 1),  # up
            ]
        ):
            return True

        board[r][c] = _temp
        return False

    for ri, r in enumerate(board):
        for ci, c in enumerate(r):
            if c != word[0]:
                continue
            if backtrack(ri, ci, 0):
                return True
    return False


def main():
    test_cases = [
        [
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        ],
        [
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True,
        ],
        [
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False,
        ],
    ]

    for i, test_case in enumerate(test_cases):
        board, word, required_output = test_case

        output = optimized_solution(board, word)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
