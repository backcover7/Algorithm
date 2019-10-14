class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dict:
                return [nums.index(comp),i]
            else:
                dict[nums[i]] = i


so = Solution()
so.twoSum([3,2,4],6)

#print[nums.index(comp),i]