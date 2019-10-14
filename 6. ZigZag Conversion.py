class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        length = len(s)
        if length < numRows - 2: return s

        pattern = []
        for x in range(numRows):
            pattern.append(x)

        for x_con in range(numRows - 2, 0, -1):
            pattern.append(x_con)

        cycle = len(pattern)        #8
        zigzag = [''] * numRows

        for iterate in range(length):
            row = pattern[iterate % cycle]
            text = s[iterate]
            zigzag[row] += text

        return ''.join(zigzag)

    def convert2(self, s, numRows):
        if numRows <= 1:
            return s

        stack = [''] * numRows
        row = 0
        reverse = True
        for c in s:
            stack[row] += c
            if reverse:
                if row == numRows - 1:
                    reverse = False
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    reverse = True
                    row += 1
                else:
                    row -= 1

        return ''.join(stack)


str = 'helloworld'
s = Solution()
s.convert(str, 5)


