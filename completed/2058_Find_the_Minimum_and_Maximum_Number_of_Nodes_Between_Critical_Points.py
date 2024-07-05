# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=use-dict-literal
# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel

from typing import List


# pylint: disable=redefined-builtin
# pylint: disable=too-few-public-methods
class ListNode:
    """
    Simple Node contains val and ref to next node.
    """

    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def create_link_list(head: List[int]) -> ListNode:
    nodes_list = [ListNode(val) for val in head]

    dummy: ListNode = ListNode()
    _head: ListNode = dummy
    for node in nodes_list:
        dummy.next = node
        dummy = node

    if not _head.next:
        return ListNode()

    _head: ListNode = _head.next
    return _head


def solution(head: ListNode) -> List[int]:
    pre = head
    if not head.next:
        return [-1, -1]

    cur: ListNode = head.next
    if not cur.next:
        return [-1, -1]

    positions = []
    pos = 2
    while cur.next:
        if pre.val > cur.val and cur.val < cur.next.val:
            positions.append(pos)

        if pre.val < cur.val and cur.val > cur.next.val:
            positions.append(pos)

        pre = cur
        cur = cur.next
        pos += 1

    if len(positions) < 2:
        return [-1, -1]

    max_dis = positions[-1] - positions[0]
    min_dis = float("inf")

    for x, y in zip(positions, positions[1:]):
        min_dis = min(min_dis, abs(y - x))

    min_dis = int(min_dis)
    return [min_dis, max_dis]


def main():
    test_cases = [
        dict(head=[3, 1], output=[-1, -1]),
        dict(head=[5, 3, 1, 2, 5, 1, 2], output=[1, 3]),
        dict(head=[1, 3, 2, 2, 3, 2, 2, 2, 7], output=[3, 3]),
    ]
    for i, test_case in enumerate(test_cases):
        head, required_output = test_case.values()
        head = create_link_list(head)
        output = solution(head)

        print(f"Test {i+1}: {'pass' if output== required_output else 'failed'}")


if __name__ == "__main__":
    main()
