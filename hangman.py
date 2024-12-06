import random
import os

random_words = [
  "quartz", "nebula", "archive", "ember", "gargoyle", "foliage", "cipher",
  "lattice", "paradox", "eclipse", "crimson", "oasis", "labyrinth", "horizon",
  "juncture", "specter", "ripple", "voyage", "artifact", "whimsy", "haven",
  "zenith", "verbatim", "cascade", "alchemy", "mosaic", "tundra", "arbor",
  "echo", "phoenix", "haven", "solstice", "mirage", "grove", "plume", "quasar",
  "serenade", "aurora", "fracture", "fossil", "meadow", "temple", "basilica",
  "lantern", "quiver", "prism", "ember", "sphinx", "galleon", "zephyr", "omen",
  "pebble", "harbinger", "verdant", "rune", "thistle", "keystone", "sepia",
  "horizon", "mandate", "rift", "scepter", "vortex", "lexicon", "harbor",
  "crescent", "tether", "glimmer", "beacon", "rhapsody", "paragon", "torrent",
  "verdure", "vantage", "spire", "pinnacle", "oblivion", "reverie", "serendipity",
  "quaint", "elixir", "labyrinthine", "ember", "effigy", "havoc", "parapet",
  "caliber", "mantle", "obscure", "perennial", "quagmire", "rift", "sanctum",
  "shard", "sublime", "taciturn", "verge", "zealot", "ethereal", "euphoria",
  "enigma", "palisade"
]

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
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
=========''', '''
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
''']

random_word = random.choice(random_words)
split_word = list(random_word)
output_list = ["_"] * len(split_word)
guessed_chars = []
lives = 6

def print_output():
  print("\n")
  print(stages[lives])
  if bool(lives):
    if lives > 1:
      print(f"\nYou have {lives} lives remaining\n")
    else:
      print("\nOnly one life remaining, choose wisely!\n")

  print("The word: \n")
  print(" ".join(output_list))
  if bool(len(guessed_chars)):
    print("\nLetters used:\n")
    print(", ".join(guessed_chars))

def handle_guess(guess):
  global lives
  print("\n")
  guess = guess.lower()
  if guess in guessed_chars:
    print(f"You've already tried '{guess}', stoopid!\n")
    lives -= 1
    return
  else:
    guessed_chars.append(guess)

  if guess in split_word:
    print(f'Boom, {guess} is in the word! Look!\n')
    correct_guess_indices = []
    for index, char in enumerate(split_word):
      if char == guess:
        correct_guess_indices.append(index)
    if bool(len(correct_guess_indices)):
      for correct_guess in correct_guess_indices:
        output_list[correct_guess] = guess
  else:
    print(f"Sorry, but {guess} ain't in this word!\n")
    lives -= 1
    if bool(lives):
      print("Try again...")

print('\nWelcome to hangman!')
while "_" in output_list and bool(lives):
  print_output()
  print("\n")
  guess = input("Choose a letter: ")
  os.system('cls' if os.name == 'nt' else 'clear')
  handle_guess(guess)

if "_" not in output_list:
  print(f"Congratulations! {random_word} was the word!!")
  print_output()
else:
  print("Uh oh!!")
  print_output()
  print(f"The word you were looking for was {random_word}, but you're dead now, so you probably don't care. Bye!")