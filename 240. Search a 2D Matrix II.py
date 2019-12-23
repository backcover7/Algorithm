class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in xrange(len(matrix)):
            if target not in matrix[row]:
                continue
            else:
                return True
        return False
    def searchMatrix_oblique(self, matrix, target):
        if matrix:
            row, col, width= len(matrix)-1, 0, len(matrix[0])
            while row >= 0 and col < width:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    row -= 1
                else:
                    col += 1
        return False

m = [[-5]]
t = -5
S = Solution()
S.searchMatrix_oblique(m, t)