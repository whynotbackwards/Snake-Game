from turtle import Turtle

# POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.make_snake()
        self.head = self.snake_parts[0]
        self.last_direction = self.head.heading()

    def make_snake(self):
        for n in range(3):
            self.add_part((-20 * n, 0))

    def add_part(self, position):
        snake_part = Turtle('square')
        snake_part.color('white')
        snake_part.penup()
        snake_part.goto(position)
        self.snake_parts.append(snake_part)

    def extend(self):
        self.add_part(self.snake_parts[-1].position())

    def reset_snake(self):
        for part in self.snake_parts:
            part.hideturtle()
        self.snake_parts.clear()
        self.make_snake()
        self.head = self.snake_parts[0]

    def move(self):
        for part_num in range(len(self.snake_parts)-1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.last_direction = self.head.heading()

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
