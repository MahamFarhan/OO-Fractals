from .commands import Commands, ForwardCommand, TurnLeftCommand, TurnRightCommand
class Turtle:
    def __init__(self, pen, canvas):
        self.pen = pen
        self.canvas = canvas
        self.command_map = {
            "F": ForwardCommand(),
            "+": TurnRightCommand(),
            "-": TurnLeftCommand()
        }

    def run(self, instructions: str):
        for char in instructions:
            cmd = self.command_map.get(char)
            if cmd:
                cmd.execute(self.pen, self.canvas)