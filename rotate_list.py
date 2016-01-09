# -*- coding:utf-8 -*-
# Given a list, rotate the list to the right by k places, where k is non-negative.
# 
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not hasattr(head, 'next'):
            return head
            
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        k = k % len(node_list)
        
        if k == 0:
            return node_list[0]
            
        if k == len(node_list):
            return node_list[0]
            
        end = node_list[-1]
        start = node_list[0]

        end.next = start
        node_list[-k -1].next = None

        return node_list[-k] 
