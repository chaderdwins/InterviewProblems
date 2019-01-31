import unittest

# Assume you have a method isSubstring which checks if one word is a substring of
# another. Given two strings, s1 & s2, write code to check if s2 is a rotation of
# s1 using only one call to isSubstring (e.g. "waterbottle" is a rotation of "erbottlewat")

def string_rotation(st1, st2):
    if len(st1) == len(st2):
        st1 = st1 + st1 #trick to finding a string rotation is add the string together!
        return st1.find(st2) != -1
    return False


# unit testing
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
