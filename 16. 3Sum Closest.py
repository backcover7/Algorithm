class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums)
        res = sum(nums[0:3])
        for start in xrange(len(nums)):
            point, end = start+1, len(nums)-1
            while point<end:
                s = sum((nums[start],nums[point]),nums[end])
                if abs(s-target) < abs(res-target):
                    res = s
                if s<target:
                    point += 1
                elif s>target:
                    end -= 1
                else:
                    return res
        return res

nums = [1,-3,3,5,4,1]
target = 1
s = Solution()
s.threeSumClosest(nums, target)