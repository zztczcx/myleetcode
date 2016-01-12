# -*- coding:utf-8 -*-
# There are N gas stations along a circular route,
# where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas
# to travel from station i to its next station (i+1).
# You begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index
# if you can travel around the circuit once, otherwise return -1.


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # 记录最后一个加起来小于零的索引，然后返回这个索引+1就是答案了。
        last, total, j = 0, 0, -1
        for i in xrange(len(gas)):
            diff = gas[i] - cost[i]
            last += diff
            total += diff

            if last < 0:
                j, last = i, 0
        if total < 0:
            return -1
        else:
            return j + 1


s = Solution()
print s.canCompleteCircuit([1, 2], [2, 1])

# code from
# https://leetcode.com/discuss/77616/my-44ms-6-line-python-solution-o-n-time-o-1-space
# class Solution(object):
#     def canCompleteCircuit(self, gas, cost):
#         """
#         :type gas: List[int]
#         :type cost: List[int]
#         :rtype: int
#         """
#         cumsum, min, min_idx = 0, 0, 0
#         for i in xrange(1, 1+len(gas)):
#             cumsum += (gas[i-1]-cost[i-1])
#             if cumsum < min:
#                 min, min_idx = cumsum, i
#         return min_idx if cumsum >= 0 else -1
# 1 如果总的gas - cost小于零的话，那么没有解返回-1
# 2 如果前面所有的gas - cost加起来小于零，那么前面所有的点都不能作为出发点。
# ----------------------------------------------------------------------
#
# 这个题要用反证法来理解。算法：
# 从i开始，j是当前station的指针，sum += gas[j] – cost[j]
# (从j站加了油，再算上从i开始走到j剩的油，走到j+1站还能剩下多少油)
# 如果sum < 0，说明从i开始是不行的。那能不能从i..j中间的某个位置开始呢？
# 假设能从k (i <=k<=j)走，那么i..j < 0，若k..j >=0，说明i..k – 1更是<0，
# 那从k处就早该断开了，根本轮不到j。
# 所以一旦sum<0，i就赋成j + 1，sum归零。
# 最后total表示能不能走一圈。
