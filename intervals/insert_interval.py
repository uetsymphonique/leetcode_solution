from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    def is_overlapped(prev_interval, next_interval) -> bool:
        # print(f"overlapped?: {prev_interval}, {next_interval}")
        prev_interval, next_interval = sorted([prev_interval, next_interval], key=(lambda interval: interval[0]))
        return prev_interval[1] >= next_interval[0]

    def merge_intervals(prev_interval, next_interval) -> List[int] | None:
        if is_overlapped(prev_interval, next_interval):
            return [min(prev_interval[0], next_interval[0]), max(next_interval[1], prev_interval[1])]
        else:
            return None

    if len(intervals) == 0:
        return []
    # elif len(intervals) == 1:
    #     return [merge_intervals(intervals[0], new_interval)] or sorted([intervals[0], new_interval],
    #                                                                  key=(lambda interval: interval[0]))

    for i, interval in enumerate(intervals):
        if new_interval[0] <= interval[0]:
            intervals.insert(i, new_interval)
            break
    else:
        intervals.append(new_interval)

    prev_interval = intervals[0]
    merged_intervals = []

    for interval in intervals[1:]:
        if is_overlapped(prev_interval, interval):
            prev_interval = merge_intervals(prev_interval, interval)
            print(f'{prev_interval}')
        else:
            merged_intervals.append(prev_interval)
            prev_interval = interval
    else:
        merged_intervals.append(prev_interval)

    return merged_intervals


# print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(insert([[1, 2]], [5, 6]))
