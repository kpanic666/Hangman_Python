import random
import string

MAX_ATTEMPTS = 8
GAME_FIELD_MASK = "-"

words_list = frozenset({'python', 'java', 'swift', 'javascript'})
guessed_word = random.choice(list(words_list))
guessed_letters = set()
left_attempts = MAX_ATTEMPTS
game_field = list(GAME_FIELD_MASK * len(guessed_word))
win_flag = False


def update_game_field(letter):
    global game_field, guessed_letters, left_attempts

    guessed_letters.add(letter)

    if letter not in guessed_word:
        print("That letter doesn't appear in the word.")
        left_attempts -= 1
        return
    else:
        for i in range(len(guessed_word)):
            if guessed_word[i] == letter:
                game_field[i] = letter


def check_win_conditions(game_field) -> bool:
    return True if GAME_FIELD_MASK not in game_field else False


def print_game_field(game_field):
    print()
    print(''.join(game_field))


def check_user_input(user_input) -> bool:
    if len(user_input) != 1:
        print("Please, input a single letter.")
        return False

    if user_input.isupper() or user_input not in string.ascii_letters:
        print("Please, enter a lowercase letter from the English alphabet.")
        return False

    if user_input in guessed_letters:
        print("You've already guessed this letter.")
        return False

    return True

print("H A N G M A N")

while left_attempts > 0 and not check_win_conditions(game_field):
    print_game_field(game_field)
    user_letter = input("Input a letter: ")
    if not check_user_input(user_letter):
        continue
    update_game_field(user_letter)

if check_win_conditions(game_field):
    print_game_field(game_field)
    print("You guessed the word " + "".join(guessed_word) + "!")
    print("You survived!")
else:
    print()
    print("You lost!")
