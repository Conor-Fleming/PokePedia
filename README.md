# PokePedia
This is small application written for submission for the hackathon at [Boot.dev](https://boot.dev/). I would classify myself in the over 1 year of coding category. The requirements of the submission were: 
- Written in Python3
- Make use of the [PokeAPI](https://pokeapi.co/)

I wanted to participate but wanted to keep it simple as the time alotted was short and I also had work on the day of submission.

The application acts as a basic encyclopedia for any Pokemon. Enter the name of a Pokemon to view a list of its Name, Height, Weight, Abilities, Moves, Forms, Species, and Types.

## Usage
To run PokePedia locally (_assuming user is on Mac or Linux machine_)
```
git clone https://github.com/Conor-Fleming/BDProjects/
```

Navigate to the source directory:
```
cd BDProjects/PokePedia
```

Create a virtual environment:
```
python<version> -m venv <virtual-environment-name>
```
Like so:
```python3 -m venv env```

Activate the virtual environment:
```
source venv/bin/activate
```

Install dependencies:

```sh
pip install -r requirements.txt
```

Run the program with:

```sh
python main.py
```
PokePedia will recognize the commands:\
```list``` - view a list of 5 random Pokemon\
```clear``` - clear screen\
```quit``` - terminate program and exit\
```[name of pokemon]``` - view stats for Pokemon entered