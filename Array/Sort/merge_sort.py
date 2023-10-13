# -*- coding:utf-8 -*-
import random


def merge(nums_left, nums_right):
    res = []
    i, j = 0, 0
    while i < len(nums_left) and j < len(nums_right):
        if nums_left[i] <= nums_right[j]:
            res.append(nums_left[i])
            i += 1
        else:
            res.append(nums_right[j])
            j += 1
    while i < len(nums_left):
        res.append(nums_left[i])
        i += 1
    while j < len(nums_right):
        res.append(nums_right[j])
        j += 1
    return res

def mergesort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    nums_left = mergesort(nums[:mid])
    nums_right = mergesort(nums[mid:])
    return merge(nums_left, nums_right)


nums = [random.randint(0, 10) for _ in range(20)]
print(nums)
nums = mergesort(nums)
print(nums)


