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

        new = self.convert_list(gas, cost)
        for start in self.posible_start(new):
            way = self.twist_list(new, start)
            last = 0
            for i in way:
                last = last + i
                if last < 0:
                    break
            if last >= 0:
                return start

        return -1

    def convert_list(self, gas, cost):
        length = len(gas)
        return [(gas[i] - cost[i]) for i in xrange(length)]

    def posible_start(self, list_new):
        length = len(list_new)
        return [i for i in xrange(length) if list_new[i] >= 0]

    def twist_list(self, new, start):
        return new[start: len(new)] + new[0:start]


s = Solution()
print s.canCompleteCircuit([1, 2], [2, 1])
