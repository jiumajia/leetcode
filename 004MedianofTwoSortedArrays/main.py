import numpy
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return float(numpy.median(nums1+nums2))

if __name__ == "__main__":
    num1 = [1, 2]
    num2 = [3, 4]
    s = Solution()
    print s.findMedianSortedArrays(num1, num2)

# [] [1] return 1