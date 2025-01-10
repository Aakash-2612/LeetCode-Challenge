"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
 

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        tempStr = s[:k]
        temp = 0
        vowel = 'aeiou'

        for i in tempStr:
            if i in vowel:
                temp += 1

        maxLen = max(0,temp)

        for i in range(k,len(s)):
            if s[i] in vowel:
                temp += 1
            if s[i-k] in vowel:
                temp -= 1

            maxLen = max(maxLen,temp)

        return maxLen
