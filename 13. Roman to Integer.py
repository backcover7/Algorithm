class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

        num = 0
        length = len(s)
        x = 0
        while(x < length):
            if x + 1 < length:
                if dict[s[x+1]] > dict[s[x]]:
                    num += dict[s[x+1]] - dict[s[x]]
                    x += 2
                    continue

            num += dict[s[x]]
            x += 1

        return num

s = Solution()
s.romanToInt('MCMXCIV')