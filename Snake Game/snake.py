from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.second = self.segments[1]
        self.head_mod()

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.second = self.segments[1]
        self.head_mod()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("orange")
        new_segment.shapesize(0.5, 0.5)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def head_mod(self):
        self.head.color("cyan")
        self.head.shape("circle")
        self.head.shapesize(0.6, 0.8)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if abs(self.head.xcor() - self.second.xcor()) > 15:
            self.head.setheading(UP)

    def down(self):
        if abs(self.head.xcor() - self.second.xcor()) > 15:
            self.head.setheading(DOWN)

    def left(self):
        if abs(self.head.ycor() - self.second.ycor()) > 15:
            self.head.setheading(LEFT)

    def right(self):
        if abs(self.head.ycor() - self.second.ycor()) > 15:
            self.head.setheading(RIGHT)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
