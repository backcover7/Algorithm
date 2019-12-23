class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0: return 0
        l = 1
        if x==1: return 1
        else: r = x/2
        while (l<=r):
            if l == r:
                return l
            mid = (l+r+1) // 2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                l = mid
            elif mid**2 > x:
                r = mid - 1

s = Solution()
print s.mySqrt(16)