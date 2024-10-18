# Create a snake game using Python
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # nothing happens until we call "update()" method

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Step 1: Create a snake body of 3 squares
# snake.create_snake()
screen.update()  # want to see update on screen at this point, not piece by piece but in its entirety

# Step 2: Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # 1 sec delay after each move
    # start at last segment and stop at beginning segment, move by -1 step
    # call function to move snake
    snake.move()
    # Step 3: Control the snake
    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    # Step 4: Create snake food in food.py
    # Step 5: Detect if collision with food
    if snake.head.distance(food) < 15:  # food is 10x10
        food.refresh()
        snake.extend()
        # Step 6: Create a scoreboard
        scoreboard.increase_score()

    # Step 7: Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()

    # Step 8: Detect collision with tail
    # if head touches any tail then game over
    # original code is too long, try using slicing instead
    """for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:"""
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:  # not including the head
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
