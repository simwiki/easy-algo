# -*- coding:utf-8 -*-
import random


def partition(nums, low, high):
    i, j = low, high
    while i < j:
        while i < j and nums[j] >= nums[low]:
            j -= 1
        while i < j and nums[i] <= nums[low]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[low] = nums[low], nums[i]
    return i


def qksort(nums, low, high):
    if low < high:
        pivot = partition(nums, low, high)
        qksort(nums, low, pivot - 1)
        qksort(nums, pivot + 1, high)


nums = [random.randint(0, 10) for _ in range(20)]
print(nums)
qksort(nums, 0, len(nums) - 1)
print(nums)
