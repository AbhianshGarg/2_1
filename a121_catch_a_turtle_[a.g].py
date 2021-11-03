# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
t = trtl.Turtle()
timekeeper = trtl.Turtle()
s = trtl.Turtle()
wn = trtl.Screen()
import random as rnd
import time

t.speed(0)

#-----game configuration----
spot_color = 'pink'
t.shape('circle')
wn.setup(400, 400)

timekeeper.penup()
timekeeper.hideturtle()
timekeeper.goto(-170, 150)

s.penup()
s.hideturtle()
s.goto(50, -150)

score = 0

font_setup = ("Arial", 20, "normal")
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False
play = True



#-----Lists--------

colors = ['green', 'blue', 'orange', 'red', 'yellow']

#-----game functions--------
def start_game():
  print("""
  Welcome to this game. Try to click the moving circle as many times as possible!

  Game starts in 3 seconds!
  """)
  
  for i in range(3, 0, -1):
    timekeeper.clear()
    timekeeper.write(i, font=font_setup)
    time.sleep(1)

  time.sleep(3)

def move(x, y):
  if play == True:
    t.penup()
    x_move = rnd.randint(-180, 180)
    y_move = rnd.randint(-180, 180)
    t.goto(x_move, y_move)
    t.stamp
    s.clear()
    global score
    score += 1
    w_score = 'Score: ' + str(score)
    s.write(w_score, font=font_setup)
    randomize()


def randomize():
  size = rnd.randint(1, 3)
  t.turtlesize(size)
  wn.bgcolor(rnd.choice(colors))
    
def countdown():
  global timer, timer_up
  global play
  timekeeper.clear()
  if timer <= 0:
    timekeeper.write("Time's Up", font=font_setup)
    global timer_up
    timer_up = True
    play = False
  else:
    timekeeper.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    timekeeper.getscreen().ontimer(countdown, counter_interval)



#-----events----------------
start_game()

wn.ontimer(countdown, counter_interval) 
while play == True:
  t.onclick(move)

  

wn.mainloop()
