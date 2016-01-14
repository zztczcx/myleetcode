# -*- coding:utf-8 -*-
# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly
# since it includes another prime factor 7.
#
# Note that 1 is typically treated as an ugly number.


class Solution(object):
    # Your runtime beats 89.64%
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1 or num == 4:
            return True

        factors = [2, 3, 5]
        if num in factors:
            return True
        for f in factors:
            if num % f == 0:
                d = num / f
                return self.isUgly(d)
            else:
                continue
        return False


    # Your runtime beats 43.96%
    # def isUgly(self, num):
    #     if num <= 0:
    #         return False
    #     for x in [2, 3, 5]:
    #         while num % x == 0:
    #             num = num / x
    #     return num == 1
