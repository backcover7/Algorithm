class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = True if x > 0 else False
        x = abs(x)
        string = ''
        l1 = []
        l1 = list(str(x))
        length = len(l1)
        for iterate in range(length, 0, -1):
            if iterate == 0 and len(string) != 0:
                continue
            else: string += str(l1[iterate-length-1])

        if int(string) < 2147483647 and int(string) >= -2147483648:
            if flag: return int(string)
            else: return (0-int(string))
        else: return 0

t = -123
s = Solution()
s.reverse(t)
