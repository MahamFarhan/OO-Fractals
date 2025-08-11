from Drawing.turtle import Turtle
from Drawing.commands import SquareCommand, ZigzagCommand
from Geometry.point import Point
from Drawing.canvas import Canvas
class App:
    def __init__(self, root,canvas, start_position=(100, 100)):
         self.canvas = canvas
         self.turtle = Turtle(Point(*start_position), 0)
         self.turtle.set_canvas(self.canvas)
         self.commands = [SquareCommand(), ZigzagCommand()]
         self.root = root

    def run(self):
        print("Available drawing commands:")
        for i, cmd in enumerate(self.commands):
            print(f"{i + 1}. {cmd.name()}")

        while True:
            try:
                choice = int(input("Choose a command (1 or 2): "))
                if 1 <= choice <= len(self.commands):
                    self.commands[choice - 1].execute(self.turtle)
                    break
                else:
                    print("Invalid choice, try again.")
            except ValueError:
                print("Please enter a number.")