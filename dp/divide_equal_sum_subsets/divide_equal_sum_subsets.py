"""
题目难易：中等

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意: 每个数组中的元素不会超过 100 数组的大小不会超过 200

示例 1:

输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
示例 2:

输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100
#算法公开课
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # base case
        if sum(nums) % 2 != 0:
            return False
        # 利用题目的特性
        target = sum(nums) // 2

        dp = [0] * (target + 1)
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = max(dp[j], dp[j-num] + num)
        return dp[-1] == target


if __name__ == '__main__':
    a = [1, 5, 6]
    print(Solution().canPartition(a))