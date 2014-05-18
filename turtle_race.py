import turtle              # 1.  import the modules
import random


wn = turtle.Screen()       # 2.  Create a screen


def setup_race():

	wn.bgcolor('lightblue')

	a = turtle.Turtle()
	a.color('blue')
	a.shape('turtle')
	a.speed(1)

	b = turtle.Turtle()
	b.color('red')
	b.shape('turtle')
	b.speed(1)

	goal = turtle.Turtle()
	goal.hideturtle()
	goal.color('green')
	goal.shape('classic')
	goal.pensize(3)
	goal.up()
	goal.goto(300, 50)
	goal.left(-90)
	goal.showturtle()
	goal.down()
	goal.forward(100)

	a.up()                  # 4.  Move the turtles to their starting point
	b.up()
	a.goto(0,20)
	b.goto(0,-20)

	return a, b

# your code goes here

def race(a, b):
	while True:
		first, second = who_first(a, b)
		first.forward(random.randrange(1,11))
		if (first.position()[0] >= 300):
			wn.clear()
			return first
        second.forward(random.randrange(1,11))
        if (second.position()[0] >= 300):
        	wn.clear()
        	return second


def who_first(a, b):
    coin_flip = random.randrange(0,2)
    if coin_flip:
        return a, b
    else:
        return b, a



def match(n):
	a_score = 0
	b_score = 0
	for i in range(n):
		a, b = setup_race()
		winner = race(a, b)
		if winner == a:
			a_score += 1
		elif winner == b:
			b_score += 1
	print a.color(), a_score, b.color(), b_score
	


match(3)
