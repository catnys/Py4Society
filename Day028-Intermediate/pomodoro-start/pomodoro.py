import tkinter as tk
from tkinter import PhotoImage, Canvas
from threading import Timer

# ---------------------------- CONSTANTS ------------------------------- #
WORK_TIME = 25 * 60  # 25 minutes
SHORT_BREAK = 5 * 60  # 5 minutes
LONG_BREAK = 15 * 60  # 15 minutes
FONT_NAME = "Courier"


class Pomodoro:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro")
        self.root.config(padx=100, pady=50)

        self.timer = None
        self.is_running = False
        self.sessions = 0
        self.time_left = WORK_TIME

        self.create_widgets()

    def create_widgets(self):
        # Create the canvas with a fixed size and a centered image
        self.canvas = Canvas(width=200, height=224, bg='white', highlightthickness=0)
        self.tomato_img = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_img)  # Center the image
        self.timer_text = self.canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)  # Place the canvas in the center

        # Create and position the buttons
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.grid(column=0, row=2)  # Place the start button to the left

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_timer)
        self.stop_button.grid(column=1, row=2)  # Place the stop button in the center below the canvas

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_timer)
        self.reset_button.grid(column=2, row=2)  # Place the reset button to the right

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.countdown()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            if self.timer:
                self.timer.cancel()

    def reset_timer(self):
        self.stop_timer()
        self.sessions = 0
        self.time_left = WORK_TIME
        self.update_timer_label()

    def countdown(self):
        if self.is_running:
            minutes, seconds = divmod(self.time_left, 60)
            self.canvas.itemconfig(self.timer_text, text=f"{minutes:02d}:{seconds:02d}")
            if self.time_left > 0:
                self.time_left -= 1
                self.timer = Timer(1, self.countdown)
                self.timer.start()
            else:
                self.is_running = False
                self.sessions += 1
                if self.sessions % 8 == 0:
                    self.time_left = LONG_BREAK
                elif self.sessions % 2 == 0:
                    self.time_left = SHORT_BREAK
                else:
                    self.time_left = WORK_TIME
                self.update_timer_label()
                self.start_timer()

    def update_timer_label(self):
        minutes, seconds = divmod(self.time_left, 60)
        self.canvas.itemconfig(self.timer_text, text=f"{minutes:02d}:{seconds:02d}")

