"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.
 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
"""

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        d = {'a': -1,
             'b': -1,
             'c': -1}
        for index, i in enumerate(s):
            d[i] = index
            if d['a'] >= 0 and d['b'] >= 0 and d['c'] >= 0:
                count += min(d['a'], d['b'], d['c']) + 1
        
        return count
