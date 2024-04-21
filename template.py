# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

import argparse

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


def main(file_name):
    # _file = input("File Name: ")

    _file = file_name.strip().replace(".", "").replace(" ", "_") + ".py"

    with open(_file, "w", encoding="utf-8") as file:
        file.write(template_string)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", action="store", required=True, help="file name")
    args = parser.parse_args()
    main(args.name)
