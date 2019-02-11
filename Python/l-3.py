# Given a string, find the length of the longest substring without repeating characters.

# Example 1:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        d , temp, final, i = {}, 0, 0, 0
        while i < len(s):
            if s[i] in d:
                i, d, temp= d[s[i]] + 1, {}, 0
                continue
            else:
                d[s[i]] = i
                temp += 1
                if temp > final:
                    final = temp
            i += 1
        return final

s = Solution()
print(s.lengthOfLongestSubstring("ddvdf"))
        
