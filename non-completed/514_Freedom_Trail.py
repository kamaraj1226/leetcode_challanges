# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(ring, key):
    from functools import cache

    def recursive(ki, ri=0):

        find_all = lambda x: [(i, v) for i, v in enumerate(ring) if v == x]

    return recursive(0)


def main():
    test_cases = [
        # dict(ring="godding", key="gd", output=4),
        # dict(ring="godding", key="godding", output=13),
        dict(
            ring="caotmcaataijjxi",
            key="oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx",
            output=137,
        ),
    ]
    for i, test_case in enumerate(test_cases):
        ring, key, required_output = test_case.values()
        output = solution(ring, key)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
