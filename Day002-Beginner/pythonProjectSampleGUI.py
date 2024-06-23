import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Graphical Calculator")
        self.master.geometry("400x500")
        self.master.configure(bg='white')

        self.equation_var = tk.StringVar()

        # Entry widget for displaying the result
        entry = ttk.Entry(self.master, textvariable=self.equation_var, font=('Helvetica', 24), justify='right', state='disabled')
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Configure grid weights to make the entry widget expandable
        for i in range(1, 5):
            self.master.grid_columnconfigure(i, weight=1)
            self.master.grid_rowconfigure(i, weight=1)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create buttons
        for (text, row, col) in buttons:
            button = ttk.Button(self.master, text=text, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, sticky='nsew')

    def button_click(self, value):
        if value == 'C':
            self.equation_var.set("")
        elif value == '=':
            try:
                result = eval(self.equation_var.get())
                self.equation_var.set(result)
            except Exception as e:
                self.equation_var.set("Error")
        else:
            current_value = self.equation_var.get()
            self.equation_var.set(current_value + str(value))

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
