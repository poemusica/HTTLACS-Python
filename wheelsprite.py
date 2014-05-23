import turtle #drawing 
import random #for generating random hex colors
import time #for sleeping

#=======================================================

#generate a random hex color.
def gen_hex_color():
    color = ['#']
    for i in range(6):
        color.append(random.choice('0123456789ABCDEF'))
    return ''.join(color)

#stop the animation.
def stop(x=None, y=None):
    global MOVE
    MOVE = False

#run turning animation.
def animate(middle):
    #prepare for movement
    all_turtles = WN.turtles()
    all_turtles.remove(middle) #get all legs
    sorted_turtles = sorted(all_turtles, key=lambda t: t.heading()) #sort leg turtles by heading
    sorted_colors = [t.color() for t in sorted_turtles] #get sorted leg turtle colors.
    print "Click to stop."
    WN.onclick(stop)

    #counterclockwise movement loop
    while MOVE:
        WN.tracer(0) #do not draw on screen.
        #shift leg turtle colors one to the right.
        last_color = sorted_colors.pop()
        sorted_colors.insert(0, last_color)

        #redraw each leg using the color of the turtle to its right.
        for pair in zip(sorted_turtles, sorted_colors):
            t = pair[0]
            c = pair[1][0]
            if t != middle:
                t.undo()
                t.undo()
                t.color(c)
                t.forward(90)
                t.stamp()
        WN.update() #draw screen.
        time.sleep(0.2) #pause


#draw center.
def draw_center():
    WN.tracer(0) #do not draw screen.
    middle = turtle.Turtle()
    c = gen_hex_color()
    middle.pen(shown=False, pencolor=c, fillcolor=c, resizemode='user', stretchfactor=(0.75, 0.75), outline=1)
    middle.shape('circle')
    WN.tracer(1) #reset tracer to draw (every) screen.
    middle.stamp()
    return middle

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


#draw legs.
def draw_legs(n):
    #calculate angle between legs.
    angle = 360.0/n #reminder: angle must be floating point! use 360.0 for Python 2.
    
    #create a list of multipliers (0 through n) and shuffle.
    n_list = [x for x in range(n)]

    #create a list of angles and shuffle it.
    angles = [x * angle for x in n_list]
    random.shuffle(angles)

    #select a random start heading.
    start_angle = random.randint(1, 360)

    #the drawing loop 
    for i in range(n):
        WN.tracer(0) #do not draw on screen.
        t = turtle.Turtle()
        c = gen_hex_color()
        t.pen(pencolor=c, fillcolor=c, shown=False, resizemode='user', stretchfactor=(0.75, 0.75), outline=1, pendown=False, speed=7)
        t.shape('classic')

        rand_angle = angles[i]
        t.lt(start_angle + rand_angle)
        t.fd(10)
        t.down()
        WN.tracer(1) #reset tracer to draw every screen.
        t.fd(90)
        t.stamp()

#draw sprite (using multiple Turtles).
def main():
    
    #get number of sprite legs from user.
    n = get_user_input()

    #draw centerpoint
    middle = draw_center()

    draw_legs(n)

    WN.update() #make sure everything was drawn to the screen.
    time.sleep(1) #pause

    animate(middle)

    turtle.mainloop()

#=======================================================
#GLOBAL VARIABLES

#set up screen and pen (turtle).
WN = turtle.Screen()
WN.title ('Let\'s make a sprite!')
#Gets rid of scroll bar by making the screensize smaller than the setup dimensions.
WN.screensize(canvwidth=200, canvheight=200, bg=gen_hex_color())
WN.setup(width=300, height=300)

MOVE = True

#=======================================================
#let's do this!
main()


