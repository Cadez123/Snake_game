from turtle import Turtle, Screen

STARTING_LOCATIONS = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.sequences = []
        self.create_snake()
        self.head = self.sequences[0]

    # function that creates the snake in starting position
    def create_snake(self):
        for position in STARTING_LOCATIONS:
            self.add_segment(position)

    # function that moves snake forward
    def move_forward(self):
        for seq in range(len(self.sequences) - 1, 0, -1):
            new_x = self.sequences[seq - 1].xcor()
            new_y = self.sequences[seq - 1].ycor()
            self.sequences[seq].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        sequence = Turtle()
        sequence.penup()
        sequence.shape('square')
        sequence.color('white')
        sequence.goto(position)
        self.sequences.append(sequence)

    def extend_snake(self):
        # add new segment to snake
        self.add_segment(self.sequences[-1].position())

    # function that moves snake up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # function that moves snake down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # function that moves snake left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # function that moves snake right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)