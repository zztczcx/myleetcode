# -*- coding:utf-8 -*-
# Given an integer, write a function to determine if it is a power of two.


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True

        if n % 2 == 0:
            n = n / 2
            if n == 1:
                return True
            return self.isPowerOfTwo(n)
        else:
            return False
