# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(s):
    total = 0
    for x, y in zip(s, s[1:]):
        total += abs(ord(x) - ord(y))

    return total


def optimized(s):
    total = 0
    for i in range(len(s) - 1):
        total += abs(ord(s[i]) - ord(s[i + 1]))

    return total


def check_performance(*args):
    import timeit

    SETUP_CODE = """
from __main__ import optimized, solution
"""
    OPTIMIZED_TEST_CODE = f"""
optimized(*{args})
"""
    TEST_CODE = f"""
solution(*{args})
"""
    optimized_times = timeit.repeat(
        setup=SETUP_CODE, stmt=OPTIMIZED_TEST_CODE, repeat=5, number=10000
    )

    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=5, number=10000)

    print(
        f"optmized={sum(optimized_times)/len(optimized_times):5f}, solution={sum(times)/len(times):5f}"
    )


def main():
    test_cases = [dict(s="hello", output=13), dict(s="zaz", output=50)]
    for i, test_case in enumerate(test_cases):
        s, required_output = test_case.values()
        output = optimized(s)
        check_performance(s)
        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
