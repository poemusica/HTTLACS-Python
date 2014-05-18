

    for i in reversed(range(n)):
        WN.tracer(0) #do not draw screen.
        t = turtle.Turtle()
        t.color(gen_hex_color())
        t.shape('leg')
        t.setheading(start_angle)
        WN.tracer(1) #reset tracer to draw (every) screen.
        angle = (leg_angle * i)
        t.speed((angle / 80) + 1) #speed is inversely proportional to the angle of rotation.
        t.left(angle)

    WN.update() #make sure everything was drawn to the screen.
    time.sleep(1) #pause

    #collect leg turtles.
    all_turtles = WN.turtles()
    all_turtles.remove(middle) #get all legs

    t.speed((((t.heading() + leg_angle) - start_angle) / 80) + 1) #speed is inversely proportional to the angle of rotation.
