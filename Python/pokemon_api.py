import requests
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
print(f"You have chosen {name} to be your Pokemon!\n")
print(f"Here is a description of your new pokemon, {name}:\n")
print(data["flavor_text_entries"][1]["flavor_text"])
