class Solution(object):
    def climbStairs_recurse(self, n):
        """
        :type n: int
        :rtype: int
        """
        # recurse but time limit exceeded
        # Time complexity: O(2^n)
        if n <= 1: return 1
        return self.climbStairs_recurse(n-1) + self.climbStairs_recurse(n-2)

    # recurse with memory: Top-to-Down, main problem first
    # def __init__(self):
    #     self.mem = {0:1, 1:1}
    def climbStairs_recurse_with_memory(self, n):
        if n not in self.mem:
            self.mem[n] = self.climbStairs_recurse_with_memory(n - 1) + self.climbStairs_recurse_with_memory(n - 2)
        return self.mem[n]

    def climbStairs_dp_with_onearray(self, n):
        # Down-to-Top, subproblem first
        # space complexity: O(n)
        dp = [1] * (n+1)
        for i in xrange(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs(self, n):
        # one param, space complexity: O(1)
        dp1, dp2 = 1, 1
        for x in xrange(2, n+1):
            dp2, dp1 = dp1+dp2, dp2
        return dp2

S = Solution()
print S.climbStairs(36)