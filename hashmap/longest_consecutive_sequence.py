import random
from typing import List
from decorators.timer import timer


@timer
def longestConsecutive_sorting(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    nums.sort()
    consecutive_max = 1
    consecutive_curr = 1
    for i, (prev, curr) in enumerate(zip(nums[:-1], nums[1:])):
        if curr == prev + 1:
            consecutive_curr += 1
        elif curr == prev:
            continue
        else:
            consecutive_curr = 1
        consecutive_max = max(consecutive_max, consecutive_curr)
    return consecutive_max


@timer
def longestConsecutive_hashmap(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    nums_set = set(nums)
    visited = dict()
    for num in nums_set:
        visited[num] = False
    consecutive_max = 1
    consecutive_curr = 1
    for num in nums_set:
        if visited[num] or num - 1 in nums_set:
            continue
        else:
            while num + 1 in nums_set:
                visited[num] = True
                consecutive_curr += 1
                num += 1
            consecutive_max = max(consecutive_max, consecutive_curr)
            consecutive_curr = 1
    return consecutive_max


@timer
def longestConsecutive_hashmap_not_visited(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    nums_set = set(nums)
    consecutive_max = 1
    consecutive_curr = 1
    for num in nums_set:
        if num - 1 in nums_set:
            continue
        else:
            while num + 1 in nums_set:
                consecutive_curr += 1
                num += 1
            consecutive_max = max(consecutive_max, consecutive_curr)
            consecutive_curr = 1
    return consecutive_max


arr = [random.randint(0, 10000000) for _ in range(15000000)]
print(longestConsecutive_sorting(arr))
print(longestConsecutive_hashmap(arr))
print(longestConsecutive_hashmap_not_visited(arr))
'''
longestConsecutive_sorting() execution time: 14.744300365447998
61
longestConsecutive_hashmap() execution time: 6.528353452682495
61
longestConsecutive_hashmap_not_visited() execution time: 4.734860181808472
61
'''
