class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]','').replace('{}','')
        return s == ''

    def isValid_stack(self, s):
        l = ['(','[','{']
        d = {')':'(',']':'[','}':'{'}
        stack = []
        for x in s:
            if x in l:
                stack.append(x)
            elif x not in l and d[x] in stack:
                stack.pop()
            else:
                return False

        if len(stack) == 0: return True
        else: return False


s = '()[(}()]'
so = Solution()
so.isValid_stack(s)