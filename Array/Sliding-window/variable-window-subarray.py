# -*- coding:utf-8 -*-
""" 不定长度滑动窗口代码模板
left = 0
right = 0

while right < len(nums):
    window.append(nums[right])
    
    while 窗口需要缩小:
        # ... 可维护答案
        window.popleft()
        left += 1
    
    # 向右侧增大窗口
    right += 1
"""


# - [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
def longest_substr_len(s):
    n = len(s)
    left, right = 0, 0
    windows = set()
    res = 0
    while right < n:
        windows.add(s[right])
        while len(windows) > 0 and len(windows) < right - left + 1:
            windows.pop()
            left += 1
        res = max(res, len(windows))
        right += 1
    return res


def longest_substr_len_v2(s):
    left = 0
    right = 0
    window = dict()
    ans = 0

    while right < len(s):
        if s[right] not in window:
            window[s[right]] = 1
        else:
            window[s[right]] += 1

        while window[s[right]] > 1:
            window[s[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)
        right += 1

    return ans

s = "abcabcbb"
print(longest_substr_len_v2(s))


# - [209. 长度最小的子数组）](https://leetcode.cn/problems/minimum-size-subarray-sum/)
def min_subarray_len(nums, target):
    n = len(nums)
    left, right = 0, 0
    windows_sum = 0
    res = n
    while right < n:
        windows_sum += nums[right]
        while windows_sum > target:
            windows_sum -= nums[left]
            left += 1
        if windows_sum == target:
            res = min(res, right - left + 1)
        right += 1
    return res if res != n else 0


def min_subarray_len_v2(nums, target):
    size = len(nums)
    ans = size + 1
    left = 0
    right = 0
    window_sum = 0

    while right < size:
        window_sum += nums[right]

        while window_sum >= target:
            ans = min(ans, right - left + 1)
            window_sum -= nums[left]
            left += 1

        right += 1

    return ans if ans != size + 1 else 0


nums = [2,3,1,2,4,3]
target = 7
print(min_subarray_len(nums, target))

