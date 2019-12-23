class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while (l <= r):
            mid = (l + r) // 2
            if (nums[int(mid)] == target):
                return mid
            elif (nums[int(mid)] < target):
                l = mid + 1
            else:
                r = mid - 1
        return -1

nums = [-1,0,3,5,9,12]
target = 9
s = Solution()
print s.search(nums, target)
