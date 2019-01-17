inti = 12
# in the first solution we are taking the value of the binary
# word and essentially looping through the word itself, time complexity
# is dependent on the length of the binary word
def stringParity(x):
        random = 0
        while x:
            random = random ^ (x & 1)
            x = x >> 1  #paying attention to only the last binary digit
        print("Brute force solution:",random)   #returns 0 if parity is even, otherwise returns 1

stringParity(inti)

#Optimization of stringParity

# in this solution we dont pay attention to the word itself, we simply delete the lowest
# bit and toggle result between 0 and 1 for odd and even amounts

def optParity(x):
    result = 0
    while x:
        result = result ^ 1 #result starts at 0000, and for each 1 present in the word it toggles to 0001 and back again
        x = x & (x-1)   #this drops the lowest bit in the word, i.e. 1100 -> 1000 -> 0000, then the while loop terminates
    print("Optimized solution:",result)

optParity(inti)
