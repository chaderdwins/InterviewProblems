class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d, c = {}, {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        for char in t:
            if char in c:
                c[char] += 1
            else:
                c[char] = 1
        print(d)
        print(c)
        return list(d.values()) == list(c.values())

s = Solution()
print(s.isIsomorphic('add', 'egg'))