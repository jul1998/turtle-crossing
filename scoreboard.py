from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """Creates score board"""
        super().__init__()
        self.penup()
        with open(r"./Highest_level/highest_level.txt") as level: # Directory for txt file where
            # highest level is located
            self.highest_level = int(level.read())
        self.score = 0
        self.goto(-200, 250)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """Updates score when called"""
        self.clear()
        self.write(f"Level: {self.score} Highest level: {self.highest_level}", align="left", font=FONT)

    def level_up(self):
        """It increments level and overwrites the highest level if new one is achieved"""
        self.score += 1
        self.update_score()
        if self.score> self.highest_level:
            self.highest_level = self.score
            with open(r"./Highest_level/highest_level.txt", "w") as level:
                level.write(f"{self.highest_level}")


    def reset_level(self):
        """Resets level when player loses"""
        self.score = 0
        self.update_score()
