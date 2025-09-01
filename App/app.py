from Drawing.pen import Pen
from Turtle.turtle import Turtle
from Turtle.commands import SquareCommand, ZigZagCommand, UserCommand
from Drawing.canvas import Canvas
import tkinter as tk
class App:
     """
    Main application:
    - Creates Tkinter window + canvas
    - Initializes a Turtle with a Pen
    - Loads predefined commands (square, zigzag, user)
    - Shows menu for user to select a command
    """
     def __init__(self):
        self.root = tk.Tk()
        self.root.title("Turtle Drawing App")

        # Create a drawing panel 
        tk_canvas = tk.Canvas(self.root, width=500, height=500, bg="white")
        tk_canvas.pack()
        self.canvas = Canvas(tk_canvas)

        canvas = Canvas(tk_canvas)
        self.root.bind("c", lambda event: canvas.clear())

        # Pen + Turtle Setup
        pen = Pen(self.canvas)
        self.turtle = Turtle(pen, position=(200, 150), heading=0)

        #  Available Commands in a list
        self.commands = [SquareCommand(), ZigZagCommand(), UserCommand()]

        
     def run_commands(self):
        #shows command menu in terminal from which the user can choose from
        print("Choose from available drawing commands:")
        for i, cmd in enumerate(self.commands):
            print(f"{i+1}. {cmd.name()}")

        try:
            choice = int(input(f"Choose a command (1 to {len(self.commands)}): "))
            if 1 <= choice <= len(self.commands):
                self.commands[choice-1].execute(self.turtle)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

        # keep GUI open
        self.root.mainloop()
    