# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList_stack(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
        dummy = q = ListNode(0)
        while head:
            l.append(head.val)
            head = head.next
        length = len(l)
        for x in xrange(length):
            q.next = ListNode(l.pop())
            q = q.next
        return dummy.next

    def reverseList(self, head):
        if not head or not head.next: return head
        prev, cur, nxt = None, head, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
S = Solution()
print S.reverseList(node1).val