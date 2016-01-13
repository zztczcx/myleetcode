# -*- coding:utf-8 -*-
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        p={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        ans=0;
        left=0
        for v in s:
            if left<p[v]:
                ans=ans-2*left
            ans=ans+p[v]
            left=p[v]
        return ans
