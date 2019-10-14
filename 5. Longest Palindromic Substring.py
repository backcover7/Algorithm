class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Failed in programming 'expand around the center', if this tip is seen please complete the algo.

        #Manacher's Algo
        #http://manacher-viz.s3-website-us-east-1.amazonaws.com/#/
        #https://www.zhihu.com/question/37289584?sort=created

        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n     #P for stroing the center
        C = R = 0       #C for center of parlindromic, R for radius of the parlindromic
        for i in range(1, n - 1):
            t1 = R - i
            t2 = 2 * C - i
            P[i] = (R > i) and min(R - i, P[2 * C - i])     #3 circumstances will make the over range possible
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:       #expand i from center, limit is R, mirrorOfI = 2*C-i
                P[i] += 1
            if i + P[i] > R:                                #out of range
                C, R = i, i + P[i]
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]  #origin index = (new index - R) // 2


s = 'babbabcbaccba'
so = Solution()
so.longestPalindrome(s)