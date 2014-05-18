import turtle #drawing 
import random #for generating random hex colors


def gen_hex_color(): #generate a random hex color.
    color = ['#']
    for i in range(6):
        color.append(random.choice('0123456789ABCDEF'))
    return ''.join(color)

def get_user_input(): #get number of legs from user.
    while True:
        user_input = raw_input("Let's draw a sprite! How many legs? ")
        try:
            int(user_input)
        except ValueError:
            print "Please enter a whole number."
        else:
            return int(user_input)

def sprite_gen(): #draw sprite (using a single Turtle).
    
    #set up screen and pen (turtle).
    wn = turtle.Screen()
    wn.title ('Let\'s make a sprite!')
    #making the screensize smaller than the setup dimensions, gets rid of the scroll bar.
    wn.screensize(canvwidth=200, canvheight=200, bg=gen_hex_color())
    wn.setup(width=300, height=300)
    t = turtle.Turtle()
    t.speed(9)
    t.shape('classic')
    t.ht()
    t.shapesize(0.75, 0.75, 1)

    #ask user for number of sprite legs.
    n = get_user_input()

    #calculate angle between legs.
    angle = 360.0/n #reminder: angle must be floating point! use 360.0 for Python 2.

    
    #the drawing loop 
    for i in range(n + 1):
        t.color(gen_hex_color())
        #stamp the center last.
        if i == n:
            t.shape('circle')
            t.stamp()
            
        #draw legs and stamp the tips
        else:   
            t.forward(100)
            t.stamp()
            t.backward(100)
            t.left(angle)

    #user can click to exit window 
    wn.exitonclick()

#Let's do this!
sprite_gen()
