from Drawing.canvas import Canvas
def run_visualizer():
    canvas = Canvas()
    #Canvas() → creates a Canvas object from your Drawing.canvas file. This is your GUI window + Tkinter drawing area.
    canvas.draw_circle(x=100, y=100, radius=50, color="blue", fill="lightblue")
    #draw_circle(...) → calls the method inside your Canvas class that uses tkinter.create_oval to draw a circle.
    canvas.draw_rectangle(x1=200, y1=200, x2=300, y2=300, outline="green", fill="lightgreen")
    canvas.draw_polygon(points=[(400, 400), (450, 350), (500, 400)], outline="red", fill="pink")
    canvas.start()
    #canvas.start() → launches the Tkinter event loop so the window stays open
