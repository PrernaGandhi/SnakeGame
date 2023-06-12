from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    # TODO 1: create the snake
    def create_snake(self):
        for i in range(3):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(STARTING_POSITIONS[i])
            self.snake_segments.append(snake)

    # TODO 2: move the snake
    def move(self):
        for seg_no in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_no - 1].xcor()
            new_y = self.snake_segments[seg_no - 1].ycor()
            self.snake_segments[seg_no].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)