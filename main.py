from list import list
from poke import poke, validate
import os

def main():

    welcome()
    while True:
        command = input()
        if command == "list":
            list()
        elif command == "quit":
            break
        elif command == "clear":
            os.system('clear')
            welcome()
        #validate user input as valid pokemon
        elif validate(command) == True:
            poke(command)
        else:
            print("\nEnter a Pokemon name to view stats, or use 'list' for some sample names")
            print("Use 'quit' to exit.\n")     
    print("Goodbye!")

#Welcome handles the printing of the welcome message/info
#cleaning up main loop by using function for printing
def welcome():
    print("Welcome to PokePedia, to view a Pokemon's stats please input its name.")
    print("If you need some ideas to get started, use the command 'list', to view a list of Pokemon.")
    print("Use 'quit' to exit PokePedia. If you need to clear the screen use 'clear'\n")

if __name__ =='__main__':
    main()



