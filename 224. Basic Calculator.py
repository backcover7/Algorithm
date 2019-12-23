class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, operand, res, sign = [], 0, 0, 1
        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch)
            elif ch == '+':
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ')':
                res += sign * operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0

        return res + sign * operand
S = Solution()
print S.calculate('1 + 2 - 7 - ( 4 -8 )')