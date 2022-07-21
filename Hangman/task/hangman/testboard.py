# Write your code here
import random
import sys
aantal_from_play = 0
list_of_words = ["python", "java", "swift", "javascript"]
print("H A N G M A N # "+ '\n')
letter_list = []

def name(string):
    list_numbers = []
    for index ,letter in enumerate(word):
        if letter == string:
            list_numbers.append(index)
    return list_numbers

def count_letters(letter):
    return letter_list.count(letter)

def function(string, list_numbers):
    for number in list_numbers:
        for letter in word:
            if letter == string:
                global word2
                word2 = word2[:number] + string + word2[number+1:]
                word2 = word2
    return word2

def get_hidden_word(word):
    hidden = ''
    for ch in word:
        if ch in letter_list:
            hidden += ch
        else:
            hidden += '-'
    return hidden

def play(word):
    letter_list.clear()
    aantal_kansen = 8
    while aantal_kansen > 0:
        print(get_hidden_word(word))
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
        if '-' not in get_hidden_word(word):
            break  # GEWONNEN!!!
    if aantal_kansen == 0:
        return "You lost!"
    else:
        print("You guessed the word " + word + "!")
        return "You survived!"




aantal_keer_gewonen = 0
aantal_keer_verloren = 0
list_of_plays = []
while True:
    what_doe_you_want_to_doe = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    print("")
    if what_doe_you_want_to_doe == "play":

        play2 = play(random.choice(list_of_words))

        print(play2)
        if play2 == "You survived!":
            aantal_keer_gewonen += 1
        if play2 == "You lost!":
            aantal_keer_verloren += 1
    elif what_doe_you_want_to_doe == "results":
        print("You won: " + aantal_keer_gewonen + "times .")
        print("You lost: " + aantal_keer_verloren + "times .")
    else:
        sys.exit(0)