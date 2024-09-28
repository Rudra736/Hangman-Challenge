# hangman_challenge_gui.py

import random
import tkinter as tk
from tkinter import messagebox

HANGMAN_WORDS = ["python", "java", "kotlin", "swift", "ruby"]

class HangmanChallengeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hangman Challenge")
        self.word = random.choice(HANGMAN_WORDS)
        self.guessed_word = ["_"] * len(self.word)
        self.incorrect_guesses = 6
        self.guessed_letters = []

        self.word_label = tk.Label(self.root, text=" ".join(self.guessed_word), font=("Arial", 24))
        self.word_label.pack(padx=10, pady=10)
        self.guess_entry = tk.Entry(self.root, width=20)
        self.guess_entry.pack(padx=10, pady=10)
        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack(padx=10, pady=10)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(padx=10, pady=10)

    def check_guess(self):
        guess = self.guess_entry.get().lower()

        if len(guess) != 1:
            self.result_label.config(text="Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            self.result_label.config(text="You already guessed this letter.")
            return

        self.guessed_letters.append(guess)

        if guess not in self.word:
            self.incorrect_guesses -= 1
            self.result_label.config(text="Incorrect guess!")
        else:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[i] = guess

        self.word_label.config(text=" ".join(self.guessed_word))
        self.result_label.config(text=f"Incorrect guesses remaining: {self.incorrect_guesses}")

        if "_" not in self.guessed_word:
            self.result_label.config(text="Congratulations! You won!")
            self.guess_button.config(state="disabled")
        elif self.incorrect_guesses == 0:
            self.result_label.config(text=f"Game over! The word was {self.word}.")
            self.guess_button.config(state="disabled")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = HangmanChallengeGUI()
    gui.run()