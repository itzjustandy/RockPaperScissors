# Rock, Paper, Scissors GAME by Andy Nguyen

# Import Statements
from tkinter import *
from random import *
root = Tk()

# Variable Names

Computer = 0
Rock = 0
Paper = 0
Scissors = 0
User = 0
Win = 0
Lose = 0
Draw = 0

# Introductions

messagebox.showinfo("Rock, Paper, Scissors", "Welcome to the Rock, Paper, Scissors")
messagebox.showinfo("Rock, Paper, Scissors", "The Rules are Simple: " +
                    "\nRock beats Scissors, Scissors beats Paper, Paper beats Rock " +
                    "\nand having the same pick is a draw.")

# THE GAME BEGINS

# The ENGINE

while True:
    Computer = randint(1,3)
    if Computer == 1:
        Computer = "Rock"
    elif Computer == 2:
        Computer = "Paper"
    else:
        Computer == "Scissors"
    while True:
        User = simpledialog.askstring("Rock, Paper, Scissors", "So.. Rock, Paper, or Scissors?")
        if (User == "Rock") or (User == "Paper") or (User == "Scissors"):
            break

# Hell Begins

    if (Computer == "Rock" and User == "Scissors") or (Computer == "Paper" and User == "Rock") or (Computer == "Scissors" and User == "Paper"):
        Lose += 1
        messagebox.showinfo("
        
                                                       
    
while True:
    if messagebox.askyesno("Hi", "do you suck?"):
        break
