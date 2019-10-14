# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        rtype = ListNode(0)
        p = rtype

        while (1):
            if l1 != None and l2 != None:
                remain = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) / 10
                p.next = ListNode(remain)
                p = p.next
                l1 = l1.next
                l2 = l2.next
            elif l1 == None and l2 != None:
                remain = (l2.val + carry) % 10
                carry = (l2.val + carry) / 10
                p.next = ListNode(remain)
                p = p.next
                l2 = l2.next
            elif l1 != None and l2 == None:
                remain = (l1.val + carry) % 10
                carry = (l1.val + carry) / 10
                p.next = ListNode(remain)
                p = p.next
                l1 = l1.next
            elif l1 == None and l2 == None:
                if carry != 0:
                    p.next = ListNode(carry)
                break

        return rtype.next

a1 = ListNode(5)
a2 = ListNode(3)
a3 = ListNode(6)
a1.next = a2
a2.next = a3

b1 = ListNode(5)
b2 = ListNode(1)
b3 = ListNode(7)
b1.next = b2
b2.next = b3

s = Solution()
s.addTwoNumbers(a1, b1)