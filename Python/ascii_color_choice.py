import termcolor
from pyfiglet import Figlet
f = Figlet(font='starwars')
# print(f.renderText('text to render'))

greeting = input("What message do you want to include?\n")
x = 0
while x == 0:
    color = input(
        "Choose a color from the following: grey, red, green, yellow, blue, magenta, cyan, white\n").lower()
    li = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    if color not in li:
        print("Error: please choose a color from the given list.")
    else:
        x = 1
# colors: grey, red, green, yellow, blue, magenta, cyan, white

ascii = f.renderText(greeting)
text = termcolor.colored(ascii, color)
print(text)
