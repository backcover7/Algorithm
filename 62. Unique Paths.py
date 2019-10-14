class Solution(object):
    # def __init__(self):
    #     self.mem = {(0,0):1}
    def uniquePaths_recurse_with_memory(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m<=0 or n<=0: return 0
        if m==1 and n==1: return 1
        if (m,n) not in self.mem:
            self.mem[(m,n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.mem[(m,n)]

    def uniquePaths(self, m, n):
        dp = [[0]*(m+1) for _ in xrange(n+1)]
        dp[1][1] = 1
        for y in xrange(1, n+1):
            for x in xrange(1, m+1):
                if x == 1 and y == 1:continue
                dp[y][x] = dp[y-1][x] + dp[y][x-1]

        return dp[n][m]

S = Solution()
print S.uniquePaths(7,3)

