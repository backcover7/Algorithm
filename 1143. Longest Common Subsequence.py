class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #https://www.youtube.com/watch?v=NnD96abizww
        #     a b c d e
        #   0 0 0 0 0 0
        # a 0 1 1 1 1 1
        # c 0 1 1 2 2 2
        # e 0 1 1 2 2 3

        score = 0
        init = 0
        m = len(text1)
        n = len(text2)
        col = n + 1
        l = [init-init for init in range(n+2)]
        for x in range(m):
            for y in range(n):
                location_index = col * (x + 1) + y + 1
                if text1[x] == text2[y]:
                    score = l[location_index - col -1] + 1
                    l.append(score)     #l[n*(x-1)+y]
                else:
                    score = max(l[location_index - 1], l[location_index - col])
                    l.append(score)
            l.append(0)
        return score


t1 = 'abc'
t2 = ''
so = Solution()
so.longestCommonSubsequence(t1, t2)