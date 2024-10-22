# INSTRUCTIONS:
#   TODO 1:
#   Run this code and click on the circle a few times. Document what happens, or
#   doesn't happen. Stop the code and observe the error message. Document what 
#   you think this means.
#
#   TODO 2:
#   Run this code again and click on the square a few times. Document what 
#   happens in the python console. Stop the code. 

import turtle as trtl
import random as rand

score = 0 

# circular turtle will not use a global variable
spot = trtl.Turtle()
spot.goto(-100, 0)
spot.shape("circle")
spot.shapesize(3)

# square shaped turtle will use a global variable
box = trtl.Turtle()
box.goto(100,0)
box.shape("square")
box.shapesize(3)

new_xpos = rand.randint(-200,200)
new_ypos = rand.randint(-150,150)

def spot_clicked(x,y):
    change_position()



spot.onclick(spot_clicked)

def change_position():
 spot.goto(new_xpos, new_ypos)
  
# attempts to update the score for spot, but will not work because this function
# does not have access to the score that was created above
def update_score_for_spot(x,y):
  global score
  score +=1
  print(score)

# update_score_for_box will update the score for spot
def update_score_for_box(x,y):
  global score # gives this function access to the score that was created above
  score += 1
  print(score)
  

#---------events----------
spot.onclick(update_score_for_spot)
box.onclick(update_score_for_box)

spot_clicked(new_xpos , new_ypos)
change_position()


wn = trtl.Screen()
wn.mainloop()

