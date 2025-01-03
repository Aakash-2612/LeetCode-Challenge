"""
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.


Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ones = 0
        zero = 0
        ans = 0
        temp = False
        for i in s:
            if i == '0':
                if temp and zero != 0:
                    ans += min(ones, zero)
                    zero = 0
                temp = False
                zero += 1

            elif i == '1':
                if not temp and ones != 0:
                    ans += min(ones, zero)
                    ones = 0
                temp = True
                ones += 1

        ans += min(ones, zero)
        return ans
