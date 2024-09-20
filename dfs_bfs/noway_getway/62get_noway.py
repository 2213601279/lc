# https://leetcode.cn/problems/unique-paths/description/
"""一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

示例 1：



输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 2, n = 3
输出：3
解释： 从左上角开始，总共有 3 条路径可以到达右下角。

向右 -> 向右 -> 向下
向右 -> 向下 -> 向右
向下 -> 向右 -> 向右
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6
提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10^9"""

"""
机器人从(0 , 0) 位置出发，到(m - 1, n - 1)终点。

按照动规五部曲来分析：

确定dp数组（dp table）以及下标的含义
dp[i][j] ：表示从（0 ，0）出发，到(i, j) 有dp[i][j]条不同的路径。

确定递推公式
想要求dp[i][j]，只能有两个方向来推导出来，即dp[i - 1][j] 和 dp[i][j - 1]。

此时在回顾一下 dp[i - 1][j] 表示啥，是从(0, 0)的位置到(i - 1, j)有几条路径，dp[i][j - 1]同理。

那么很自然，dp[i][j] = dp[i - 1][j] + dp[i][j - 1]，因为dp[i][j]只有这两个方向过来。

dp数组的初始化
如何初始化呢，首先dp[i][0]一定都是1，因为从(0, 0)的位置到(i, 0)的路径只有一条，那么dp[0][j]也同理。

所以初始化代码为：

for (int i = 0; i < m; i++) dp[i][0] = 1;
for (int j = 0; j < n; j++) dp[0][j] = 1;
确定遍历顺序
这里要看一下递推公式dp[i][j] = dp[i - 1][j] + dp[i][j - 1]，dp[i][j]都是从其上方和左方推导而来，那么从左到右一层一层遍历就可以了。

这样就可以保证推导dp[i][j]的时候，dp[i - 1][j] 和 dp[i][j - 1]一定是有数值的。

举例推导dp数组"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        # 设置第一行和第一列的基本情况
        # for i in range(m):
        #     dp[i][0] = 1
        # for j in range(n):
        #     dp[0][j] = 1
        print(f"dp init {dp}")
        # 计算每个单元格的唯一路径数
        for i in range(1, m):
            for j in range(1, n):
                # 只能往左下走
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(f"dp calculate {dp}")
        # 返回右下角单元格的唯一路径数
        return dp[m - 1][n - 1]


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建一个一维列表用于存储每列的唯一路径数
        dp = [1] * n
        print(f"dp init {dp}")

        # 计算每个单元格的唯一路径数
        for j in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]
        print(f"dp calculate {dp}")
        # 返回右下角单元格的唯一路径数
        return dp[n - 1]


if __name__ == '__main__':
    print(Solution().uniquePaths(m=10, n=10))
    print(Solution2().uniquePaths(m=10, n=10))
