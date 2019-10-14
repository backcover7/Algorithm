class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # https://www.youtube.com/watch?v=htX69j1jf5U
        sig = (dividend < 0) == (divisor < 0)
        a, b, res = abs(dividend), abs(divisor), 0
        while a >= b:
            x = 0       # 2^x   # b*2^0; b*2^1; b*2^2
            while a >= b << (x + 1): x += 1
            res += 1 << x
            a -= b << x
            '''
            3*2^0=3, 10>3, x=0
            3*2^1=6, 10>6, x=1
            3*2^2=12, 10<12, x=2 [NO]
            res = 1<<x = 2^1 = 2
            10-3*2^1=10-6=4
            4->res=2+{1}=3      #This is the answer
            '''

        return min(res if sig else -res, 2147483647)

a = 10
b = 3
S = Solution()
print S.divide(a, b)