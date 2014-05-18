import turtle #drawing 
import random #for generating random hex colors
import time #for sleeping

# FUNCTION DEFINITIONS

#generate a random hex color.
def gen_hex_color():
    color = ['#']
    for i in range(6):
        color.append(random.choice('0123456789ABCDEF'))
    return ''.join(color)

#help gracefully exit the program.
def stretching(x=None, y=None):
    if x != None:
        global STRETCH
        STRETCH = False

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

#create leg shape
def create_leg_shape():
    WN.tracer(0) #do not draw screen.
    t = turtle.Turtle()
    t.ht()
    t.up()
    t.speed(0)
    t.left(90)
    t.fd(10)
    t.begin_poly()
    t.fd(100)
    t.right(90)
    t.circle(7)
    t.end_poly()
    p = t.get_poly()
    turtle.register_shape('leg', p)

#draw sprite (using multiple Turtles).
def sprite_gen():

    #get number of sprite legs from user.
    n = get_user_input()

    #calculate angle between legs.
    leg_angle = 360.0/n #reminder: must be floating point! use 360.0 for Python 2.
    
    #draw centerpoint
    WN.tracer(0) #do not draw screen.
    middle = turtle.Turtle()
    middle.ht() 
    middle.color(gen_hex_color())
    middle.shape('circle')
    middle.shapesize(0.75, 0.75, 1)
    WN.tracer(1) #reset tracer to draw (every) screen.
    middle.stamp()

    #create leg shape.
    create_leg_shape()

    #select a random start heading.
    start_angle = random.randint(0, 359)

    #draw the first leg.
    WN.tracer(0) #do not draw screen.
    leg0 = turtle.Turtle()
    leg0.color(gen_hex_color())
    leg0.shape('leg')
    leg0.resizemode('user')
    leg0.setheading(start_angle)
    WN.tracer(1) #reset tracer to draw (every) screen.
    leg0.st()
    leg0.left(leg_angle)

    #draw the rest of the legs counterclockwise.
    legs = [leg0]
    for i in range(n - 1):
        WN.tracer(0) #do not draw screen.
        t = legs[i].clone()
        t.color(gen_hex_color())
        WN.tracer(1) #reset tracer to draw (every) screen.
        t.speed(2)
        t.left(leg_angle)
        legs.append(t)

    WN.update() #make sure everything was drawn to the screen.
    time.sleep(1) #pause

    #turn legs counterclockwise.
    print "Click to stop."
    while STRETCH:
        WN.onclick(stretching)
        WN.tracer(0) #do not draw screen.
        random.shuffle(legs)
        i = 0
        for t in legs:
            stretch_factor = random.random() 
            t.shapesize(stretch_len=stretch_factor)
            middle.stamp()
            WN.update()
            time.sleep(0.02)
        WN.update() #draw screen.
    print "Click to exit."
    WN.exitonclick()

#GLOBAL VARIABLES

#set up screen and pen (turtle).
WN = turtle.Screen()
WN.title ('Let\'s make a sprite!')
#Gets rid of scroll bar by making the screensize smaller than the setup dimensions.
WN.screensize(canvwidth=200, canvheight=200, bg=gen_hex_color())
WN.setup(width=300, height=300)

STRETCH = True

#Let's do this!
sprite_gen()


