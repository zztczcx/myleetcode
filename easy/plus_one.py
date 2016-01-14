# -*- coding:utf-8 -*-
# Given a non-negative number represented as an array of digits,
# plus one to the number.
#
# The digits are stored such that
# the most significant digit is at the head of the list.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        return map(int, list(str(int(''.join(map(str, digits))) + 1)))
        # num=reduce(lambda x,y:x*10+y,digits)+1
        # return [int(i) for i in str(num)]
