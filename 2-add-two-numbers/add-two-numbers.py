# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        num1 = ""
        num2 = ""

        while(l1 != None):
            num1 = str(l1.val) + num1
            l1 = l1.next
        
        while(l2 != None):
            num2 = str(l2.val) + num2
            l2 = l2.next
        
        print(num1)
        print(num2)

        res = int(num1) + int(num2)
        res = str(res)

        l3 = ListNode(res[len(res)-1])
        first = l3
        print(first)

        for c in reversed(res[:len(res)-1]):
            print c
            l3.next = ListNode(c)
            l3 = l3.next

        
        return first