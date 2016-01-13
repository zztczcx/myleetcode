# -*- coding:utf-8 -*-
# Write a function that takes an unsigned integer and
# returns the number of ’1' bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer ’11'
# has binary representation 00000000000000000000000000001011,
# so the function should return 3.

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # beats 44.46%
        return sum([int(i) for i in list("{0:b}".format(n))])
        # beats 72.87%
        # return str(bin(n)).count('1')
        # beats 44.46%
        # return len([i for i in range(32) if (1<<i)&n])
