class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return
        if len(nums) == len(list(set(nums))): return
        nums = sorted(nums)
        for x in xrange(len(nums)):
            if nums[x+1] == nums[x]:
                return nums[x]

    def set_find(self, nums):
        distinct = set()
        for num in nums:
            if num in distinct:
                return num
            distinct.add(num)

        return None

S = Solution()
S.findDuplicate([1,3,4,2,2])