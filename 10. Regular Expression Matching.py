class Solution(object):
    def isMatch(self, s, p):
        if not p: return not s

        first_match = bool(s) and p[0] in {s[0],'.'}
        if len(p) >= 2 and p[1] == '*':
            return first_match and self.isMatch(s[1:],p) or self.isMatch(s, p[2:])

        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def isMatch_DP_top_down(self, s, p):
        #https://www.youtube.com/watch?v=l3hda49XcDE&list=PLrmLmBdmIlpuE5GEMDXWf0PWbBD9Ga1lO
        #bool T[i][j]     i is s, j is p
        #|- T[i-1][j-1] if str[i] == p[j] or p[j] == '.'
        #|- if p[j] == '*'
        #   |- 1. T[i][j-2]       0 occurrence
        #   |- 2. T[i-1][j] if str[i] == p[j-1] or p[j-1] == '.'
        #|- False

        s = ' ' + s
        p = ' ' + p
        lengthP = len(p)
        lengthS = len(s)
        T = [[0 for x in range(lengthP)] for y in range(lengthS)]
        T[0][0] = 1

        for j in range(1, lengthP):
            if p[j] == '*':
                T[0][j] = T[0][j - 2]


        for i in range(1, lengthS):
            for j in range(lengthP):
                if j == 0:
                    T[i][j] = 0

                if s[i] == p[j] or p[j] == '.':
                    T[i][j] = T[i-1][j-1]
                elif p[j] == '*':
                    T[i][j] = T[i][j - 2]
                    if s[i] == p[j-1] or p[j-1] == '.':
                        T[i][j] = T[i-1][j] or T[i][j]
                else: T[i][j] = 0

        if T[-1][-1]: return True
        else: return False


s = "a"
p = ".*..a*"
so = Solution()
#so.isMatch(s,p)
so.isMatch_DP_top_down(s,p)