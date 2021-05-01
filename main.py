# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(201, 164, 112), (238, 246, 241), (152, 75, 49),
              (221, 201, 138), (171, 153, 42), (56, 95, 126), (139, 31, 19), (134, 163, 184), (197, 93, 73),
              (48, 121, 88), (98, 75, 77), (142, 178, 148), (75, 41, 33), (165, 145, 156), (15, 99, 71),
              (234, 175, 164), (54, 45, 47), (32, 61, 77), (145, 21, 25), (21, 83, 89), (182, 205, 175),
              (85, 147, 127), (44, 66, 87), (178, 94, 98), (222, 177, 184), (8, 68, 51), (108, 127, 151)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()






























screen = t.Screen()
screen.exitonclick()
