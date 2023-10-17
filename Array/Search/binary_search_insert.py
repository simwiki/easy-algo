# -*- coding:utf-8 -*-


def binary_search_insert(nums, target):
    """
    若数组（包含重复元素）中已存在元素 target ，则插入到其左方。
    """
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (right - left) // 2 + left
        print(left, mid, right)

        # tatget in [left, mid-1]
        if target < nums[mid]:
            right = mid - 1
        # target in [mid+1, right]
        elif target > nums[mid]:
            left = mid + 1
        # 首个小于target in [left, mid-1]
        else:
            right = mid - 1
    return left


nums = [2, 5, 7, 7, 7, 7, 7, 9, 10, 16]
target = 7
print(binary_search_insert(nums, target))
