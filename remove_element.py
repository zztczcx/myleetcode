# -*- coding:utf-8 -*-
# Given an array and a value,
# remove all instances of that value in place and return the new length.
#
# The order of elements can be changed.
# It doesn't matter what you leave beyond the new length.


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a = nums[:]
        for i in a:
            if i == val:
                nums.remove(i)
        return nums

s = Solution()
print s.removeElement([3,3], 3)
