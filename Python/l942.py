# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]

class Solution:
    def diStringMatch(self, S: 'str') -> 'List[int]':
        maximum = len(S)
        minimum = 0
        A = []
        for item in S:
            if item == "D":
                A.append(maximum)
                maximum -= 1
            else:
                A.append(minimum)
                minimum += 1
        A.append(minimum)
        return A
