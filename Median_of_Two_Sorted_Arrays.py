"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n,m=len(nums1),len(nums2)
        i,j=0,0
        r=[]
        while i<n and j<m:
            if nums1[i]<nums2[j]:
                r.append(nums1[i])
                i+=1
            else:
                r.append(nums2[j])
                j+=1
        while i<n:
            r.append(nums1[i])
            i+=1
        while j<m:
            r.append(nums2[j])
            j+=1
        mid=len(r)//2
        if len(r)%2!=0:
            return r[mid]
        else:
            return (float(r[mid]+r[mid-1])/2)
    