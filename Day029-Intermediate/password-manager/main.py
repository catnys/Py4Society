from tkinter import *
import csv


def readFile(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        for row in csv_reader:
            print(row)


def writeFile(filename,data):
    header = data[0].keys()

    with open(filename, mode='w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=header)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def generatePasswordButtonClicked():
    """generatePasswordButtonClicked"""
    print("generatePasswordButtonClicked")


def saveButtonClicked():
    """saveButtonClicked"""
    print("saveButtonClicked")



def main():
    window = Tk()
    window.title('Password Manager')
    window.geometry('500x500')
    window.config(padx=20, pady=20, bg='#333333')  # Set background color

    # Canvas
    canvas = Canvas(window, width=200, height=200, bg='#333333', highlightthickness=0)
    logo = PhotoImage(file='logo.png')
    canvas.create_image(150, 150, image=logo)
    canvas.grid(row=0, column=0, columnspan=3, pady=20)  # Adjust padding

    # Labels
    websiteLabel = Label(window, text='Website', fg='white', bg='#333333')
    websiteLabel.config(font=('Calibri', 20))
    websiteLabel.grid(row=1, column=0, pady=5, sticky='e')

    emailLabel = Label(window, text='Email', fg='white', bg='#333333')
    emailLabel.config(font=('Calibri', 20))
    emailLabel.grid(row=2, column=0, pady=5, sticky='e')

    passwordLabel = Label(window, text='Password', fg='white', bg='#333333')
    passwordLabel.config(font=('Calibri', 20))
    passwordLabel.grid(row=3, column=0, pady=5, sticky='e')

    # Entries
    websiteEntry = Entry(window, width=35)
    websiteEntry.grid(row=1, column=1, columnspan=2, pady=5, padx=5, sticky='w')

    emailEntry = Entry(window, width=35)
    emailEntry.grid(row=2, column=1, columnspan=2, pady=5, padx=5, sticky='w')

    passwordEntry = Entry(window, width=21)
    passwordEntry.grid(row=3, column=1, pady=5, padx=5, sticky='w')

    # Generate Password Button
    generatePasswordButton = Button(window, text='Generate Password', command=generatePasswordButtonClicked)
    generatePasswordButton.grid(row=3, column=2, pady=5, padx=5, sticky='w')

    # Save Button
    saveButton = Button(window, text='Save', width=36, command=saveButtonClicked)
    saveButton.grid(row=4, column=1, columnspan=2, pady=10)

    # Run the Tkinter event loop
    window.mainloop()


if __name__ == "__main__":
    main()