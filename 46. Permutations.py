from itertools import permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(every_res, nums, res):
            if not nums:
                res.append(every_res)
                return
            else:
                for x in xrange(len(nums)):
                    backtrack(every_res+[nums[x]], nums[:x]+nums[x+1:], res)

        res = []
        backtrack([], nums, res)
        return res

so = Solution()
so.permute([1,2,3])
#so.permute([0,-1,1])