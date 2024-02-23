import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Circle Animation")

circle_ani = turtle.Turtle()
circle_ani.color("white")

turtle_color_list = ["white", "yellow", "brown", "orange", "pink", "red", "green"]


for element in range(8):
    circle_ani.color(turtle_color_list[element])
    circle_ani.circle(10 * element)
    circle_ani.circle(-10 * element)
    circle_ani.left(element)

turtle.done()
