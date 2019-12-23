class Solution(object):
    def searchRange_cheating(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0: return [-1, -1]
        if target in nums: index = first = nums.index(target)
        else: return [-1, -1]
        if first == len(nums)-1: return [len(nums)-1, len(nums)-1]
        while (first+1<=len(nums)):
            if first+1 == len(nums):
                last = first
                break
            if nums[first+1] == target:
                first += 1
            elif nums[first+1] != target:
                last = first
                break
        return [index, last]

    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        left, right = 0, len(nums)
        while left < right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle
            elif target > nums[middle]:
                left = middle
            else:
                break
        i = middle
        while i >= 0 and nums[i] == target:
            i -= 1
        j = middle
        while j <= len(nums) -1 and nums[j] == target:
            j += 1
        return [i+1, j-1]

S = Solution()
print S.searchRange([5,7,7,8,8,10],8)