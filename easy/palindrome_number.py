# -*- coding:utf-8 -*-
# Determine whether an integer is a palindrome. Do this without extra space.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        tmp = x
        res = 0
        while(tmp != 0):
            res = res * 10 + tmp % 10
            tmp = tmp / 10
        return res == x
