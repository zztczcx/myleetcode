# -*- coding:utf-8 -*-
# Given a sorted linked list,
# delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # beats 42.97%
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r = head
        while head:
            val = head.val
            n = head.next
            if n and n.val == val:
                if n.next:
                    head.next = n.next
                else:
                    head.next = None
            else:
                head = n
        return r
