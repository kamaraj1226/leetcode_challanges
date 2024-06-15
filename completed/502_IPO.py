# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(k, w, profits, capital):

    import heapq

    projects = list(zip(capital, profits))
    projects.sort()
    N = len(capital)

    maxHeap = []
    i = 0
    for _ in range(k):
        while i < N and projects[i][0] <= w:
            heapq.heappush(maxHeap, -projects[i][1])
            i += 1

        if not maxHeap:
            break
        w -= heapq.heappop(maxHeap)
    return w


def main():
    test_cases = [
        dict(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1], output=4),
        dict(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2], output=6),
    ]
    for i, test_case in enumerate(test_cases):
        k, w, profits, capital, required_output = test_case.values()
        output = solution(k, w, profits, capital)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
