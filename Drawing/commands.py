class Commands:
   def name(self):
        raise NotImplementedError("Subclasses should implement this method.")
   def execute(self, turtle):
        raise NotImplementedError("Subclasses should implement this method.")


class SquareCommand(Commands):
    def name(self):
        return "Draw Square"

    def execute(self, turtle):
        print(f"Move to ({turtle.x:.1f}, {turtle.y:.1f})")
        for _ in range(4):
            turtle.forward(20)
            turtle.turn_left(90)


class ZigzagCommand(Commands):
    def name(self):
        return "Draw Zigzag"

    def execute(self, turtle):
        print(f"Move to ({turtle.x:.1f}, {turtle.y:.1f})")
        steps = [20, 20, 20, 20]
        angles = [45, -90, 45, 0]
        for dist, ang in zip(steps, angles):
            turtle.forward(dist)
            if ang > 0:
                turtle.turn_left(ang)
            elif ang < 0:
                turtle.turn_right(-ang)