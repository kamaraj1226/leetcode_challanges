# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(deadends, target):
    from collections import deque

    if "0000" in deadends:
        return -1

    deadends = set(deadends)

    combination = "0000"

    queue = deque()
    queue.append((combination, 0))
    visited = set()

    while queue:
        comb, move = queue.popleft()
        # print(comb, move)

        if comb == target:
            return move

        for i, v in enumerate(comb):
            for delta in [-1, 1]:
                new_combination = comb[:i] + str((int(v) + delta) % 10) + comb[i + 1 :]

                if new_combination not in visited and new_combination not in deadends:
                    visited.add(new_combination)
                    queue.append((new_combination, move + 1))
    return -1


def main():
    test_cases = [
        dict(
            deadends=["0201", "0101", "0102", "1212", "2002"], target="0202", output=6
        ),
        dict(deadends=["8888"], target="0009", output=1),
        dict(
            deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
            target="8888",
            output=-1,
        ),
    ]
    for i, test_case in enumerate(test_cases):
        deadends, target, required_output = test_case.values()
        output = solution(deadends, target)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
