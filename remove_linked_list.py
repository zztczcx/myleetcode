# -*- coding:utf-8 -*-
# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        nodes = []
        while head:
            if head.val != val:
                nodes.append(head)
            head = head.next

        for i in xrange(0, len(nodes)-1):
            nodes[i].next = nodes[i+1]

        if len(nodes) == 0:
            return None
        else:
            nodes[-1].next = None
            return nodes[0]
