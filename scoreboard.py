from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        # read text mode 'r'
        # with keyword, python will help manage and close the file after opening
        # Try reading the high score from the file, default to 0 if the file is empty or non-existent
        try:
            with open(
                "/Users/mei/projects/python_practice_snake_game/data.txt", mode="r"
            ) as data:
                content = data.read().strip()
                print(f"Content of data.txt: '{content}'")  # Debug line
                self.high_score = int(content) if content else 0
                print(self.high_score)  # test purpose
        except FileNotFoundError:
            # If file doesn't exist, set high_score to 0
            self.high_score = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # avoid text from overlapping
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            # Write the new high score to the file text mode of 'w'
            with open(
                "/Users/mei/projects/python_practice_snake_game/data.txt", mode="w"
            ) as data:
                data.write(f"{self.high_score}")
                print(f"{self.high_score}")  # test purpose

        self.score = 0  # reset the score back to 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # save high scores into a file
