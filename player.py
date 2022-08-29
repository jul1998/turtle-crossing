from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    """Creates turtle to be used by player"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")

    def move_up(self):
        """Allows turtle to move upwards only"""
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Resets player position"""
        self.goto(STARTING_POSITION)



