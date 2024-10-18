from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Collision(Turtle):
    def __init__(self):
        super().__init__()
        self.write(f"Game Over.", align=ALIGNMENT, font=FONT)
