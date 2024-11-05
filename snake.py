from turtle import Turtle

# Constant variables is set here
# want range to go in  2, 1, 0 direction.
STARTING_POSITIONS = [
    (0, 0),
    (-20, 0),
    (-40, 0),
]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()  # automatically calls this function when object is created.
        self.head = self.segments[
            0
        ]  # b/c we call this so many times we create a variable for it

    def create_snake(self):
        """Create snake body using 3 square shapes"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def reset(self):
        for seg in self.segments:
            seg.goto(
                1000, 1000
            )  # move existing segment off of the screen b/c clear() method doesn't really remove what's on screen so this is a way to hide them off screen.

        self.segments.clear()  # clear all the segments from list
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(
        self, position
    ):  # position is needed in the for loop of create_snake method
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to the snake.
        self.add_segment(
            self.segments[-1].position()
        )  # start counting from end of list and calling the position method from the turtle class.

    # Get snake to automatically move forward
    def move(self):
        for seg_num in range(
            len(self.segments) - 1, 0, -1
        ):  # going backwards starting at index position of 2
            new_x = self.segments[seg_num - 1].xcor()  # this is 2nd to last segment
            new_y = self.segments[seg_num - 1].ycor()  # this is 2nd to last segment
            self.segments[seg_num].goto(
                new_x, new_y
            )  # move last segment to 2nd to first segment.

        # Finally move the first segment (head) forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # up = 90
        # when up, shouldn't let snake go down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # down = 270
        # when down, shouldn't let snake go up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # left = 180
        # when left, shouldn't let snake go right
        if (
            self.head.heading() != RIGHT
        ):  # Turtle has a heading method to use to check the direction
            self.head.setheading(LEFT)

    def right(self):
        # right = 0
        # when right, shouldn't let snake go left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
