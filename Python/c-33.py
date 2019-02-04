# <p>Write a function called <strong>letter_counter</strong><strong> </strong>
# which accepts a string and returns a function. When the inner function is invoked
# it should accept a parameter which is a letter, and the inner function should
# return the number of times that letter appears. This inner function should be case
# insensitive.</p>
'''
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1
'''
def letter_counter(st):
    def inner(letter):
        return st.lower().count(letter.lower())
    return inner

counter = letter_counter('Amazing')
print(counter('a')) # 2
print(counter('m')) # 1

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i')) # 2
print(counter2('t')) # 1
