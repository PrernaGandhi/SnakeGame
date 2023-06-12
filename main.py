from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakezzzzzzzzzyyy")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # can only be used if tracer is off(animation is off)
    screen.update()
    time.sleep(0.1)
    snake.move()

# TODO 3: control the snake
# TODO 4: detect collision with food
# TODO 5: create score board
# TODO 6: detect collision with wall
# TODO 7: detect collision with tail


screen.exitonclick()
