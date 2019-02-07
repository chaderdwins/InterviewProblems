# You have a list of words and a pattern, and you want to know which words in words
# matches the pattern. A word matches the pattern if there exists a permutation of
# letters p so that after replacing every letter x in the pattern with p(x),
# we get the desired word.
#
# (Recall that a permutation of letters is a bijection from letters to letters:
# every letter maps to another letter, and no two letters map to the same letter.)
#
# Return a list of the words in words that match the given pattern. You may return
# the answer in any order.
#
# Example 1:
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
# since a and b map to the same letter.

class Solution:
    def findAndReplacePattern(self, words: 'List[str]', pattern: 'str') -> 'List[str]':
        li = []
        count = 0
        temp_li = []
        for item in pattern:
            if item not in temp_li:
                temp_li.append(item)
        d = {}
        for num in temp_li:
            d[num] = count
            count += 1
        seq = ''
        for char in pattern:
            seq += str(d[char])

        for word in words:
            phase_set = []
            for item in word:
                if item not in phase_set:
                    phase_set.append(item)
            print(phase_set)
            d = {}
            i = 0
            for item in phase_set:
                d[item] = i
                i += 1
            print(d)
            translate = ''
            for char in word:
                translate += str(d[char])
            # print(translate)
            if translate == seq:
                li.append(word)
        return li



s = Solution()
print(s.findAndReplacePattern(["ab","cd","fe","gg"],"ab"))
