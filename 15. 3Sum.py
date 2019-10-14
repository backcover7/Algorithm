import bisect

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        if len(nums)<3: return res

        length = len(nums)
        listsort = sorted(nums)
        for start in range(length-2):
            if listsort[start] > 0: break
            if start > 0 and listsort[start] == listsort[start-1]: continue
            point = start + 1
            end = length - 1

            while point<end:
                total = listsort[start] + listsort[point] + listsort[end]
                if total < 0:
                    point += 1
                elif total > 0:
                    end -= 1
                else:
                    res.append([listsort[start], listsort[point], listsort[end]])
                    while point < end and listsort[point] == listsort[point+1]:
                        point += 1
                    while point< end and listsort[end] == listsort[end-1]:
                        end -= 1
                    point += 1
                    end -= 1

        return res

    def threeSum_180ms(self, nums):
        ans = []
        numcounts = self.count(nums)  # get set(nums) and their counts
        nums = sorted(numcounts)  # same as set(nums)
        for i, num in enumerate(nums):
            '''
                We consider two scenarios:
                    When there are duplicate nums in a solution
                    When all values in a solution are unique
                        at which point, we perform twosum for each negative num
            '''
            if numcounts[num] >= 2:  # there are 2 scenarios for 2 duplicate vals
                if num == 0:  # zeros
                    if numcounts[num] >= 3:
                        ans.append([0, 0, 0])
                else:  # and non-zeros
                    if (-2 * num) in nums:
                        ans.append([num, num, -2 * num])
            if num < 0:
                ans = self.twosum(ans, nums, numcounts, num, i)

        return ans

    def twosum(self, ans, nums, numcounts, num, i):
        """Find two numbers a, b such that a + b + num = 0 (a + b = -num)"""
        twosum = -num  # find 2 nums that sum up to this positive num
        left = bisect.bisect_left(nums, (twosum - nums[-1]), i + 1)  # minval
        right = bisect.bisect_right(nums, (twosum // 2), left)  # maxval

        for num2 in nums[left:right]:  # we do this knowing the list is sorted
            num3 = twosum - num2
            if num3 in numcounts and num3 != num2:
                ans.append([num, num2, num3])

        return ans

    def count(self, nums):
        """Organize nums by `{num: occurence_count}`"""
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        return count



s = Solution()
s.threeSum_180ms([-1, 0, 1, 2, -1, -4])


# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]