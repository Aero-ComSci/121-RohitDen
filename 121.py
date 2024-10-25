import turtle as trtl
import random as rand

colors = ["yellow", "blue", "red", "green", "purple", "pink", "black", "white"]
sizes = [0.5, 1, 1.5, 2, 2.5, 3]  # Sizes as floats
score = 0
timer = 30
counter_interval = 1000  # 1000 represents 1 second
timer_up = False

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

# Setup score display
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(100, 200)
score_writer.pendown()
score_writer.hideturtle()

# Countdown timer
counter = trtl.Turtle()
counter.penup()
counter.goto(-100, 200)
counter.pendown()

def add_color(): 
    spot.color(rand.choice(colors))
    spot.stamp()
    spot.color("black")
    box.color(rand.choice(colors))
    box.stamp()
    box.color("black")

def spot_clicked(x, y):
    global timer_up
    if not timer_up:
        update_score_for_spot(x, y)
        change_position(spot)
        change_size(spot)
    else:
        spot.hideturtle()

def box_clicked(x, y):
    global timer_up
    if not timer_up:
        update_score_for_box(x, y)
        change_position(box)
        change_size(box)
    else:
        box.hideturtle()

def change_size(turtle):
    new_size = rand.choice(sizes)  # Select a random size
    turtle.shapesize(new_size)  # Change the size of the turtle

def change_position(turtle):
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    turtle.goto(new_xpos, new_ypos)

# Game functions
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=("Arial", 20, "normal"))
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=("Arial", 20, "normal"))
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval) 

# Score update functions
def update_score_for_spot(x, y):
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=("Arial", 20, "normal"))

def update_score_for_box(x, y):
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=("Arial", 20, "normal"))

def start_game():
    global timer, timer_up, score
    timer = 30  # Reset timer
    timer_up = False  # Reset timer status
    score = 0  # Reset score
    score_writer.clear()  # Clear previous score display
    add_color()  # Add initial colors
    spot.onclick(spot_clicked)  # Bind click events
    box.onclick(box_clicked)
    countdown()  # Start countdown timer
    trtl.Screen().bgcolor("sky blue")  # Set background color
    trtl.Screen().mainloop()  # Start the main event loop

# Start the game
start_game()

