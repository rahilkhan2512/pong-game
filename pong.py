#!/usr/bin/env python3

import turtle

wn = turtle.Screen()
wn.title("Ping Pong game")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0) # stops the window from updating

# Main game loop

while True:
    wn.update()