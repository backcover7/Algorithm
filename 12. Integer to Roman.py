class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        dict = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}

        string = ''
        for x in range(3, -1, -1):
            text = str(num / (10**x))
            digit = int(text[-1])
            if digit < 4 :
                string += dict[10**x] * digit
            elif digit == 4:
                string += dict[10**x] + dict[10**x * 5]
            elif digit >= 5 and digit < 9:
                string += dict[10**x * 5] + dict[10**x] * (digit-5)
            elif digit == 9:
                string += dict[10**x] + dict[10**(x+1)]

        return string


s = Solution()
s.intToRoman(1994)