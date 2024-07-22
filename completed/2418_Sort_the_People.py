# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(names, heights):
    return [
        val[1] for val in sorted(zip(heights, names), key=lambda x: x[0], reverse=True)
    ]


def main():
    test_cases = [
        dict(
            names=["Mary", "John", "Emma"],
            heights=[180, 165, 170],
            output=["Mary", "Emma", "John"],
        ),
        dict(
            names=["Alice", "Bob", "Bob"],
            heights=[155, 185, 150],
            output=["Bob", "Alice", "Bob"],
        ),
    ]
    for i, test_case in enumerate(test_cases):
        names, heights, required_output = test_case.values()
        output = solution(names, heights)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
