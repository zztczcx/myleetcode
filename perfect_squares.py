# -*- coding:utf-8 -*-
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, 25,...) which sum to n.
# 
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.




class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q1 = [0]
        q2 = []
        level = 0
        visited = [False] * (n+1)
        while True:
            level += 1
            for v in q1:
                i = 0
                while True:
                    i += 1
                    t = v + i * i
                    if t == n: return level
                    if t > n: break
                    if visited[t]: continue
                    q2.append(t)
                    visited[t] = True
            q1 = q2
            q2 = []

        return 0 

## accept copy from https://leetcode.com/discuss/57218/python-accepted-solution
## 采用了深度优先，不是很明白他那个算法。
