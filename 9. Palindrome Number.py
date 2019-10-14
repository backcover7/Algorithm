class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        str_x = str(x)
        length = len(str_x)
        if x < 0:
            return False
        else:
            l1 = list(str_x)
            l1_reverse = l1.reverse()
            str_x_reverse = ''.join(l1)
            if str_x == str_x_reverse: return True
            else: return False


x = 3123
s = Solution()
s.isPalindrome(x)