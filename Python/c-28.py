# Write a function called valid_parentheses that takes a string
# of parentheses, and determines if the order of the parentheses is valid.valid_parentheses
# should return true if the string is valid, and false if it's invalid.
'''
valid_parentheses("()") # True
valid_parentheses(")(()))") # False
valid_parentheses("(") # False
valid_parentheses("(())((()())())") # True
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''
def valid_parentheses(st):
    counter = 0
    for item in st:
        if item == '(':
            counter += 1
        elif item == ')':
            counter -= 1
        if counter < 0: #if the counter ever goes below 0, it means a ) appeared w/o a (
            return False
    return counter == 0

print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))
print(valid_parentheses('))(('))
print(valid_parentheses('())('))
print(valid_parentheses('()()()()())()('))
