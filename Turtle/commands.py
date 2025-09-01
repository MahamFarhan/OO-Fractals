class Command:
    def execute(self, turtle):
        raise NotImplementedError("Command must implement execute()")

class MoveForward(Command):
    def __init__(self, distance=50):
        #validate that distance is a number 
        if not isinstance(distance, (float, int)):
            raise TypeError("distance must be a number")
        self.distance = distance

    def run(self, turtle):
        #executes the command that moves the turtle forward
        turtle.forward(self.distance)

class TurnLeft(Command):
    def __init__(self, heading=90):
        #validates that angle is a number 
        if not isinstance(heading, (float, int)):
            raise TypeError("angle must be a number")
        self.heading = heading

    def run(self, turtle):
        turtle.turn_left(self.heading)   # left turn = positive

class TurnRight(Command):
    def __init__(self, heading=90):
        if not isinstance(heading, (float, int)):
            raise TypeError("angle must be a number")
        self.heading = heading

    def run(self, turtle):
        turtle.turn_right(self.heading) 

# ---------- Command Parser ----------
def parse_command_string(command_str):
    #Takes a string like "F+F-F" and converts it into
    #a list of command objects like (ForwardCommand, TurnRightCommand, etc.)
    commands = []
    valid_chars = {"F", "+", "-"} #allowed and used symbols
    for ch in command_str.upper():
        if ch not in valid_chars:
            raise ValueError(f"Unknown command: '{ch}' — entire command ignored")
    #convert valid characters into command objects
    for ch in command_str.upper():
        if ch == "F":
            commands.append(MoveForward())
        elif ch == "+":
            commands.append(TurnRight())
        elif ch == "-":
            commands.append(TurnLeft())
    return commands

# ---------- Command Patterns ----------
class SquareCommand:
    def name(self):
        return "Draw Square"

    def execute(self, turtle):
        pattern = "F+F+F+F"
        for cmd in parse_command_string(pattern):
            cmd.run(turtle)


class ZigZagCommand:
    def name(self):
        return "Draw ZigZag"

    def execute(self, turtle):
        pattern = "F+F-F+F-F"
        for cmd in parse_command_string(pattern):
            cmd.run(turtle)

class UserCommand:
    def name(self):
        return "User Command"

    def execute(self, turtle):
        pattern = input("Enter drawing commands (e.g., F+F-F+F): ").strip()
        if not pattern:
            print("[Error] Empty command string!")
            return
        try:
            for cmd in parse_command_string(pattern):
                cmd.run(turtle)
        except ValueError as e:
            print(f"[Invalid] {e}")
    # if the user types something invalid the parser raises a ValueError, 
    # and your except ValueError prints a warning instead of crashing.