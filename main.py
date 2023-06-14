import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

GAME_TITLE = "Snakezzzzzzzzzyyy"


def setup_screen():
    game_screen.setup(width=600, height=600)
    game_screen.bgcolor("black")
    game_screen.title(GAME_TITLE)
    game_screen.tracer(0)
    game_screen.listen()


def set_keyboard_controls(snake):
    game_screen.onkey(snake.up, "Up")
    game_screen.onkey(snake.down, "Down")
    game_screen.onkey(snake.left, "Left")
    game_screen.onkey(snake.right, "Right")


def play_game(screen, player_name):
    # screen = Screen()
    setup_screen()
    snake = Snake()
    set_keyboard_controls(snake)
    food = Food()
    scoreboard = ScoreBoard(player_name)
    game_is_on = True
    while game_is_on:
        # can only be used if tracer is off(animation is off)
        screen.update()
        time.sleep(0.1)
        # TODO 3: control the snake
        snake.move()
        # TODO 4: detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            # TODO 5: create score board
            scoreboard.update_score()
        # TODO 6: detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()
        # TODO 7: detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()


game_screen = Screen()
setup_screen()
player_name = game_screen.textinput(GAME_TITLE, "Enter the player's first name: ").split(" ")[0]

restart_game = True
while restart_game:
    play_game(game_screen, player_name)
    user_input = game_screen.textinput("Wanna play again ??", "Do you want to restart the game ? Type 'y' or 'n : ")
    if user_input == 'y':
        game_screen.clearscreen()
    else:
        restart_game = False

game_screen.exitonclick()
