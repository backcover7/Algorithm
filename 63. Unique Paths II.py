class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        dp = [[0]*(m+1) for _ in xrange(n+1)]
        if obstacleGrid[0][0] != 1: dp[1][1] = 1
        for y in xrange(1, n+1):
            for x in xrange(1, m+1):
                if obstacleGrid[y - 1][x - 1] == 1: continue
                if x == 1 and y == 1:continue
                dp[y][x] = dp[y-1][x] + dp[y][x-1]

        return dp[n][m]

grid = [[1]]
S = Solution()
print S.uniquePathsWithObstacles(grid)

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]

# [
#   [0, 0, 0, 0, 0, 1, 1, 1, 1],
#   [0, 0, 1, 0, 0, 0, 0, 0, 0],
#   [0, 0, 1, 0, 1, 0, 0, 0, 0],
#   [0, 0, 1, 0, 0, 0, 1, 0, 0],
#   [0, 0, 1, 0, 0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]