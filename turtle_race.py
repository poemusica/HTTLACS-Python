import turtle          
import random
import time

#=======================================================

#generate a random hex color.
def gen_hex_color():
    color = ['#']
    for i in range(6):
        color.append(random.choice('0123456789ABCDEF'))
    return ''.join(color)

def update_score(score1, score2, t1, t2, winner):
	if winner == t1:
			score1 += 1
	elif winner == t2:
		score2 += 1
	return score1, score2

def who_first(a, b):
    coin_flip = random.randrange(0,2)
    if coin_flip:
        return a, b
    else:
        return b, a

def race(a, b):
	count_down(3)
	while True:
		first, second = who_first(a, b)
		first.forward(random.randrange(1,11))
		if (first.position()[0] >= 300):
			return first
        second.forward(random.randrange(1,11))
        if (second.position()[0] >= 300):
        	return second

def count_down(n):
	for i in range(n):
		print str(n-i) + "..."
		time.sleep(0.5)
	print "GO!"

def setup_racers(a, b):
	WN.tracer(0)
	a.goto(0,20)
	b.goto(0,-20)
	WN.tracer(1)

def draw_goal():
	goal = turtle.Turtle()
	goal.pen(shown=False, pencolor='black', pensize=3, pendown=False)
	goal.goto(300, 50)
	goal.lt(-90)
	goal.down()
	goal.fd(100)

def get_names():
	print "Which turtles are racing today?"
	name1 = raw_input("Turtle 1 name: ")
	name2 = raw_input("Turtle 2 name: ")
	print "Great! Let's get ready to race!"
	return name1, name2

def make_turtle():
	c = gen_hex_color()
	t = turtle.Turtle()
	t.pen(speed = 1, fillcolor=c, pencolor=c, pendown=False)
	t.shape('turtle')
	return t

def main():
	print "Two turtles race. Best of three."
	WN.tracer(0)
	a = make_turtle()
	b = make_turtle()
	name1, name2 = get_names()
	names = {a:name1, b:name2}
	a.goto(-10,35)
	b.goto(-10,-50)
	font = ('Arial', 16, "normal")
	a.write(names[a], font=font)
	b.write(names[b], font=font)
	draw_goal()
	WN.tracer(1)

	a_score = 0
	b_score = 0
	for i in range(3):
		setup_racers(a, b)
		time.sleep(1)
		winner = race(a, b)
		a_score, b_score = update_score(a_score, b_score, a, b, winner)
		print names[a] + ': ' + str(a_score) + ', ' + names[b] + ': ' + str(b_score)
	
	scores = {a_score: name1, b_score: name2}
	print scores[max(a_score, b_score)]+ ' wins! \nThanks for attending the the turtle race.'  
	WN.exitonclick()
	

#=======================================================
#GLOBAL VARIABLES

WN = turtle.Screen()
WN.title('Welcome to Turtle Racing!')
WN.bgcolor('lightblue')

#=======================================================
main()
