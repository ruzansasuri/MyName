'''
myname.py
To draw last name using 6 distinct characters and repeating 1 character
Version: $Id myname.py 1.0 8/25/2016 rps7183
'''
__author__ = "Ruzan Sasuri"

import turtle
import math

LINESIZE = 20

def drawP():
    '''
    precondition: Start point of Letter with pen up
    postcondition: Start point of next letter with pen up
    :return:
    '''
    turtle.down()
    turtle.left(90)
    turtle.forward(2*LINESIZE)
    turtle.right(90)
    turtle.forward(LINESIZE)
    turtle.right(90)
    turtle.forward(LINESIZE)
    turtle.right(90)
    turtle.forward(LINESIZE)
    turtle.up()
    turtle.left(90)
    turtle.forward(LINESIZE)
    turtle.left(90)
    turtle.forward(2*LINESIZE)

def drawS():
    '''
    precondition: Start point of Letter with pen up
    postcondition: Start point of next letter with pen up
    :return:
    '''
    turtle.down()
    turtle.forward(LINESIZE)
    turtle.left(90)
    turtle.forward(LINESIZE)
    turtle.left(90)
    turtle.forward(LINESIZE)
    turtle.right(90)
    turtle.forward(LINESIZE)
    turtle.right(90)
    turtle.forward(LINESIZE)
    turtle.up()
    turtle.right(90)
    turtle.forward(2*LINESIZE)
    turtle.left(90)
    turtle.forward(LINESIZE)

def drawA():
    '''
    precondition: Start point of Letter with pen up
    postcondition: Start point of next letter with pen up
    :return:
    '''
    turtle.down()
    turtle.left(90)
    turtle.forward(2*LINESIZE)
    turtle.right(90)
    turtle.forward(LINESIZE)
    turtle.right(90)
    turtle.forward(2*LINESIZE)
    turtle.up()
    turtle.right(180)
    turtle.forward(LINESIZE)
    turtle.left(90)
    turtle.down()
    turtle.forward(LINESIZE)
    turtle.up()
    turtle.right(180)
    turtle.forward(LINESIZE)
    turtle.right(90)
    turtle.forward(LINESIZE)
    turtle.left(90)
    turtle.forward(LINESIZE)

def drawU():
    '''
    precondition: Start point of Letter with pen up
    postcondition: Start point of next letter with pen up
    :return:
    '''
    turtle.left(90)
    turtle.forward(2*LINESIZE)
    turtle.right(180)
    turtle.down()
    turtle.forward(2*LINESIZE)
    turtle.left(90)
    turtle.forward(LINESIZE)
    turtle.left(90)
    turtle.forward(2*LINESIZE)
    turtle.up()
    turtle.right(180)
    turtle.forward(2*LINESIZE)
    turtle.left(90)
    turtle.forward(LINESIZE)

def drawR():
    '''
    precondition: Start point of Letter with pen up
    postcondition: Starrt point of next letter with pen up
    :return:
    '''
    turtle.down()
    turtle.left(90)
    turtle.forward(2*LINESIZE)
    turtle.right(90)
    turtle.forward(LINESIZE)
    turtle.right(90)
    turtle.forward(LINESIZE)
    turtle.right(90)
    turtle.forward(LINESIZE)
    turtle.left(135)
    turtle.forward(LINESIZE*math.sqrt(2))
    turtle.up()
    turtle.left(45)
    turtle.forward(LINESIZE)

def drawI():
    '''
    precondition: Start point of Letter with pen up
    postcondition: Starrt point of next letter with pen up
    :return:
    '''
    turtle.down()
    turtle.forward(2*LINESIZE)
    turtle.up()
    turtle.right(180)
    turtle.forward(LINESIZE)
    turtle.right(90)
    turtle.down()
    turtle.forward(2*LINESIZE)
    turtle.left(90)
    turtle.up()
    turtle.forward(LINESIZE)
    turtle.right(180)
    turtle.down()
    turtle.forward(2*LINESIZE)
    turtle.up()
    turtle.right(90)
    turtle.forward(2*LINESIZE)
    turtle.left(90)
    turtle.forward(LINESIZE)

def draw():
    '''
    Draws all the letters
    precondition: At starting position with pen up
    postcondition: At
    :return:
    '''
    turtle.speed(0)
    turtle.up();
    drawP()
    drawS()
    drawA()
    drawS()
    drawU()
    drawR()
    drawI()
    turtle.mainloop()

if __name__ == "__main__":
    draw()