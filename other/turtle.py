from turtle import *
for steps in range(100):
    for i in ('green', 'purple', 'blue'):
        color(i)
        forward(steps)
        right(30)