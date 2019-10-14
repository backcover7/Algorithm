class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.findNum(nums, target, 4, [], results)
        return results

    def findNum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return
        # sovle 2-nums
        if N == 2:
            point, end = 0, len(nums)-1
            while point < end:
                if nums[point] + nums[end] == target:
                    results.append(result + [nums[point], nums[end]])
                    point += 1
                    end -= 1
                    while point < end and nums[point] == nums[point-1]:
                        point += 1
                    while point < end and nums[end] == nums[end+1]:
                        end -= 1
                elif nums[point] + nums[end] < target:
                    point += 1
                else:
                    end -= 1
        else:
            for i in range(0, len(nums)-N+1):
                #print len(nums)-N+1
                if target < nums[i]*N or target > nums[-1]*N:       #the least sum and the most sum
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.findNum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return



l = [1, 0, -1, 0, -2, 2]
t = 0
l1 = [-3,-1,0,2,4,5]
t1 = 1
l2 = [-3,-1,0,2,4,5]
t2 = 2
l3 = [-3,-2,-1,0,0,1,2,3]
t3 = 0
l4 = [5,5,3,5,1,-5,1,-2]
t4 = 4
s = Solution()
s.fourSum(l4,t4)