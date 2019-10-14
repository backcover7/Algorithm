# Definition for singly-linked list.
from Queue import PriorityQueue

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def Two_lists(l1, l2):
            if not l1 or l2 and l1.val > l2.val:
                l1, l2 = l2, l1
            if  l1:
                l1.next = Two_lists(l1.next, l2)
            return l1

        res = []
        if not lists: return
        for x in xrange(len(lists)):
            res = Two_lists(res, lists[x])

        return res

    def mergeKLists_PriorityQueue(self, lists):
        head = point = ListNode(0)
        q = PriorityQueue()
        for x in lists:
            if x:
                q.put((x.val, x))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

    def mergeKLists_DivideAndConquer(self, lists):
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists_DivideAndConquer(lists[:mid])
        r = self.mergeKLists_DivideAndConquer(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = cur = ListNode(0)
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next

if 1:
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(5)
    node1.next = node2
    node2.next = node3

    nodea = ListNode(1)
    nodeb = ListNode(3)
    nodec = ListNode(4)
    nodea.next = nodeb
    nodeb.next = nodec

    nodeq = ListNode(2)
    nodew = ListNode(6)
    nodeq.next = nodew

    lists = [node1, nodea, nodeq]

s = Solution()
s.mergeKLists_DivideAndConquer(lists)