import random
# used to select a random word from wordlist
words = [
    "other",
    "there",
    "which",
    "their",
    "about",
    "write",
    "would",
    "these",
    "thing",
    "could",
    "sound",
    "water",
    "first",
    "place",
    "where",
    "after",
    "round",
    "every",
    "under",
    "great",
    "think",
    "cause",
    "right",
    "three",
    "small",
    "large",
    "spell",
    "light",
    "house",
    "again",
    "point",
    "world",
    "build",
    "earth",
    "stand",
    "found",
    "study",
    "still",
    "learn",
    "plant",
    "cover",
    "state",
    "never",
    "cross",
    "start",
    "might",
    "story",
    "don't",
    "while",
    "press",
    "close",
    "night",
    "north",
    "white",
    "begin",
    "paper",
    "group",
    "music",
    "those",
    "often",
    "until",
    "river",
    "carry",
    "began",
    "horse",
    "watch",
    "color",
    "plain",
    "usual",
    "young",
    "ready",
    "above",
    "leave",
    "black",
    "short",
    "class",
    "order",
    "south",
    "piece",
    "since",
    "whole",
    "space",
    "heard",
    "early",
    "reach",
    "table",
    "vowel",
    "money",
    "serve",
    "voice",
    "power",
    "field",
    "pound",
    "drive",
    "stood",
    "front",
    "teach",
    "final",
    "green",
    "quick",
    "ocean",
    "clear",
    "wheel",
    "force",
    "plane",
    "stead",
    "laugh",
    "check",
    "shape",
    "bring",
    "paint",
    "among",
    "grand",
    "heart",
    "heavy",
    "dance",
    "speak",
    "count",
    "store",
    "train",
    "sleep",
    "prove",
    "catch",
    "mount",
    "board",
    "glass",
    "grass",
    "visit",
    "month",
    "happy",
    "eight",
    "raise",
    "solve",
    "metal",
    "seven",
    "third",
    "shall",
    "floor",
    "coast",
    "value",
    "fight",
    "sense",
    "quite",
    "broke",
    "scale",
    "child",
    "speed",
    "organ",
    "dress",
    "cloud",
    "quiet",
    "stone",
    "climb",
    "stick",
    "smile",
    "trade",
    "mouth",
    "exact",
    "least",
    "shout",
    "wrote",
    "clean",
    "break",
    "blood",
    "touch",
    "brown",
    "equal",
    "woman",
    "whose",
    "radio",
    "spoke",
    "human",
    "party",
    "agree",
    "won't",
    "chair",
    "fruit",
    "thick",
    "guess",
    "sharp",
    "crowd",
    "sight",
    "hurry",
    "chief",
    "clock",
    "enter",
    "major",
    "fresh",
    "allow",
    "print",
    "block",
    "chart",
    "event",
    "quart",
    "truck",
    "noise",
    "level",
    "throw",
    "shine",
    "wrong",
    "broad",
    "anger",
    "claim",
    "sugar",
    "death",
    "skill",
    "women",
    "thank",
    "match",
    "steel",
    "guide",
    "score",
    "apple",
    "pitch",
    "dream",
    "total",
    "basic",
    "smell",
    "track",
    "shore",
    "sheet",
    "favor",
    "spend",
    "chord",
    "share",
    "bread",
    "offer",
    "slave",
    "chick",
    "enemy",
    "reply",
    "drink",
    "occur",
    "range",
    "steam",
    "meant",
    "teeth",
    "shell",
]
# wordle's wordlist
print("----------WORDLE----------")
# prints header
word = random.choice(words).upper()
# chooses a random word from the list above and sets 'word's value to it
filename1 = 'one.txt'
filename2 = 'two.txt'
filename3 = 'three.txt'
filename4 = 'four.txt'
filename5 = 'five.txt'
filename6 = 'six.txt'
# sets variables to access files in direc


def read_value(filename):
    try:
        with open(filename, 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 0
# sets function to read text files in direc


def write_value(filename, guess_num):
    with open(filename, 'w') as file:
        file.write(str(guess_num))

# sets function to write values to text files in direc


stats1 = read_value(filename1)
stats2 = read_value(filename2)
stats3 = read_value(filename3)
stats4 = read_value(filename4)
stats5 = read_value(filename5)
stats6 = read_value(filename6)

# sets stats to current values for later use. each no. correlates to 1st guess etc.

for guess_num in range(1, 7):
    # makes it so you only have 6 guesses and that you begin on guess 1
    correct_letters = set()
    misplaced_letters = set()
    wrong_letters = set()
    guess = input(f"\nGuess {guess_num} : ").upper()
    # input for word guess, tells you what guess number you're on
    if guess == word:
        print("Correct!")
        print(f"\nYou guessed on the {guess_num} guess!")
        average = guess_num
        if guess_num == 1:
            first_guess = read_value(filename1)
            first_guess += 1
            write_value(filename1, first_guess)
        elif guess_num == 2:
            secondguess = read_value(filename2)
            secondguess += 1
            write_value(filename2, secondguess)
        elif guess_num == 3:
            thirdguess = read_value(filename3)
            thirdguess += 1
            write_value(filename3, thirdguess)
        elif guess_num == 4:
            fourthguess = read_value(filename4)
            fourthguess += 1
            write_value(filename4, fourthguess)
        elif guess_num == 5:
            fifthguess = read_value(filename5)
            fifthguess += 1
            write_value(filename5, fifthguess)
        elif guess_num == 6:
            sixthguess = read_value(filename6)
            sixthguess += 1
            write_value(filename6, sixthguess)
        # reads your current amount of guesses for this play through and updates relevant var in txt file
        print("Stats:")
        print(f"\n Times guessed first: {stats1}")
        print(f"\n Times guessed second: {stats2}")
        print(f"\n Times guessed third: {stats3}")
        print(f"\n Times guessed fourth: {stats4}")
        print(f"\n Times guessed fifth: {stats5}")
        print(f"\n Times guessed sixth: {stats6}")
        # prints your current all-time statistics with guesses
        quit()

    for letter, correct in zip(guess, word):
        # reads what letters are in 'word' and compares them to 'guess'
        if letter == correct:
            correct_letters.add(letter)
            # checks correct letters in guess and adds them to correct_letters
        elif letter in word:
            misplaced_letters.add(letter)
            # adds letters that are IN the word but not in the correct position to misplaced_letters
        else:
            wrong_letters.add(letter)
            # adds all letters in 'guess' that aren't in 'word' to wrong_letters

    misplaced_letters -= correct_letters
    # removes the correctly placed letters from the misplaced letters word list
    print("Correct Letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced Letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong Letters:", ", ".join(sorted(wrong_letters)))
    # prints correct, misplaced, and wrong letters in alphabetical order
else:
    print("Game Over! The correct answer was: " + word.lower())
    quit()
