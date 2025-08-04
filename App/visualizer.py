from Drawing.canvas import Canvas
def run_visualizer():
    canvas = Canvas()
    canvas.draw_circle(x=100, y=100, radius=50, color="blue", fill="lightblue")
    canvas.draw_rectangle(x1=200, y1=200, x2=300, y2=300, outline="green", fill="lightgreen")
    canvas.draw_polygon(points=[(400, 400), (450, 350), (500, 400)], outline="red", fill="pink")
    canvas.start()
