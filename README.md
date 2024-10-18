# Snake Game

This project is a simple **Snake Game** implemented in Python using the `turtle` graphics library. The game allows you to control the snake's movement and challenges you to eat food, grow in size, and avoid collisions with the walls or the snake's own tail. The score increases each time the snake eats food.

## Features

- **Snake Movement**: The snake moves around the screen based on user input.
- **Food Generation**: Random food appears on the screen, which the snake can "eat" to grow longer.
- **Scoreboard**: Displays the current score, which increments as the snake eats food.
- **Collision Detection**: The game ends if the snake collides with the wall or with its own tail.
  
## Prerequisites

Before running the game, make sure you have Python installed along with the `turtle` module (which is included with Python by default).

## How to Run

1. Clone the repository or download the code files.
2. Make sure you have the following Python files in the same directory:
    - `snake.py`: Contains the `Snake` class, which defines the snake's behavior.
    - `food.py`: Contains the `Food` class, which defines the food object.
    - `scoreboard.py`: Contains the `Scoreboard` class, which tracks the score.
3. Run the main game file:

    ```bash
    python snake_game.py
    ```

## Gameplay Instructions

- **Move the Snake**: Use the arrow keys (`Up`, `Down`, `Left`, `Right`) to control the snake's movement.
- **Objective**: Eat the food to grow longer and increase your score.
- **Game Over**: The game ends if the snake hits the walls or its own tail.

## Code Overview

- **`Snake` Class**:
  - Creates and manages the snake's body and movement.
  - Handles turning, growing, and collision detection.
  
- **`Food` Class**:
  - Manages the food object that appears randomly on the screen.
  - Food is consumed when the snake's head touches it.
  
- **`Scoreboard` Class**:
  - Displays the current score on the screen.
  - Shows a "Game Over" message when the game ends.

## Code Structure

```python
# Set up the game window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Control the screen updates

# Initialize game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # Control snake speed
    
    # Move the snake and listen for user input
    snake.move()
    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    # Check for collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Check for collision with wall or tail
    if snake.detect_collision():
        game_is_on = False
        scoreboard.game_over()

# Close the game window on click
screen.exitonclick()
