"""
You are given a string text. You can swap two of the characters in the text.

Return the length of the longest substring with repeated characters.

 

Example 1:
Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa" with length 3.

Example 2:
Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa" with length 6.

Example 3:
Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa" with length is 5.
"""

class Solution:
    def cal_max(self, hashTable):
        cur_max = 0
        max_val = None
        for key, value in hashTable.items():
            if value > cur_max:
                max_val = key
                cur_max = value
        return cur_max, max_val

    def maxRepOpt1(self, text: str) -> int:
        count = Counter(text)
        l = 0
        hashTable = {}
        res = 0

        for r in range(len(text)):
            hashTable[text[r]] = 1 + hashTable.get(text[r], 0)
            count[text[r]] -= 1
            cur_max, max_val = self.cal_max(hashTable)
            while (r - l + 1) - cur_max >= 2:
                # print(hashTable)
                hashTable[text[l]] -= 1
                count[text[l]] += 1
                l += 1
                cur_max, max_val = self.cal_max(hashTable)
                
            if (r - l + 1) - cur_max == 0:
                res = r - l + 1
            elif (r - l + 1) - cur_max == 1:
                if count[max_val] >= 1:
                    res = max(res, (r - l + 1))
        
        return res
