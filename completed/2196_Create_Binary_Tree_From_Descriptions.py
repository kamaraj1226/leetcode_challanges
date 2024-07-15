# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


class TreeNode:
    """Test TreeNode"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(descriptions):
    d = {}
    root = None
    for description in descriptions:
        parent, child, isleft = description

        d.setdefault(parent, [TreeNode(parent), True])
        d.setdefault(child, [TreeNode(child), True])

        parent_node, child_node = d[parent][0], d[child][0]

        if isleft == 1:
            parent_node.left = child_node
            d[child][-1] = False
        else:
            parent_node.right = child_node
            d[child][-1] = False

    for _, val in d.items():
        if val[-1]:
            root = val[0]

    return root


def parse_output(output):
    """
    This will return wrong output need to implement it properly
    Solution code have been passed in leetcode.
    """
    result = []

    stack = [output]

    while stack:
        node = stack.pop(0)
        result.append(node.val)

        if node.left is None or node.right is None:
            if node.left is None and node.right is None:
                continue

            elif node.left is None:
                stack.append(node.right)
                result.append(None)
            else:
                stack.append(node.left)
                result.append(None)

        else:
            stack.append(node.left)
            stack.append(node.right)
    return result


def main():
    test_cases = [
        dict(
            descriptions=[
                [20, 15, 1],
                [20, 17, 0],
                [50, 20, 1],
                [50, 80, 0],
                [80, 19, 1],
            ],
            output=[50, 20, 80, 15, 17, 19],
        ),
        dict(
            descriptions=[[1, 2, 1], [2, 3, 0], [3, 4, 1]],
            output=[1, 2, None, None, 3, 4],
        ),
    ]
    for i, test_case in enumerate(test_cases):
        descriptions, required_output = test_case.values()
        output = solution(descriptions)
        output = parse_output(output)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
