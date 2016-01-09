# -*- coding:utf-8 -*-
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#
#     x x . x . . . 
#     . x x . . x .
#     . . . x . . .
#     . . . . x . .
#     . . x . . . x
#
# data: ( 1, 2 ), ( 1, 4 ) ( 4, 5 )
#
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        max_line = 0
        max_points = 0

        for p in points:
            p.xk
