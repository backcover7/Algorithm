class Solution(object):
    def permuteUnique_from46(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(every_res, nums, res):
            if not nums:
                if every_res in res: return
                else:
                    res.append(every_res)
                return
            else:
                for x in xrange(len(nums)):
                    backtrack(every_res+[nums[x]], nums[:x]+nums[x+1:], res)

        res = []
        backtrack([], nums, res)
        return res

    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            return res.append(path)
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)

so = Solution()
print so.permuteUnique([1,1,2])
