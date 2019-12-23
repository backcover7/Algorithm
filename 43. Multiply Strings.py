class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        d = {48: 0, 49: 1, 50: 2, 51: 3, 52: 4, 53: 5, 54: 6, 55: 7, 56: 8, 57: 9}
        num1, num2 = num1[::-1], num2[::-1]
        def str_to_int(num):
            res = radix = 0
            for x in num:
                res += d[ord(x)] * (10 ** radix)
                radix += 1
            return res
        return str(str_to_int(num1) * str_to_int(num2))

S = Solution()
print S.multiply('2', '3')
