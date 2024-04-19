# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

template_string = """
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name


def solution(): ...


def main():
    test_cases = [
        dict()
    ]
    for i, test_case in enumerate(test_cases):
        required_output = test_case.values()
        output = solution()

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")

if __name__ == "__main__":
    main()
"""


def main():
    _file = input("File Name: ")

    with open(_file, "w", encoding="utf-8") as file:
        file.write(template_string)


if __name__ == "__main__":
    main()
