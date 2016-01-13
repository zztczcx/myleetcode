# -*- coding:utf-8 -*-
# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

        # Recursion 31%
        # def reverseList(self, head):
        #     return self._reverse(head)

        # def _reverse(self, node, prev=None):
        #     if not node:
        #         return prev
        #     n = node.next
        #     node.next = prev
        #     return self._reverse(n, node)
