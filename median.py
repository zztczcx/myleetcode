class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = nums1 + nums2
        l.sort()
        length = len(l)
        print length
        if len(l) % 2 == 0:
            return (l[length / 2 - 1] + l[length / 2]) / 2.0
        else:
            return l[(length + 1) / 2 - 1]

if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([], [2, 3])
