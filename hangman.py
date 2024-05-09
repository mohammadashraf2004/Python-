import tkinter as tk
import random

words = ["python", "programming", "computer", "algorithm", "function", "syntax"]

hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]

def choose_word():
    return random.choice(words)

def update_hangman(mistakes):
    hangman_label.config(text=hangman_art[mistakes], font=("Courier", 14))

def check_guess(guess):
    global word_with_blanks
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                word_with_blanks = word_with_blanks[:i] + guess + word_with_blanks[i+1:]
        word_label.config(text=word_with_blanks, font=("Arial", 24))
        if "_" not in word_with_blanks:
            end_game("win")
    else:
        global mistakes
        mistakes += 1
        update_hangman(mistakes)
        if mistakes == 6:
            end_game("lose")

def guess():
    global mistakes
    guess = guess_entry.get()
    if len(guess) == 1 and guess.isalpha():
        check_guess(guess.lower())
    else:
        result_label.config(text="Invalid guess! Please enter a single letter.")
        return

def end_game(result):
    if result == "win":
        result_text = "Congratulations! You guessed the word correctly!"
    else:
        result_text = f"You Lose, the word was {word}"
    result_label.config(text=result_text, font=("Arial", 18))
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")

root = tk.Tk()
root.title("Hangman")

hangman_label = tk.Label(root, font=("Courier", 14))
hangman_label.grid(row=0, column=0, pady=20)

word = choose_word()
word_with_blanks = "_ " * len(word)
word_label = tk.Label(root, text=word_with_blanks, font=("Arial", 32))
word_label.grid(row=1, column=0, pady=20)

guess_entry = tk.Entry(root, width=3, font=("Arial", 24))
guess_entry.grid(row=2, column=0, pady=20)
guess_button = tk.Button(root, text="Guess", command=guess, font=("Arial", 18))
guess_button.grid(row=2, column=1, pady=20)

result_label = tk.Label(root, font=("Arial", 18))
result_label.grid(row=3, column=0, pady=20)

mistakes = 0
update_hangman(mistakes)

root.mainloop()

