class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''

        common = strs[0]
        length = len(strs)
        for x in range(length-1):
            if strs[x+1] == '' and len(common) != 0:
                return ''
            else:
                for y in range(min(len(common), len(strs[x+1]))):
                    if strs[x+1][y] == common[y]:
                        continue
                    else:
                        common = common[0:y]
                        break

                if len(common) != 0:
                    common = common[0:y+1]
                else: common = ''

        return common

    def longestCommonPrefix_zip(self, strs):
        prefix=[]
        num = len(strs)
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)


l = ["flower","flow","flight"]
s = Solution()
s.longestCommonPrefix_divde_and_conquer(l)