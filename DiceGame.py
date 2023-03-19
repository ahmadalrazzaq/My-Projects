from tkinter import *
from tkinter.messagebox import showinfo
from random import *

class Craps(Tk):
    'a GUI that makes dice game'

   
    def __init__(self, parent=None):
        'constructor'
        Tk.__init__(self, parent)
        self.title("Play ")
        self.new_game()
        self.make_widgets()

    def new_game(self):
        'reset the game'
        self.firstroll = 0

    
    def make_widgets(self):
        'define the widgets'
        Label(self, text="Die 1").grid(row=0, column=0)
        Label(self, text="Die 2").grid(row = 0, column = 1)
        self.ent1 = Entry(self, justify = CENTER)
        self.ent1.grid(row = 1, column = 0)
        self.ent2 = Entry(self, justify = CENTER)
        self.ent2.grid(row = 1, column = 1)
        Label(self, text = "First roll").grid(row = 2, column = 0)
        self.first = Entry(self, justify = CENTER)
        self.first.grid(row = 3, column = 0)
        Label(self, text = "Result").grid(row = 2, column = 1)
        self.result = Entry(self, justify = CENTER)
        self.result.grid(row = 3, column = 1)
        Button(self, text="Roll the dice!", command = self.play).grid(row = 4, column = 0, columnspan = 2)

    def play(self):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        self.ent1.delete(0, END)
        self.ent2.delete(0, END)
        self.result.delete(0, END)
        self.ent1.insert(END, die1)
        self.ent2.insert(END, die2)
        total = die1 + die2
        if self.firstroll ==0:
            self.firstroll = total
            self.first.delete(0, END)
            self.first.insert(END, total)
            if self.firstroll in (7, 11):
                self.result.insert(END, 'You won! Roll dice to play again')
                self.new_game()
            elif self.firstroll in (2, 3, 12):
                self.result.insert(END, 'You have lost :( Roll dice to play again')
                self.new_game()
        else:
            if total == 7:
                self.result.insert(END, 'You lost. Play again?')
                self.new_game()
            elif total == self.firstroll:
                self.result.insert(END, 'You won! Play again?')
                self.new_game()
            else:
                self.result.insert(END, 'Keep trying! Roll again.')
        
        

Craps().mainloop()
