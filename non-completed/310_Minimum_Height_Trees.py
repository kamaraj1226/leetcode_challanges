# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


def solution(n, edges):
    from collections import deque

    tree_dict = {}

    def find_depth(node):
        queue = deque()
        queue.append((node, 1))
        visited = set()
        _depth = 0
        while queue:
            _node, depth = queue.popleft()

            visited.add(_node)

            for n in tree_dict.get(_node):
                if n == node or n in visited:
                    continue
                if depth > min_depth:
                    print(depth, min_depth)
                    break
                _depth = max(_depth, depth)
                queue.append((n, depth + 1))

        return _depth

    for edge in edges:
        _from, _to = edge
        if tree_dict.get(_from):
            tree_dict[_from].append(_to)
        else:
            tree_dict[_from] = [_to]

        if tree_dict.get(_to):
            tree_dict[_to].append(_from)
        else:
            tree_dict[_to] = [_from]

    min_depth = float("inf")
    depth_dict = {}
    for key in tree_dict:
        print("=========", key)
        depth = find_depth(key)
        if depth_dict.get(depth):
            depth_dict[depth].append(key)
        else:
            depth_dict[depth] = [key]
        min_depth = min(depth, min_depth)
        print("final: ", depth)

    if min_depth == float("inf"):
        return [0]
    return depth_dict[min_depth]


def main():
    test_cases = [
        dict(n=4, edges=[[1, 0], [1, 2], [1, 3]], output=[1]),
        # dict(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]], output=[3, 4]),
    ]
    for i, test_case in enumerate(test_cases):
        n, edges, required_output = test_case.values()
        output = solution(n, edges)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
