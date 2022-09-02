import requests

def poke(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response = requests.get(url)

    data = response.json()
    stats(data)

#Validate func takes the user input via name variable and then checks the status code of the get request
# if not successful(200) it will return false and continue to the else statement in the while loop in main.py    
def validate(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Check your spelling, otherwise the Pokemon you are searching might not exist in the dataset.")
        return False
    return True

#stats func handles the printing/formatting of poke data
def stats(data):
    print(f"\n{data['name'].upper()}")
    print("-----------------------------")

    #display height and weight values
    print(f"Height: {data['height']}")
   
    print(f"Weight: {data['weight']}\n")
    
    print("Abilities:")
    for val in data['abilities']:
        print(f"\t{val['ability']['name']}")

    print("Moves:")
    for val in data['moves']:
        print(f"\t{val['move']['name']}")

    print("Forms:")
    for val in data['forms']:
        print(f"\t{val['name']}")

    print(f"Species: \n\t{data['species']['name']}")

    print("Types:")
    for val in data['types']:
        print(f"\t{val['type']['name']}")

    print("\n")


