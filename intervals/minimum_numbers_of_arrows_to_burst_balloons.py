from typing import List


def findMinArrowShots(self, points: List[List[int]]) -> int:
    points.sort(key=lambda point: point[0])

    def is_overlapped(prev_interval, next_interval) -> bool:
        print(f"overlapped?: {prev_interval}, {next_interval}")
        prev_interval, next_interval = sorted([prev_interval, next_interval], key=(lambda interval: interval[0]))
        return prev_interval[1] >= next_interval[0]

    n_arrows = 1
    prev_interval = points[0]
    for point in points[1:]:
        if is_overlapped(prev_interval, point):
            prev_interval = [max(prev_interval[0], point[0]), min(prev_interval[1], point[1])]
        else:
            n_arrows += 1
            prev_interval = point

    return n_arrows
