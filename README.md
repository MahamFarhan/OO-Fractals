# OO Fractals

This is a beginner-friendly Python project focused on learning and applying object-oriented programming (OOP) concepts through geometry and fractal drawing. The project includes reusable classes for shapes like circles, rectangles, and polygons, with visual rendering using Tkinter. It also includes custom turtle commands.

## Structure and Combination
- Geometry classes (Point, Line)
- Drawing classes (Pen, Canvas)
- Shapes classes (Shapes(Parent class), Circle, Polygon, Rectangle)
- Turtle engine (Turtle)
- Command Pattern (MoveForward, TurnLeft, TurnRight, SquareCommand, ZigzagCommand, UserCommand)
- Application Manager (App(Turtle),Visualizer(Shapes))

## Features
- Move a turtle with commands: Forwaed, Left, Right (F, +, -).
- Predefined patterns: Square and ZigZag.
- User-defined patterns entered in the terminal.
- Draw shapes (Circle, Rectangle, Polygon) with object-oriented structure.
- Canvas supports clearing, redrawing, and storing drawn lines.
- Validation checks for wrong inputs (non-numeric coordinates, invalid commands).
