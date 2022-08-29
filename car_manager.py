from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        """Creates empty list to store turtles as cars"""
        super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def spawn_cars(self):
        """Generates turtles in form of cars randomly"""
        random_number = random.randint(0, 4)
        if random_number == 3:
            random_y = random.randint(-200, 200)
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=0.8, stretch_len=2, outline=None)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(310, random_y)
            self.cars.append(new_car)

    def move_car(self):
        """Moves cars"""
        for car in self.cars:
            car.forward(self.speed)

    def increment_speed(self):
        """Increments cars speed"""
        self.speed += MOVE_INCREMENT
        for car in self.cars:
            car.forward(self.speed)

    def reset_cars_speed(self):
        """Resets cars speed"""
        self.speed = STARTING_MOVE_DISTANCE



