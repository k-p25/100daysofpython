# import colorgram 
import turtle as t
import random

t.colormode(255)

# colors = colorgram.extract("hirst spot painting.jpg", 20)

# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))
# print(color_list)
color_list = [(29, 41, 60), (49, 92, 143), (145, 81, 44), (170, 14, 28), (160, 56, 87), (227, 154, 8), (209, 162, 105), (235, 217, 75), (66, 30, 43), (37, 142, 47), (222, 225, 4), (48, 36, 30), (46, 47, 96), (95, 193, 168), (120, 161, 172), (19, 54, 47)]   

tim = t.Turtle()
x_coord = -220
y_coord = -220
tim.teleport(x_coord, y_coord)
for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
    y_coord += 50
    tim.teleport(x_coord, y_coord)
tim.hideturtle()


screen = t.Screen()
screen = t.exitonclick()