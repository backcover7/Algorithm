class Solution(object):
    def findMedianSortedArrays_On(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge_list = []
        x = y = i = 0
        while x < len(nums1) or y < len(nums2):
            if x == len(nums1):
                merge_list.append(nums2[y])
                y += 1
            elif y == len(nums2):
                merge_list.append(nums1[x])
                x += 1
            elif nums1[x] >= nums2[y]:
                merge_list.append(nums2[y])
                y += 1
            else:
                merge_list.append(nums1[x])
                x += 1
            i += 1

        mid = len(merge_list) / 2
        if len(merge_list) % 2 == 0:
            return (merge_list[mid-1] + merge_list[mid]) / 2.0
        else:
            return merge_list[mid] / 1.0

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #https://www.youtube.com/watch?v=LPFhl65R7ww&t=1013s
        #
        #l1 -> l1_left and l1_right: x1, x2, x3, | x4, x5, x6       x
        #l2 -> l2_left and l2_right: y1, y2, y3, y4, | y5, y6, y7   y
        #(x+y+1)/2
        # partition x + partition y = (x + y + 1) / 2
        # Found:
        # maxLeftX <= minRightY
        # maxLeftY <= minRightX
        #
        # elif:
        # maxLeftX > minRightY
        # move
        # towards
        # left in X
        #
        # else:
        # move
        # towards
        # right in X

        start = 0
        x = len(nums1)
        y = len(nums2)
        end = x - 1
        parx = (start + end) / 2
        parx_and_pary = (x + y + 1) / 2
        pary = parx_and_pary - parx
        if x == 0:
            if y % 2 != 0: return nums2[y/2] / 1.0
            else: return (nums2[y/2 - 1] + nums2[y/2]) / 2.0
        elif y == 0:
            if x % 2 != 0: return nums1[x/2] / 1.0
            else: return (nums1[x/2 - 1] + nums1[x/2]) / 2.0
        else:
            while 1:
                leftx = nums1[parx - 1] if parx != 0 else float('-inf')
                rightx = nums1[parx] if parx != x else float('inf')
                lefty = nums2[pary - 1] if pary != 0 else float('-inf')
                righty = nums2[pary] if pary !=y else float('inf')
                if leftx <= righty and lefty <= rightx:
                    if((x + y) % 2 != 0):
                        return max(leftx, lefty)
                    else:
                        return (max(leftx, lefty) + (min(rightx, righty))) / 2.0
                elif leftx > righty:
                    end = parx - 1
                    parx = (start + end) / 2
                    pary = parx_and_pary - parx
                else:
                    start = parx + 1
                    parx = (start + end) / 2
                    pary = parx_and_pary - parx

    def findMedianSortedArrays3(self, nums1, nums2):
        nums3 = sorted(nums1 + nums2)
        length = len(nums1) + len(nums2)
        if length % 2 == 0: return (nums3[length/2] + nums3[length/2 - 1]) / 2.0
        else: return float(nums3[length/2])

l1 = [1,3]
l2 = [2]

s = Solution()
s.findMedianSortedArrays3(l1,l2)