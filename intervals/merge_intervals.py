from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 0:
        return []
    elif len(intervals) == 1:
        return [intervals[0]]

    def is_overlapped(prev_interval, next_interval) -> bool:
        print(f"overlapped?: {prev_interval}, {next_interval}")
        prev_interval, next_interval = sorted([prev_interval, next_interval], key=(lambda interval: interval[0]))
        return prev_interval[1] >= next_interval[0]

    def merge_intervals(prev_interval, next_interval) -> List[int] | None:
        if is_overlapped(prev_interval, next_interval):
            return [min(prev_interval[0], next_interval[0]), max(next_interval[1], prev_interval[1])]
        else:
            return None

    intervals.sort(key=(lambda interval: interval[0]))
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


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
