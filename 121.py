import turtle as trtl
import random as rand

score = 0

# Create circular turtle (spot)
spot = trtl.Turtle()
spot.goto(-100, 0)
spot.shape("circle")
spot.shapesize(3)

# Create square shaped turtle (box)
box = trtl.Turtle()
box.goto(100, 0)
box.shape("square")
box.shapesize(3)

font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

def spot_clicked(x, y):
    timer_up
    if timer_up == False:
       update_score_for_spot(x,y)
       change_position()
    else:
       spot.hideturtle()


def box_clicked(x, y):
    timer_up
    if timer_up == False:
       update_score_for_box(x,y)
       change_position2()
    else:
       box.hideturtle()

def change_position():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.goto(new_xpos, new_ypos)

def change_position2():
    new_xpos2 = rand.randint(-200, 200)
    new_ypos2 = rand.randint(-150, 150)
    box.goto(new_xpos2, new_ypos2)

#Game functions
def countdown():
  global timer, timer_up
  counter.clear()
  timer_up
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

# Score update functions
def update_score_for_spot(x, y):
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def update_score_for_box(x, y):
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

# Setup score display
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(100, 200)
score_writer.pendown()
score_writer.hideturtle()

#countdown timer
counter =  trtl.Turtle()
counter.penup()
counter.goto(-100,200)
counter.pendown()

# Event bindings
spot.onclick(spot_clicked)
box.onclick(box_clicked)



# Start the main event loop
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()


