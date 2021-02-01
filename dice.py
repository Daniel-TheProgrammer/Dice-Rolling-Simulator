import random
from tkinter import Tk, Label, Button

class DiceRolla:
    def __init__(self, master):
        self.master = master
        master.title("Dice Rolla")

        self.label = Label(master, text="")
        self.label.pack()

        self.rollDice_button = Button(master, text="Roll", command=self.roll)
        self.rollDice_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def roll(self):
        self.value = random.randint(1, 6)
        self.label.configure(text=str(self.value))

root = Tk()
app = DiceRolla(root)
root.mainloop()
