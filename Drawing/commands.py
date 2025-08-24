class Command:
    def execute(self):
        raise NotImplementedError("Command must implement execute()")


class MoveForward(Command):
    def __init__(self, pen):
        self.pen = pen

    def execute(self):
        self.pen.move_forward()


class TurnLeft(Command):
    def __init__(self, pen):
        self.pen = pen

    def execute(self):
        self.pen.turn_left()


class TurnRight(Command):
    def __init__(self, pen):
        self.pen = pen

    def execute(self):
        self.pen.turn_right()