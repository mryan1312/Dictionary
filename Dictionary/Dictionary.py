
import json                                                             # This program will take a user input and give
import os                                                               # a definition for the world. Includes suggestions        
from difflib import get_close_matches                                   # for similar words. -Matthew Adams

def main(word):
    data=json.load(open("data.json", 'r'))
    global working
    if word in data.keys():                                             # Key is found in the dict, printing value
        print(data[word])
        again = input("Continue? y or n\n").lower()                     # Go another round?
        if again == "y":
            pass
        else:                                                           # Closing the working loop to exit the program
            working = False
    elif len(get_close_matches(word, data.keys())) > 0:                 # Check to see if number of alts > 0
        correct = get_close_matches(word, data.keys())[0]               # Returns the closest related word
        accept = input(f"Did you mean {str(correct)}? y or n\n")
        if accept == "y":                                               # If alt is correct, pass it to main
            main(correct)
        else:
            print("Word not found, try again.\n")
            os.system('cls')
    else:                                                               # Word not found, no alternatives.
        print("Word not found, try again.\n")
        os.system('cls')

working = True
while working == True:                                                  # Keep it looping until we decide to quit
    word = input("What is your word?\n").lower()
    main(word)
print("Bye!")