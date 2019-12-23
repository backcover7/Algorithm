class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # https://leetcode.com/problems/powx-n/discuss/182026/Python-or-Recursion-tm
        if n == 0: return 1
        if n < 0: return 1.0 / self.myPow(x, -n)
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
s = Solution()
print s.myPow(2, 10)