# Write your code here
import random
import sys

list_of_words = ["python", "java", "swift", "javascript"]
print("H A N G M A N #\n")
word = random.choice(list_of_words)

letter_list = []
aantal_kansen = 8

def get_hidden_word():
    hidden = ''
    for ch in word:
        if ch in letter_list:
            hidden += ch
        else:
            hidden += '-'

    return hidden

while aantal_kansen > 0:
    print(get_hidden_word())
    letter = input('Input a letter: ')

    if len(letter) != 1:
        print("Please, input a single letter.")
    elif not letter.islower():
        print("Please, enter a lowercase letter from the English alphabet")
    elif letter in letter_list:
        print("You've already guessed this letter.")
    elif letter not in word:
        print("That letter doesn't appear in the word.")
        aantal_kansen -= 1

    # print(f'# {aantal_kansen} attempts')

    letter_list.append(letter)
    print('')
    if '-' not in get_hidden_word():
        break  # GEWONNEN!!!

if aantal_kansen == 0:
    print("You lost!")
else:
    print("You guessed the word " + word + "!")
    print("You survived!")
