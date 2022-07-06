from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game   oo====D~")
screen.tracer(0)
WALL_LIMIT = 290

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()

# Can control snake with either WSAD or arrow keys
screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 's')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'a')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'd')
screen.onkeypress(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if abs(snake.last_direction - snake.head.heading()) == 180:
        snake.head.setheading(snake.last_direction)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.score_point()
        food.teleport()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() < -WALL_LIMIT or snake.head.xcor() > WALL_LIMIT or \
            snake.head.ycor() < -WALL_LIMIT or snake.head.ycor() > WALL_LIMIT:
        scoreboard.reset_high_score()
        snake.reset_snake()
        # time.sleep(0.5)
        # screen.update()
        # time.sleep(0.5)

    # Detect collision with tail
    for snake_part in snake.snake_parts[1:]:
        if snake.head.distance(snake_part) < 10:
            scoreboard.reset_high_score()
            snake.reset_snake()
            # time.sleep(0.5)
            # screen.update()
            # time.sleep(0.5)

screen.exitonclick()
