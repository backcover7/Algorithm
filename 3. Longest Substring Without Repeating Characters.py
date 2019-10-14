class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start_index = 0
        sub = {}
        l1 = list(s)
        max = 0

        for x in range(len(l1)):
            if l1[x] not in sub:
                sub[l1[x]] = x
                if x+1-start_index > max:
                    max = x+1-start_index
            else:
                same_index = sub[l1[x]]
                for el in l1[start_index:same_index+1]:
                    del sub[el]
                sub[l1[x]] = x
                start_index = same_index + 1
                if x - start_index > max:
                    max = x - start_index
        return max

    def lengthOfLongestSubstring2(self, s):     #90.8%
        d = ""
        f = ""
        for i in range(len(s)):
            if s[i] not in f:
                f += s[i]
            else:
                if len(d) < len(f):
                    d = f
                f = f[f.index(s[i]) + 1::] + s[i]

        return max(len(d), len(f))

str = 'abcabcbb'
s = Solution()
s.lengthOfLongestSubstring2(str)