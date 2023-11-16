from typing import List
from decorators.timer import timer


@timer
def summaryRanges(nums: List[int]) -> List[str]:
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return[f"{nums[0]}"]
    len_curr_range = 0
    curr_start = nums[0]
    ranges = []
    for prev, curr in zip(nums[:-1], nums[1:]):
        print(prev, curr)
        if curr == prev + 1:
            print('consecutive...')
            len_curr_range += 1
        else:
            print('not consecutive...')
            ranges.append(f'{curr_start}{f"->{prev}" if prev > curr_start else ""}')
            curr_start = curr
            len_curr_range = 0
    else:
        ranges.append(f'{curr_start}{f"->{curr}" if curr > curr_start else ""}')
    return ranges


print(summaryRanges([-1]))
