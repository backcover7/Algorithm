class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip(' ')
        start = 0
        sign = 1

        if not str: return 0
        if str[0] == '-':
            sign = -1
            start = 1
        elif str[0] == '+':
            start = 1
        elif not str[0].isdigit():
            return 0

        result = 0
        for x in range(start, len(str)):
            if not str[x].isdigit():
                break
            result = result * 10 + int(str[x])

        result *= sign

        MAX_VALUE = 2**31 -1
        MIN_VALUE = -2**31
        if result > MAX_VALUE:
            return MAX_VALUE
        elif result < MIN_VALUE:
            return  MIN_VALUE
        else:
            return result



x = ""
s = Solution()
s.myAtoi(x)