class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def greedy(nums, index):
            if nums[index] == len(nums)-1 or index == len(nums)-1:
                return True
            if nums[index] != 0:
                return greedy(nums, nums[index]+index)
            if nums[index] == 0 or nums[index] >= len(nums):
                return greedy(nums, nums[index]+index-1)
            else:
                return
        return greedy(nums, 0)

s = Solution()
print s.canJump([3,2,1,0,4])