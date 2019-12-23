import bisect

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums: return nums.index(target)
        if target < nums[0]: return 0
        if target > nums[-1]: return len(nums)
        origin = nums
        def binary_search(nums, target):
            if len(nums) == 1:
                if target < nums[0]:
                    return origin.index(nums[0])
                elif target > nums[0]:
                    return origin.index(nums[0])+1
            mid = len(nums) // 2
            if target < nums[mid]:
                return binary_search(nums[:mid], target)
            elif target > nums[mid]:
                return binary_search(nums[mid:], target)

        return binary_search(nums, target)

    def searchInsert_bisect(self, nums, target):
        return bisect.bisect_left(nums, target)

S = Solution()
print S.searchInsert([1,3,5,6], 0)
