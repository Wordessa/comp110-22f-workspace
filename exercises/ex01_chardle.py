"""EX01 - Chardle - A cute step towards Wordle."""
__author__ = "730580505"

five_char_word: str = input("Enter a 5-character word: ")
if len(five_char_word) != 5:
    print("Error: Word must contain 5 characters.")
    exit()

single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

instances: int = int(0)

print("Searching for " + single_character + " in " + five_char_word) 
if single_character == five_char_word[0]:
    print(single_character + " found at index 0")
    instances = instances + 1
if single_character == five_char_word[1]:
    print(single_character + " found at index 1")
    instances = instances + 1
if single_character == five_char_word[2]:
    print(single_character + " found at index 2")
    instances = instances + 1
if single_character == five_char_word[3]:
    print(single_character + " found at index 3")
    instances = instances + 1
if single_character == five_char_word[4]:
    print(single_character + " found at index 4")
    instances = instances + 1
    
print(str(int(instances)) + " instance of " + single_character + " found in " + five_char_word)

