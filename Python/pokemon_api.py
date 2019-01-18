import requests
import termcolor
from pyfiglet import Figlet
f = Figlet(font='big')

ascii = f.renderText("Choose Your Pokemon!")
text = termcolor.colored(ascii, "cyan")
print(text)
y = 0
while y == 0:
    x = 0
    while x == 0:
        number = input("Enter a number between 1 & 721:\n")
        try:
            number = int(number)
        except ValueError:
            print("Please enter a number.")
            continue
        if number > 0 and number < 722:
            x = 1
    url = f"https://pokeapi.co/api/v2/pokemon-species/{number}"
    response = requests.get(url, headers={"Accept":"application/json"})

    data = response.json()
    name = data["name"]
    name = name[0].upper() + name[1::]
    color_name = termcolor.colored(name, "yellow")
    print(f"You have chosen {color_name}!\n")
    print(f"Here is a description of your new pokemon, {color_name}:\n")
    try:
        print(data["flavor_text_entries"][1]["flavor_text"] + "\n")
    except UnicodeEncodeError:
        print(data["flavor_text_entries"][2]["flavor_text"] + "\n")
    play_again = input("Would you like to pick another pokemon? (y/n):\n").lower()
    if play_again == "n":
        y = 1
