class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, d):
            if i<0 or j<0 or i==h or j==w or board[i][j] != word[d]: return False
            tmp = board[i][j]
            if board[i][j] == word[d]: board[i][j] = '#'    # avoid visting again
            if d == len(word)-1: return True
            res = dfs(i - 1, j, d + 1) \
                   or dfs(i + 1, j, d + 1) \
                   or dfs(i, j - 1, d + 1) \
                   or dfs(i, j + 1, d + 1)
            board[i][j] = tmp
            return res

        if not board: return False
        h = len(board)
        w = len(board[0])
        for i in xrange(h):
            for j in xrange(w):
                if dfs(i, j, 0):
                    return True
        return False

board =[
  ['a','a']
]

S = Solution()
print S.exist(board, "aaa")