from typing import List


def candy_two_pass_greedy(ratings: List[int]) -> int:
    candies = [1] * len(ratings)
    for i in range(1, len(ratings)):
        candies[i] = candies[i - 1] + 1 if ratings[i] > ratings[i - 1] else 1

    for i in range(len(ratings) - 2, -1, -1):
        candies[i] = max(candies[i], candies[i + 1] + 1) if ratings[i] > ratings[i + 1] else candies[i]

    print(candies)
    return sum(candies)


def candy_one_pass_greedy(ratings: list[int]) -> int:
    if not ratings:
        return 0
    '''
        up: count numbers of increasing -> if prev < curr then current candies increase by "the level of up" to 
        flat the candies (if the more increasing the more candies need to be added) and plus 1 to meet the requirement
        of the problem -> cnt += 1 + up
        
        peak: go up with 'up' but it is used to save the last rating reaching at peak. peak = 0 when having two 
        consecutive equal numbers -> can go up from 1 again -> cnt += 1
        
        down: count numbers of decreasing -> if prev > curr then previous candies increase by "the level of down" to 
        flat the candies (if the more decreasing the more candies need to be added) and plus 1 to meet the requirement
        of the problem -> cnt -= 1 + down. But if the peak is still higher than or equal to the down, then the peak has 
        its own candies and it don't need to plus 1 candies to flat -> cnt -= 1
    '''
    up, down, peak, cnt = 0, 0, 0, 1
    for prev, curr in zip(ratings[:-1], ratings[1:]):

        if prev < curr:
            up, down, peak = up + 1, 0, peak + 1
            cnt += 1 + up
            print(f'prev:{prev} < curr:{curr}, (up={up},down={down},peak={peak},cnt=cnt+(1+up)={cnt})')
        elif prev == curr:
            up, down, peak = 0, 0, 0
            cnt += 1
            print(f'prev:{prev} == curr:{curr}, (up={up},down={down},peak={peak},cnt=cnt+1={cnt})')
        else:
            up, down = 0, down + 1
            cnt += 1 + down
            print(f'prev:{prev} > curr:{curr}, (up={up},down={down},peak={peak},cnt=cnt+(1+down)={cnt})', end='')
            if peak >= down:
                cnt -= 1
                print(f'peak >= down => cnt=cnt-1={cnt}')
            else:
                print('')
    return cnt


if __name__ == '__main__':
    ratings = [2, 4, 4, 2, 1, 3, 5, 6, 9, 3, 6]
    print(f'ratings: {ratings}')
    print(candy_two_pass_greedy(ratings))
    print(candy_one_pass_greedy(ratings))
