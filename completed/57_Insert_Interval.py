"""
57 Insert Interval

##########################
# Solution By: Kamaraj J #
##########################
"""

# pylint: disable=use-dict-literal
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name


from typing import List


class Solution:
    """Solution Class"""

    def optimized_insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """Optimized solution"""

        if not intervals:
            return [newInterval]

        _start, _end = newInterval

        # In case if newInterval should come first
        # if intervals[0][0] < _end:
        merged_interval = []

        i = 0

        # intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        # newInterval=[4, 8],
        # output=[[1, 2], [3, 10], [12, 16]],

        # all the intervals less than the new one is been appended
        while i < len(intervals):
            _s, _e = intervals[i]

            if _e >= _start:
                break

            if _s < _start < _e:
                merged_interval.append([_s, _e])
            i += 1

        # Merge should take place
        # new_start = min(_s, _start)
        # new_end = _end

        # while i < len(intervals):
        #     _s, _e = intervals[i]

        #     if _s >= _end:
        #         new_end = max(_end, _e)
        #         i += 1
        #         break
        #     i += 1

        # merged_interval.append([new_start, new_end])

        print(merged_interval)
        return merged_interval

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        "Insert new interval in intervals lsit"
        if not intervals:
            return [newInterval]

        _start, _end = newInterval

        merged_interval = []
        need_to_merge = [
            interval
            for interval in intervals
            if interval[1] >= _start and interval[0] <= _end
        ]

        if need_to_merge:
            newInterval = [
                min(_start, need_to_merge[0][0]),
                max(_end, need_to_merge[-1][-1]),
            ]
        need_to_insert = True
        for interval in intervals:
            if interval not in need_to_merge:
                merged_interval.append(interval)
            else:
                if need_to_insert:
                    merged_interval.append(newInterval)
                    need_to_insert = False

        if need_to_insert:
            merged_interval.append(newInterval)
            merged_interval.sort()
        return merged_interval


def run_test():
    """
    Test cases
    """
    test_cases = {
        1: dict(
            intervals=[[1, 3], [6, 9]], newInterval=[2, 5], output=[[1, 5], [6, 9]]
        ),
        2: dict(
            intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            newInterval=[4, 8],
            output=[[1, 2], [3, 10], [12, 16]],
        ),
        3: dict(intervals=[[1, 5]], newInterval=[6, 8], output=[[1, 5], [6, 8]]),
        4: dict(intervals=[[1, 5]], newInterval=[0, 0], output=[[0, 0], [1, 5]]),
    }

    for test_case in test_cases:
        intervals, newInterval, output = test_cases.get(
            test_case, dict(intervals=[], newInterval=[], output=[])
        ).values()
        solution = Solution()
        final_output = solution.optimized_insert(intervals, newInterval)
        if output == final_output:
            print(f"Test case: {test_case} Passed")
        else:
            print(f"Test case: {test_case} Failed")


if __name__ == "__main__":
    run_test()
