# -*- coding:utf-8 -*-
""" 固定长度滑动窗口代码模板
left = 0
right = 0

while right < len(nums):
    window.append(nums[right])
    
    # 超过窗口大小时，缩小窗口，维护窗口中始终为 window_size 的长度
    if right - left + 1 >= window_size:
        # ... 维护答案
        window.popleft()
        left += 1
    
    # 向右侧增大窗口
    right += 1
"""


# [1343. 大小为 K 且平均值大于等于阈值的子数组数目](https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)
def find_subarry_nums(nums, k, threshold):
    n = len(nums)
    left, right = 0, 0
    windows = []
    res = 0
    while right < n:
        while len(windows) < k:
            windows.append(nums[right])
            right += 1
        avg = sum(windows) / k
        if avg >= threshold:
            res += 1
        windows.pop(0)
        left += 1
    return res


def find_subarry_nums_v2(nums, k, threshold):
    n = len(nums)
    left, right = 0, 0
    windows_sum = 0
    res = 0
    while right < n:
        windows_sum += nums[right]
        if right - left + 1 >= k:
            if windows_sum >= k * threshold:
                res += 1
            windows_sum -= nums[left]
            left += 1

        right += 1
    return res




nums = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

# 返回长度为 $k$ 且平均值大于等于 $threshold$ 的子数组数目。
# 子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 。

print(find_subarry_nums_v2(nums, k, threshold))
