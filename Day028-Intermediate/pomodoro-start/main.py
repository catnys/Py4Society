import tkinter as tk
from pomodoro import Pomodoro

def main():
    root = tk.Tk()
    app = Pomodoro(root)
    root.mainloop()

if __name__ == '__main__':
    main()