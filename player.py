from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.go_to_start()
        self.setheading(90)

    def move_north(self):
        self.setheading(NORTH)
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_south(self):
        self.setheading(SOUTH)
        self.forward(MOVE_DISTANCE)

    def move_west(self):
        self.setheading(WEST)
        self.forward(MOVE_DISTANCE)

    def move_east(self):
        self.setheading(EAST)
        self.forward(MOVE_DISTANCE)
