# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel
# pylint: disable=unused-argument


def solution(n, edges, source, destination):
    from collections import deque

    def generate_hash_map(edges):
        hash_map = {}

        for edge in edges:
            _from, _to = edge

            if not hash_map.get(_from):
                hash_map[_from] = [_to]
            else:
                hash_map[_from].append(_to)

            if not hash_map.get(_to):
                hash_map[_to] = [_from]
            else:
                hash_map[_to].append(_from)
        return hash_map

    if not edges and source == destination:
        return True

    hash_map = generate_hash_map(edges)

    if not hash_map.get(source):
        return False

    stack = deque(hash_map.get(source))
    visited = set()
    while len(stack) > 0:
        vertex = stack.pop()
        if vertex == destination:
            return True

        vertices = hash_map.get(vertex)
        if vertices is None:
            continue

        for vertex in vertices:
            if vertex in visited:
                continue
            stack.append(vertex)
            visited.add(vertex)

    return False


def main():
    test_cases = [
        dict(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2, output=True),
        dict(
            n=6,
            edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]],
            source=0,
            destination=5,
            output=False,
        ),
        dict(n=1, edges=[], source=0, destination=0, output=True),
        dict(
            n=10,
            edges=[
                [0, 7],
                [0, 8],
                [6, 1],
                [2, 0],
                [0, 4],
                [5, 8],
                [4, 7],
                [1, 3],
                [3, 5],
                [6, 5],
            ],
            source=7,
            destination=5,
            output=True,
        ),
    ]
    for i, test_case in enumerate(test_cases):
        n, edges, source, destination, required_output = test_case.values()
        output = solution(n, edges, source, destination)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
