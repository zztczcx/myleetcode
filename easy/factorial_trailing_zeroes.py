# -*- coding:utf-8 -*-
# Given an integer n, return the number of trailing zeroes in n!.
# Note: Your solution should be in logarithmic time complexity.


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n >= 5:
            return self.trailingZeroes(n/5) + n/5
        else:
            return 0

# Concept:
#
# Since 0 only company with 5*2 So only need to count the volume of 5 factor.
# (because 2 always enough)
# So.. 100! 's zero has =>
# floor(100/5) + floor(100/25) = floor(100/5) + floor((100/5)/5)


# class Solution(object):
#     def trailingZeroes(self, n):
#         zeroCnt = 0
#         while n > 0:
#             n = n / 5; zeroCnt += n
#
#         return zeroCnt
