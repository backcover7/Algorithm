# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or l2 and l1.val > l2.val:
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

l1 = ListNode(1)
l12 = ListNode(4)
l1.next = l12

l2 = ListNode(2)
l22 = ListNode(4)
l2.next = l22

s = Solution()
s.mergeTwoLists(l1,l2)