from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0, 3):
            self.add_segment(STARTING_POSITIONS[i])

    def add_segment(self, position):
        new_seg = Turtle(shape='square')
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def self_collision(self):
        for segment in self.segments[3:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def is_within_screen(self):
        return 283 >= self.head.xcor() >= -283 and 283 >= self.head.ycor() >= -283

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            next_pos = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(next_pos)
        self.head.forward(MOVE_DISTANCE)

    def moving_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def moving_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def moving_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def moving_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for segment in self.segments:
            segment.reset()
        self.__init__()
        # self.segments.clear()
        # self.create_snake()
        # self.head = self.segments[0]
