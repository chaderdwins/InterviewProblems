# Write a function called reverse_vowels. This function should reverse the vowels
# in a string. Any characters which are not vowels should remain in their original
# position. You should not consider "y" to be a vowel.

#for some reason this problem gave me trouble. I came up with a rather hacky solution

def reverse_vowels(st):
    vowels = 'aeiou'
    st = list(st)
    li = []
    for item in range(len(st)):
        if st[item].lower() in vowels:
            li.append(item)

    y = len(li) - 1
    for x in range(len(li)):
        if len(li) % 2 == 1:
            if x == y: break
        else:
            if y < len(li) // 2: break
        st[li[x]], st[li[y]] = st[li[y]], st[li[x]]
        y -= 1
    return ''.join(st)

print(reverse_vowels("Reverse Vowels In A String"))
