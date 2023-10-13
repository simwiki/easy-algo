# -*- coding:utf-8 -*-
import random


def count_sort(nums):
    """
    count[num]代表num的出现次数
    nums:  [4, 2, 7, 5, 2, 6, 1, 3, 3]
            0, 1, 2, 3, 4, 5, 6, 7
    count: [0, 1, 2, 2, 1, 1, 1, 1]
    """
    m = max(nums)
    count = [0 for _ in range(m+1)]
    for i in range(len(nums)):
        count[nums[i]] += 1

    res = []
    for i in range(m+1):
        while count[i] > 0:
            res.append(i)
            count[i] -= 1
    return res

def count_sort_v2(nums):
    """
    count[num]代表num的出现次数
    nums:    [4, 2, 7, 5, 2, 6, 1, 3, 3]
              0, 1, 2, 3, 4, 5, 6, 7
    count:   [0, 1, 2, 2, 1, 1, 1, 1]
    pre_sum: [0, 1, 3, 5, 6, 7, 8, 9]
    res:     [1, 2, 2, 3, 3, 4, 5, 6, 7]
    pre_sum[i] - 1表示num出现在res中的位置
    前缀和具有明确的意义, prefix[num] - 1 代表元素 num 在结果数组 res 中最后一次出现的索引。
    """
    m = max(nums)
    count = [0 for _ in range(m+1)]
    for i in range(len(nums)):
        count[nums[i]] += 1

    for i in range(1, m+1):
        count[i] += count[i-1]

    res = [0 for _ in range(len(nums))]

    for num in nums[::-1]:
        ix = count[num] - 1
        res[ix] = num
        count[num] -= 1

    return res

nums = [random.randint(0, 10) for _ in range(20)]
print(nums)
nums = count_sort_v2(nums)
print(nums)
