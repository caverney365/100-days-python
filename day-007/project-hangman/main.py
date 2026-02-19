import random

from source import hangman_art, hangman_words

print(hangman_art.logo)
print("===============================================")
play_game = input("Want to play hangman? ").lower()
game_start = False

if play_game in ["yes", "y"]:
    game_start = True

    easy = 6
    normal = 4
    hard = 2

    lives = 0

    level = input('Choose game difficulty: "Easy", "Normal", or "Hard"? ').lower()

    if level == "hard":
        lives = hard
    elif level == "normal":
        lives = normal
    elif level == "easy":
        lives = easy

    category, chosen_list = random.choice([
        ("Animal", hangman_words.animals),
        ("Fruit", hangman_words.fruits)
    ])

    hidden_word = random.choice(chosen_list)
    guessed_letters = []

    max_lives = lives
    hint_shown = False

display = ["_"] * len(hidden_word)

while game_start and lives > 0:

    print("=============================================")
    print(hangman_art.stages[lives])
    print(f"Lives: {lives}")

    if level == "easy" and not hint_shown:
        print(f"Hint: it's a {category}")
        hint_shown = True
    elif level == "normal" and lives <= max_lives // 2 and not hint_shown:
        print(f"Hint: it's a {category}")
        hint_shown = True

    print("Word to guess:", " ".join(display).upper())

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in hidden_word:
        for position in range(len(hidden_word)):
            if hidden_word[position] == guess:
                display[position] = guess
        print("Correct!")
    else:
        lives -= 1
        print("Wrong answer!")

    if "_" not in display:
        print("Congrats! You guessed the hidden word.")
        game_start = False

    if lives == 0:
        print(f"You lose! The hidden word was {hidden_word.upper()}.")
        game_start = False

else:
    game_start = False
    print("Goodbye!")