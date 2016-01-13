# -*- coding:utf-8 -*-
# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary
# as 00000010100101000001111010011100),
# return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
#
# Related problem: Reverse Integer


class Solution(object):
    # beats 10.49%
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """

        l = list(bin(n))[-1:1:-1]
        l = l + ['0'] * (32 - len(l))
        s = ''.join(l)
        return int(s, 2)

    # return int(bin(n)[2:].zfill(32)[::-1], 2)


    # oribin='{0:032b}'.format(n)
    # reversebin=oribin[::-1]
    # return int(reversebin,2



s = Solution()
print s.reverseBits(43261596)
