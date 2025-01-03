"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.


Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        neg = []
        temp = nums[-1] * nums[-2] * nums[-3]
        for i in nums:
            if i < 0:
                neg.append(i)
        
        if len(neg) >= 2:
            a, b = neg[0], neg[1]
            c = nums[-1]
            res = a * b * c
            return max(temp, res)
        else:
            return temp
