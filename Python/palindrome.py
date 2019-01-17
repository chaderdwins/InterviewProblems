'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(string):
    sting = string.replace(" ", "")
    print(f"Is {sting} a palindrome? Let's find out:")
    return sting == sting[::-1]

print(is_palindrome("testing"))
print(is_palindrome("tacocat"))
print(is_palindrome("hannah"))
print(is_palindrome("robert"))
print(is_palindrome("am an aplanac an alp an ama"))
