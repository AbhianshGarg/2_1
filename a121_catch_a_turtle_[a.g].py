# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
t = trtl.Turtle()
wn = trtl.Screen()
import random as rnd
import time

t.speed(0)

#-----game configuration----
spot_color = 'pink'
t.shape('circle')
wn.setup(400, 400)

score = 0
#-----initialize turtle-----



#-----game functions--------
def timer():
  start = time.time()



def move(x, y):
  t.penup()
  x_move = rnd.randint(-180, 180)
  y_move = rnd.randint(-180, 180)
  t.goto(x_move, y_move)
  t.stamp
  global score
  score += 1
  print('Score: ' + str(score))
    




#-----events----------------
cd = 0

while cd < 5:
  start = time.time()
  t.onclick(move)
  end = time.time()
  cd = end - start
  





wn.mainloop()