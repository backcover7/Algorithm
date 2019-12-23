class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        digit = self.decompse(n)
        dict = {}
        while 1:
            res = 0
            for i in xrange(len(digit)):
                res += digit[i] ** 2
            if res == 1:
                return True
            elif res not in dict:
                dict[res] = res
                digit = self.decompse(res)
            else:
                return False

    def decompse(self, n):
        digit = []
        while n > 0:
            digit.append(n % 10)
            n = (n - n % 10) / 10
        return digit


S = Solution()
print S.isHappy(116)