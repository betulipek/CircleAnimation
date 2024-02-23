import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Circle Animation")

circle_ani = turtle.Turtle()
circle_ani.color("white")

for element in range(10):
    circle_ani.circle(10 * element)
    circle_ani.circle(-10 * element)
    circle_ani.left(element)

turtle.done()
