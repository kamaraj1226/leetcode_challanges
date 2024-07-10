# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(logs):
    depth = 0

    for log in logs:
        if log == "../":
            if depth == 0:
                continue
            depth -= 1

        elif log == "./":
            continue
        else:
            depth += 1

    return depth


def main():
    test_cases = [
        dict(logs=["d1/", "d2/", "../", "d21/", "./"], output=2),
        dict(logs=["d1/", "d2/", "./", "d3/", "../", "d31/"], output=3),
        dict(logs=["d1/", "../", "../", "../"], output=0),
        dict(logs=["./", "../", "./"], output=0),
    ]
    for i, test_case in enumerate(test_cases):
        logs, required_output = test_case.values()
        output = solution(logs)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
