# Simple Hangman for the word "HANGAN"

word = list("HANGAN")  # ['H','A','N','G','A','N']
display = ['_'] * len(word)
lives = len(word)
guessed = set()

def print_display():
    print("Word: " + " ".join(display))

print(f"Word length: {len(word)}")
print_display()

while lives > 0:
    print(f"\nLives: {lives}")
    user_guess = input("Guess a letter: ").strip().upper()

    
    if len(user_guess) != 1 or not user_guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue

    if user_guess in guessed:
        print(f"You already guessed '{user_guess}'. Try another letter.")
        continue

    guessed.add(user_guess)

    if user_guess in word:

        found_any = False
        for i, ch in enumerate(word):
            if ch == user_guess and display[i] == '_':
                display[i] = user_guess
                found_any = True

        print_display()

        if '_' not in display:
            print("You win! The word was:", "".join(word))
            break
    else:
        lives -= 1
        print(f"'{user_guess}' is not in the word.")
        print_display()

# Lose condition
if '_' in display and lives == 0:
    print("Out of lives! The word was:", "".join(word))
