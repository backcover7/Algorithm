class Solution(object):
    def removeElement_onepass(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for x in xrange(0, len(nums)):
            if nums[x] != val:
                nums[i] = nums[x]
                i += 1
        return i

    def removeElement(self, nums, val):
        for x in nums[:]:
            if x == val:
                nums.remove(val)
        return len(nums)

s = Solution()
s.removeElement([0,1,2,2,3,0,4,2],1)