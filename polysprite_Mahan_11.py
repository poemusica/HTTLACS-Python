import turtle #for drawing 
import random #for generating random hex colors
import time #for sleeping

#=======================================================
#generate a random hex color.
def gen_hex_color():
    color = ['#']
    for i in range(6):
        color.append(random.choice('0123456789ABCDEF'))
    return ''.join(color)

#stop the turning animation.
def stop(x=None, y=None):
    global TURN
    TURN = False

#run turning animation.
def animate(shapes):

    #stop the animation.
    print "Click to stop."
    WN.onclick(stop)

    #turn legs counterclockwise.
    while TURN:
        WN.tracer(0) #do not draw screen.
        for t in shapes:
            t.lt(2)
        WN.update() #draw screen.

#draw legs.
def draw_legs(n):
    #select a random start heading.
    start_angle = random.randint(0, 359)

    #calculate angle between legs.
    leg_angle = 360.0/n #reminder: must be floating point! use 360.0 for Python 2.

    #draw the first leg.
    WN.tracer(0) #do not draw screen.
    leg0 = turtle.Turtle()
    c = gen_hex_color()
    leg0.pen(pencolor=c, fillcolor=c, shown=True)
    leg0.shape('leg')
    leg0.seth(start_angle)
    WN.tracer(1) #reset tracer to draw (every) screen.
    leg0.lt(leg_angle)

    #draw the rest of the legs counterclockwise.
    legs = [leg0]
    for i in range(n - 1):
        WN.tracer(0) #do not draw screen.
        t = legs[i].clone()
        t.color(gen_hex_color())
        WN.tracer(1) #reset tracer to draw (every) screen.
        t.speed(2)
        t.lt(leg_angle)
        legs.append(t)
    return legs

#create leg shape.
def create_leg_shape():
    WN.tracer(0) #do not draw screen.
    t = turtle.Turtle()
    t.pen(speed=0, shown=False, pendown=False)
    t.lt(90)
    t.fd(10)
    t.begin_poly()
    t.fd(100)
    t.circle(7)
    t.end_poly()
    p = t.get_poly()
    turtle.register_shape('leg', p)

#draw center.
def draw_center():
    WN.tracer(0) #do not draw screen.
    middle = turtle.Turtle()
    c = gen_hex_color()
    middle.pen(shown=False, pencolor=c, fillcolor=c, resizemode='user', stretchfactor=(0.75, 0.75), outline=1)
    middle.shape('circle')
    WN.tracer(1) #reset tracer to draw (every) screen.
    middle.stamp()


#ask user for number of sprite legs.
def get_user_input():
    while True:
        user_input = raw_input("Let's draw a sprite! How many legs? ")
        try:
            int(user_input)
        except ValueError:
            print "Please enter a whole number."
        else:
            return int(user_input)


#draw sprite (using multiple Turtles).
def main():

    #get number of sprite legs from user.
    n = get_user_input()
    
    #draw centerpoint
    draw_center()

    #create leg shape.
    create_leg_shape()

    #draw legs
    legs = draw_legs(n)

    WN.update() #make sure everything was drawn to the screen.
    time.sleep(1) #pause

    #turn legs counterclockwise
    animate(legs)

    turtle.mainloop()

#=======================================================
#GLOBAL VARIABLES

#set up screen and pen (turtle).
WN = turtle.Screen()
WN.title ('Let\'s make a sprite!')
#gets rid of scroll bar by making the screensize smaller than the setup dimensions.
WN.screensize(canvwidth=200, canvheight=200, bg=gen_hex_color())
WN.setup(width=300, height=300)

TURN = True

#=======================================================

#let's do this!
main()


