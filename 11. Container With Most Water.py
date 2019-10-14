class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        length = len(height)
        i = 0
        j = length - 1

        while 1:
            if i == j: break
            if height[i] >= height[j]:
                max_area = max(height[j] * (j - i), max_area)
                j -= 1
            elif height[i] < height[j]:
                max_area = max(height[i] * (j - i), max_area)
                i += 1

        return max_area

h = [2,3,4,5,18,17,6]
s = Solution()
s.maxArea(h)