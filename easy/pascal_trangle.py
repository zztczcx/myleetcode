# -*- coding:utf-8 -*-
# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []
        for i in xrange(1, numRows + 1):
            if i == 1:
                row = [1]
                pascal.append(row)
                continue
            if i == 2:
                row = [1, 1]
                pascal.append(row)
                continue
            else:
                pre = pascal[i-2]
                row = [1]
                for n in xrange(len(pre) - 1):
                    s = pre[n] + pre[n+1]
                    row.append(s)
                row.append(1)
            pascal.append(row)

        return pascal

s = Solution()
print s.generate(5)


#def generate(numRows):
#    pascal = [[1]*(i+1) for i in range(numRows)]
#    for i in range(numRows):
#        for j in range(1,i):
#            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
#    return pascal
