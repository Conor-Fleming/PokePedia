import requests
import random

def list():
    #using a randomly generated list of ids to get the 5 random pokemon names
    #might not be the most efficient way to do this but it was quick and the method that I got working the fastest.
    randlist = random.sample(range(1, 100), 5)
    for val in randlist:
        url = f"https://pokeapi.co/api/v2/pokemon/{val}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: the request failed with status code {response.status_code}")

        data = response.json()
        print(data['name'])
    print()
    
