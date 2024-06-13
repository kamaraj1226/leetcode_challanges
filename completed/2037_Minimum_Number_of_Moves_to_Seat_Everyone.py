# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(seats, students):
    seats.sort()
    students.sort()
    total = 0
    for x, y in zip(seats, students):
        total += abs(x - y)

    return total


def main():
    test_cases = [
        dict(seats=[3, 1, 5], students=[2, 7, 4], output=4),
        dict(seats=[4, 1, 5, 9], students=[1, 3, 2, 6], output=7),
        dict(seats=[2, 2, 6, 6], students=[1, 3, 2, 6], output=4),
    ]
    for i, test_case in enumerate(test_cases):
        seats, students, required_output = test_case.values()
        output = solution(seats, students)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
