class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or len(nums) == 2: return nums[-1]
        start = 0
        end = len(nums)-1
        while(start<=end):
            if nums[start] < nums[end] or start == end:
                return nums[end+1]
            else:
                start += 1
                end -= 1

s = Solution()
print s.findMin([3,2,1])