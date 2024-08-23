from turtle import Screen
import time
from snake_object import Snake
from food import Food
from scoreboard import Score

# prepare the screen (size, color  title) and stop refreshing
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Snake game')

# create a snake object and food object
snake = Snake()
food = Food()
score = Score()

# update screen and start the game
screen.update()
game_is_on = True

# move snake up, down, left or right
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

# keep moving forward while game is on

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.add_point()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print('GAME OVER')
        score.game_over()
        game_is_on = False

    # detect collision with tail
    for segment in snake.sequences[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False



screen.exitonclick()