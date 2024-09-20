# https://leetcode.cn/problems/unique-paths-ii/
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。



示例 1：


输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：


输入：obstacleGrid = [[0,1],[0,0]]
输出：1


提示：

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] 为 0 或 1
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)  # 网格的行数
        n = len(obstacleGrid[0])  # 网格的列数
        # bad case
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            # 如果起点或终点有障碍物，直接返回0
            return 0

        dp = [[0] * n for _ in range(m)]  # 创建一个二维列表用于存储路径数
        # dp = [[0] * n] * m  # 该方式会邮箱内部的值不推荐
        # print(f"dp init -> {dp}, {dp1}")
        # 设置起点的路径数为1
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        # 计算第一列的路径数
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        # 计算第一行的路径数
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        # 计算其他位置的路径数
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(f"dp result  -> {dp}")
        return dp[m - 1][n - 1]  # 返回终点的路径数


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * n  # 创建一个一维列表用于存储路径数

        # 初始化第一行的路径数
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[j] = 1

        # 计算其他行的路径数
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1]

        return dp[-1]  # 返回最后一个元素，即终点的路径数


if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))
    print(Solution2().uniquePathsWithObstacles(obstacleGrid))
