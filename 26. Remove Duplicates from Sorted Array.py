from collections import OrderedDict


class Solution(object):
    def removeDuplicates_(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        while index < len(nums):
            if nums[index] == nums[index-1]:
                nums.remove(nums[index])
                continue
            index += 1
        return len(nums)

    def removeDuplicates_runner(self, nums):
        # slow runner and fast runner
        if len(nums) <= 1: return len(nums)
        i = 0
        for x in xrange(1, len(nums)):
            if nums[i] != nums[x]:
                i += 1
                nums[i] = nums[x]
        return i+1

    def removeDuplicates(self, nums):
        # use library
        nums[:] = OrderedDict.fromkeys(nums)
        return len(nums)

S = Solution()
print S.removeDuplicates([0,0,1,1,1,2,2,3,3,4])