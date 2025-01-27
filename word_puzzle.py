import tkinter as tk
import random

class WordPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Puzzle Game")

        self.word_list = ["apple", "banana", "cherry", "grape", "orange"]
        self.current_word = ""
        self.scrambled_word = ""
        self.score = 0

        self.label = tk.Label(root, text="Welcome to Word Puzzle Game!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 12))
        self.score_label.pack()

        self.word_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 16))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_answer)

        self.new_word_button = tk.Button(root, text="New Word", command=self.new_word)
        self.new_word_button.pack()

        self.new_word()

    def new_word(self):
        self.current_word = random.choice(self.word_list)
        self.scrambled_word = "".join(random.sample(self.current_word, len(self.current_word)))
        self.word_label.config(text=self.scrambled_word)
        self.entry.delete(0, tk.END)

    def check_answer(self, event):
        user_input = self.entry.get().lower()
        if user_input == self.current_word:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.new_word()

if __name__ == "__main__":
    root = tk.Tk()
    game = WordPuzzleGame(root)
    root.mainloop()
