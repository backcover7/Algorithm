# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = []
        while head != None:
            l.append(head.val)
            head = head.next
        del l[-n]
        q = ListNode(0)
        m = q
        for x in range(len(l)):
            m.next = ListNode(l[x])
            m = m.next
        return q.next

    def removeNthFromEnd_onePass(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for x in xrange(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
s = Solution()
s.removeNthFromEnd_onePass(a, 2)