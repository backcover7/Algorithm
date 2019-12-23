class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        found = False
        stack = []
        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j]:
                    self.dfs(A, i, j, n, m, stack)
                    found = True
                    break
            if found:
                break
        steps = 0
        # breadth first search, once we find next '1', that is our final answer 
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while stack:
            size = len(stack)
            level = []
            while (size):
                temp = stack.pop()
                size -= 1
                x, y = temp[0], temp[1]
                for dx, dy in dirs:
                    tx = x + dx
                    ty = y + dy
                    if tx < 0 or ty < 0 or tx >= n or ty >= m or A[tx][ty] == 2:
                        continue
                    if A[tx][ty] == 1:
                        return steps
                    A[tx][ty] = 2
                    level.append((tx, ty))
            steps += 1
            stack = level
        return -1

    def dfs(self, A, row, col, n, m, stack):
        if row < 0 or col < 0 or row >= n or col >= m or A[row][col] != 1:
            return
        A[row][col] = 2
        stack.append((row, col))
        self.dfs(A, row + 1, col, n, m, stack)
        self.dfs(A, row - 1, col, n, m, stack)
        self.dfs(A, row, col + 1, n, m, stack)
        self.dfs(A, row, col - 1, n, m, stack)


A = [[0,1],[1,0]]
S = Solution()
print S.shortestBridge(A)