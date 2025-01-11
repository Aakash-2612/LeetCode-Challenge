"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

• Each letter in pattern maps to exactly one unique word in s.
• Each unique word in s maps to exactly one letter in pattern.
• No two letters map to the same word, and no two words map to the same letter.
 

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        d = {}
        sett = set()
        if len(arr) != len(pattern):
            return False
        for i, j in zip(pattern, arr):
            if i not in d:
                d[i] = j
                if j not in sett:
                    sett.add(j)
                else:
                    return False
            else:
                if d[i] != j:
                    return False
        
        return True

