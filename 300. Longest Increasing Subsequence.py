class Solution(object):
    def lengthOfLIS(self, nums):
        #DP
        #https://www.youtube.com/watch?v=S9oUiVYEq7E
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [1]*len(nums)
        for i in range (1, len(nums)):
            for j in range(i):
                if nums[i] >nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        # this step will choose the element j which is less than element i
        # and the length of sequence which is tailed with element j is used to calculate the length of the new sequence tailed with element i
        return max(dp)

    def lengthOfLIS_BS(self, nums):
        #Binary Search
        #https://blog.csdn.net/wbin233/article/details/77570070
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

S = Solution()
print S.lengthOfLIS_BS([4,5,6,3])