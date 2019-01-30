import unittest

# implement a method to perform basic string compression using the counts of repeated
# characters. For example, the string aabcccccaaa would become a2b1c5a3. If the compressed
# string would not be smaller than the original string, return the original string.

def string_compression(st):
    i = 0
    k = 0
    new_string = ''
    while i < len(st):
        if i == len(st) - 1:
            new_string += st[i] + str(k+1)
            break
        if st[i] == st[i+1]:
            i += 1
            k += 1
            continue
        new_string += st[i] + str(k+1)
        i += 1
        k = 0
    return new_string

print(string_compression('aabcccccaaa'))

# unit testing
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3')
        # ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
