class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans, i, j, left, right = 0, 0, len(height)-1, 0, 0
        while i < j:
            if height[i] < left:
                ans += left - height[i]
            elif height[i] >= left:
                left = height[i]

            if height[j] < right:
                ans += right - height[j]
            elif height[j] >= right:
                right = height[j]

            if height[i] < height[j]:
                i += 1
            elif height[i] >= height[j]:
                j -= 1
        return ans

h = [0,1,0,2,1,0,1,3,2,1,2,1]
S = Solution()
print S.trap(h)