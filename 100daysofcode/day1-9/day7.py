# DAY 7 PROJECT - HANGMAN
import random
import unicodedata

def normalize_string(s):
    s = s.lower()
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


word_list = [
    "aadvark", "bee", "beetle", "sloth", "goat", "hot dog",
    "dog", "kangaroo", "horse", "seahorse", "deer", "jackal",
    "chimpanzee", "owl", "coyote", "dingo", "elephant", "seal", "ferret",
    "rooster", "cat", "giraffe", "dolphin", "hamster", "iguana", "alligator",
    "ocelot", "lizard", "lion", "leopard", "lemur", "otter", "sheep",
    "panda", "parrot", "bird", "fish", "penguin", "porcupine",
    "guinea pig", "cougar", "fox", "mouse", "reindeer", "snake",
    "turtle", "tiger", "shark", "bear", "polar bear", "zebra", "wolf"
]

normalized_word_list = [normalize_string(word) for word in word_list]

stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]

chosen_word = random.choice(word_list)
normalized_chosen_word = normalize_string(chosen_word)

display = ["_"] * len(chosen_word)

lives = 6
word_attempts = 2
guessed_letters = []
guessed_words = []

def reveal_letters(word, display):
    indices = [i for i, letter in enumerate(word) if display[i] == "_"]

    if len(indices) > 0:
        missing_letters = len(indices)

        if missing_letters <= 2:
            reveal_count = 1
        elif len(word) > 8:
            reveal_count = 2
        else:
            reveal_count = 1

        for _ in range(reveal_count):
            index_to_reveal = random.choice(indices)
            display[index_to_reveal] = word[index_to_reveal]
            indices.remove(index_to_reveal)

while True:
    print(stages[6 - lives])
    print(f"Lives: {lives}")
    print(" ".join(display))
    print(f"Letras tentadas: {', '.join(guessed_letters)}")
    print(f"Palavras tentadas: {', '.join(guessed_words)}")

    if lives == 2:
        reveal_letters(chosen_word, display)

    guess = input("Guess a letter or the word: ").lower()

    if len(guess) == 1:
        if guess in guessed_letters:
            print("You already tried this letter. Try another one.")
            continue

        guessed_letters.append(guess)
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = guess
        else:
            lives -= 1
            print("Wrong guess! You lost a life.")

    elif len(guess) > 1:
        if word_attempts > 0:
            if normalize_string(guess) == normalized_chosen_word:
                print(f"Congratulations! You guessed the word '{chosen_word}' and won!")
                break
            else:
                word_attempts -= 1
                lives -= 3
                guessed_words.append(guess)
                print(f"Wrong guess! You lost 3 lives. You have {word_attempts} word attempts remaining.")
        else:
            print("You have already used all your attempts to guess the word.")
    else:
        print("Invalid choice. Try again.")
        continue

    if "_" not in display:
        print(f"Congratulations! You completed the word '{chosen_word}' and won!")
        break
    if lives <= 0:
        print(stages[0])
        print(f"You lost! The word was '{chosen_word}'.")
        break
