'''
input:nums1 = [1,2],nums2 = [3];nums1 = [1, 2],nums2 = [3, 4]
output:2.0;2.5
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = num1.extend(nums2)
        res = sorted(res)
        lenres = len(res)
        pointer = int((lenres)/2)
        if lenres % 2 == 0:
            return (res[me_pointer2]+res[me_pointer2-1])/2
        else:
            return res[me_pointer2]


a = [1,2,3]
b = [2,3,4]
print(a)
print(b)
a.extend(b)
print(a)