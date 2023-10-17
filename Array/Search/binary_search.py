# -*- coding:utf-8 -*-


def binary_search(nums, target):
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (right - left) // 2 + left
        print(left, mid, right)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [2, 5, 7, 9, 10, 16]
target = 16
print(binary_search(nums, target))
