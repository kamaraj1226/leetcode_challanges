# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(s):
    number = int(s, 2)
    step = 0

    while number != 1:
        if number & 1:
            number += 1
        else:
            number //= 2
        step += 1
    return step


def main():
    test_cases = [
        dict(s="1101", output=6),
        dict(s="10", output=1),
        dict(s="1111011110000011100000110001011011110010111001010111110001", output=85),
    ]
    for i, test_case in enumerate(test_cases):
        s, required_output = test_case.values()
        output = solution(s)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
