import tkinter as tk
from tkinter import messagebox
import time


class TypingSpeedTest(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test")
        self.geometry("800x400")

        # Sample text
        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.user_input_var = tk.StringVar()

        # Display sample text
        self.sample_label = tk.Label(self, text=self.sample_text, wraplength=700, justify=tk.LEFT)
        self.sample_label.pack(pady=(10, 0))

        # User input area
        self.user_input_entry = tk.Entry(self, textvariable=self.user_input_var, width=50)
        self.user_input_entry.pack(pady=(20, 10))
        self.user_input_entry.bind("<Return>", self.calculate_speed)

        # Typing speed display
        self.speed_label = tk.Label(self, text="")
        self.speed_label.pack()

    def calculate_speed(self, event=None):
        start_time = time.time()
        self.after(1000 * 60, lambda: self.end_test(start_time))  # Auto-end test after 1 minute

    def end_test(self, start_time):
        user_text = self.user_input_var.get().strip()
        elapsed_time = time.time() - start_time
        words_typed = len(user_text.split())
        wpm = round((words_typed / elapsed_time) * 60)

        accuracy = self.calculate_accuracy(user_text)

        self.speed_label.config(text=f"Your typing speed is {wpm} WPM with {accuracy}% accuracy.")

        # Optional: Show results in a messagebox
        messagebox.showinfo("Typing Speed Test Result", f"Your typing speed is {wpm} WPM with {accuracy}% accuracy.")

    def calculate_accuracy(self, user_text):
        correct_words = self.sample_text.split()
        typed_words = user_text.split()
        correct_count = sum(
            [1 for i in range(min(len(correct_words), len(typed_words))) if correct_words[i] == typed_words[i]])
        accuracy = round((correct_count / max(len(correct_words), len(typed_words))) * 100, 2)
        return accuracy


if __name__ == "__main__":
    app = TypingSpeedTest()
    app.mainloop()
