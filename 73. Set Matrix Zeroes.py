class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        h = len(matrix)
        w = len(matrix[0])
        is_col = False
        for i in xrange(h):
            if matrix[i][0] == 0:
                is_col = True
            for j in xrange(1, w):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in xrange(1, h):
            for j in xrange(1, w):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(w):
                matrix[0][j] = 0
        if is_col:
            for i in range(h):
                matrix[i][0] = 0
        return matrix

print Solution().setZeroes([
    [1, 1, 1],
    [0, 1, 2]
])
