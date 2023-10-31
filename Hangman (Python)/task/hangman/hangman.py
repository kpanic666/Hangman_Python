import random

MAX_ATTEMPTS = 8
GAME_FIELD_MASK = "-"

words_list = frozenset({'python', 'java', 'swift', 'javascript'})
guessed_word = random.choice(list(words_list))
left_attempts = MAX_ATTEMPTS
game_field = list(GAME_FIELD_MASK * len(guessed_word))


def update_game_field(letter):
    global game_field

    if letter not in guessed_word:
        print("That letter doesn't appear in the word.")
        return
    elif letter in game_field:
        return
    else:
        for i in range(len(guessed_word)):
            if guessed_word[i] == letter:
                game_field[i] = letter


print("H A N G M A N")

while left_attempts > 0:
    print()
    print(''.join(game_field))
    user_letter = input("Input a letter: ")
    update_game_field(user_letter)
    left_attempts -= 1

print("\nThanks for playing!")