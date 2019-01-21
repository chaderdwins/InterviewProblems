#test if a string has all unique characters

import unittest
#brute force implementation
# def unique(x):
#     d = {}
#     for char in x:
#         if char in d.keys():
#             return False
#         else:
#             d[char] = 1
#     for value in d.values():
#         if value > 1:
#             return False
#     return True

#optimized version
def unique(x):
    d = {}
    for char in x:
        if char in d:
            return False
        else:
            d[char] = 1
    return True

#unit testing for this function
class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
