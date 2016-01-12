# -*- coding:utf-8 -*-
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty
# and the majority element always exist in the array.


# beats 71%
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        times_dict = {}
        for i in nums:
            if i not in times_dict:
                times_dict[i] = 1
            else:
                times_dict[i] += 1

        max_times = 0
        maj = 0
        for k, v in times_dict.iteritems():
            if v > max_times:
                max_times = v
                maj = k

        return maj


# return sorted(num)[len(num)/2]

# class Solution(object):
#     def majorityElement(self, nums):
#         # implement the Moore's voting algorithm: find a pair different element and delete it
#         count = 0
#         for i in range(0, len(nums)):
#             if count == 0:
#                 key = nums[i]
#                 count = 1
#             else:
#                 if key == nums[i]:
#                     count += 1
#                 else:
#                     count -= 1
#         return key
