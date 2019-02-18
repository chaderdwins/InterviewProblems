# Given a string S, return the "reversed" string where all characters that are not a letter 
# stay in the same place, and all letters reverse their positions.

# Example 1:
# Input: "ab-cd"
# Output: "dc-ba"

# Example 2:
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

# Example 3:
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

# Note:
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S doesn't contain \ or "


class Solution:
    def reverseOnlyLetters(self, S: 'str') -> 'str':
        if len(S) < 1:
            return ""
        li, d , final = [], {}, []
        alpha = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAMNBVCXZ'
        for i in range(len(S)):
            if S[i] not in alpha:
                d[i] = S[i]
            else:
                li.append(S[i])
        for i in range(len(S)):
            if i in d:
                final.append(d[i])
            else:
                final.append(li.pop())
        return ''.join(final)