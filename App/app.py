from Drawing.pen import Pen

class App:
    def __init__(self, root, canvas, start_position=(0, 0)):
        self.root = root
        self.canvas = canvas
        self.start_position = start_position
        self.pen = Pen(canvas, position=start_position)

    def run(self, commands: str):
        """Execute a sequence of drawing commands."""
        print(f"Executing commands: {commands}")
        for cmd in commands:
            if cmd == "F":        # Move forward
                self.pen.forward(50)
            elif cmd == "+":      # Turn left
                self.pen.turn_left(90)
            elif cmd == "-":      # Turn right
                self.pen.turn_right(90)
            elif cmd == "B":      # Move backward
                self.pen.forward(-50)
            else:
                print(f"Unknown command: {cmd}")