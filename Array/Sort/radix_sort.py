# -*- coding:utf-8 -*-
import random


def count_sort(nums, exp):
    n = len(nums)
    count = [0] * 10
    for num in nums:
        # 取出num的第k位, 记为d
        d = (num // exp ) % 10
        count[d] += 1

    # 前缀和, 将“出现个数”转换为“数组索引”
    for i in  range(1, 10):
        count[i] += count[i-1]

    # 倒序赋值
    res = [0] * n
    for i in range(n-1, -1, -1):
        d = (nums[i] // exp ) % 10
        ix = count[d] - 1
        res[ix] = nums[i]
        count[d] -= 1

    # 覆盖nums
    for i in range(n):
        nums[i] = res[i]


def radix_sort(nums):
    """
    从低位到高位执行计数排序
    """
    m = max(nums)
    exp = 1
    while exp < m:
        count_sort(nums, exp)
        exp *= 10
    return nums


nums = [random.randint(10**2, 10**6) for _ in range(20)]
print(nums)
nums = radix_sort(nums)
print(nums)
