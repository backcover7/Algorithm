class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = ' ' + s
        p = ' ' + p
        lengthP = len(p)
        lengthS = len(s)
        T = [[0 for x in range(lengthS)] for y in range(lengthP)]
        T[0][0] = 1
        for i in xrange(lengthP):
            for j in xrange(lengthS):
                if i==0 and j== 0: continue
                if j==0 and p[i]=='*':
                    T[i][j] = T[i-1][j]
                elif j==0:
                    T[i][j] = 0
                elif p[i] == s[j] or p[i] == '?':
                    T[i][j] = T[i-1][j-1]
                elif p[i] == '*':
                    T[i][j] = max(T[i-1][j], T[i][j-1])
                else:
                    T[i][j] = 0
        if T[-1][-1]:
            return True
        else:
            return False

s = "aa"
p = "*"
so = Solution()
print so.isMatch(s, p)