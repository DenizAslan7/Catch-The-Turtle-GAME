import time
import turtle
from random import randint as randint

# making game screen
game_screen = turtle.Screen()
game_screen.bgcolor("light blue")
game_screen.title("Catch The Turtle!!")

# making turtle
player = turtle.Turtle()
player.shapesize(4)
player.shape("turtle")
player.speed(9)
player.color("green")
player.penup()
player.hideturtle()

#score and timer
score = 0
timer =30

# score title
scor_title = turtle.Turtle()
scor_title.speed(0)
scor_title.color("black")
scor_title.penup()
scor_title.hideturtle()
scor_title.goto(0,300)
scor_title.write("Score : {}".format(score), align ="center" , font=("Courier",24,"normal"))

#time title
time_title = turtle.Turtle()
time_title.speed(0)
time_title.color("black")
time_title.penup()
time_title.hideturtle()
time_title.goto(0,260)
time_title.write("Time : {}".format(timer), align="center", font=("Courier",22,"normal"))

#color list
turtle_colors = ["green","blue","yellow","red","orange","brown","purple","pink","grey","white"]
color_counter = score

# click  function
def click_counter(x, y):
    global score
    score += 1
    scor_title.clear()
    scor_title.write("Score : {}".format(score), align="center", font=("Courier",24,"normal"))

# timer function
def countdown():
    global timer
    timer -= 1
    time_title.clear()
    time_title.write("Time : {}".format(timer),align="center",font=("Courier",22,"normal"))
    time.sleep(0.5)

# turtle color change function
def change_color():
    global color_counter
    if color_counter != score:
        player.color(turtle_colors[randint(0,10)])
        color_counter = score
    else:
        pass

# game start
while timer != 0:
    change_color()
    countdown()
    player.hideturtle()
    player.goto(randint(-400,400),randint(-400,400))
    player.showturtle()
    time.sleep(0.5)
    player.onclick(click_counter)

# end screen
scor_title.clear()
time_title.clear()
player.hideturtle()
end_title = turtle.Turtle()
end_title.speed(0)
end_title.color("Green")
end_title.penup()
end_title.hideturtle()
end_title.goto(0,0)
end_title.write("""GAME OVER!
Your Score : {}
""".format(score),align="center",font=("Courier",30,"normal"))


turtle.mainloop()

