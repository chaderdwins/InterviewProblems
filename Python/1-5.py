import unittest

# There are 3 changes that can be made for strings: insert, remove, or replace a
# character. Given two strings, write a function to check if they are on edit away.

def one_away(st1, st2):
    count = 0
    if len(st1) > len(st2):
        for item in st1:
            if item not in st2:
                count += 1
    elif len(st2) > len(st1):
        for item in st2:
            if item not in st1:
                count +=1
    else:
        for item in st2:
            if item not in st1:
                count +=1
    if count > 1:
        return False
    return True


#unit testing
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
