# import colorgram
# colors = colorgram.extract('image.jpg',30)
# rgb_colors = []
# for color in colors :
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors .append(new_color)
# print(rgb_colors)

import turtle as t
import random
t.colormode(255)
color_list = [(186, 249, 245), (209, 165, 124), (249, 234, 236), (140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56), (215, 234, 231), (241, 65, 140), (1, 143, 184), (162, 55, 51), (50, 203, 226), (254, 230, 0), (20, 166, 126), (244, 223, 49), (210, 231, 234), (171, 186, 177), (27, 197, 220), (232, 165, 190), (233, 174, 161), (141, 213, 224), (191, 191, 193), (160, 211, 182), (105, 46, 100), (8, 117, 39)]
tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_count % 10 == 0 :
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = Screen()
screen.exitonclick()
