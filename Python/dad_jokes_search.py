import requests
import termcolor
from random import randint as r
from pyfiglet import Figlet
f = Figlet(font='big')

print(termcolor.colored(f.renderText("Dad Joke Generator"), "magenta"))

term = input("Let me tell you a joke. Give me a topic: ")

url = f"https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={"Accept":"application/json"},
    params={
    "term":term
    }
)

data = response.json()
length = len(data['results'])
print(f"I found {length} {term} joke(s). Here is one!\n")
i = 0
while i == 0:
    if length > 1:
        joke_number = r(0,length)
    else:
        joke_number = 0
    print(data['results'][joke_number]['joke'])
    if input(f"\nWould you like to hear another {term} joke?(y/n) ").lower() == "n":
        i = 1
