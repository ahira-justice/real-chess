# By Justice Ahira -> E-mail:justiceahira@gmail.com
# Student, Department of Computer Science, graduating class of 2017/2018,
# Faculty of Science, University of Ibadan, Ibadan.

# start July, 2014.

import sys, pygame, os
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('CHESS')

FPS = 30
FPSCLOCK = pygame.time.Clock()
#Defining constant variables for color
#          R   G   B
White  = (255,255,255)
Black  = (  0,  0,  0)
Ash    = (128,128,128)
Silver = (235,235,235)
Milk   = (255,225,175)

HUE1 = pygame.image.load('build/WHITE.jpg')

DISPLAYSURF.fill(Ash)

def disBoard(): # Blits imported image to create game board
    DISPLAYSURF.blit(HUE1,(  0,  0))
    DISPLAYSURF.blit(HUE1,(150,  0))
    DISPLAYSURF.blit(HUE1,(300,  0))
    DISPLAYSURF.blit(HUE1,(450,  0))# Row 1

    DISPLAYSURF.blit(HUE1,( 75, 75))
    DISPLAYSURF.blit(HUE1,(225, 75))
    DISPLAYSURF.blit(HUE1,(375, 75))
    DISPLAYSURF.blit(HUE1,(525, 75))# Row 2

    DISPLAYSURF.blit(HUE1,(  0,150))
    DISPLAYSURF.blit(HUE1,(150,150))
    DISPLAYSURF.blit(HUE1,(300,150))
    DISPLAYSURF.blit(HUE1,(450,150))# Row 3

    DISPLAYSURF.blit(HUE1,( 75,225))
    DISPLAYSURF.blit(HUE1,(225,225))
    DISPLAYSURF.blit(HUE1,(375,225))
    DISPLAYSURF.blit(HUE1,(525,225))# Row 4

    DISPLAYSURF.blit(HUE1,(  0,300))
    DISPLAYSURF.blit(HUE1,(150,300))
    DISPLAYSURF.blit(HUE1,(300,300))
    DISPLAYSURF.blit(HUE1,(450,300))# Row 5

    DISPLAYSURF.blit(HUE1,( 75,375))
    DISPLAYSURF.blit(HUE1,(225,375))
    DISPLAYSURF.blit(HUE1,(375,375))
    DISPLAYSURF.blit(HUE1,(525,375))# Row 6

    DISPLAYSURF.blit(HUE1,(  0,450))
    DISPLAYSURF.blit(HUE1,(150,450))
    DISPLAYSURF.blit(HUE1,(300,450))
    DISPLAYSURF.blit(HUE1,(450,450))# Row 7

    DISPLAYSURF.blit(HUE1,( 75,525))
    DISPLAYSURF.blit(HUE1,(225,525))
    DISPLAYSURF.blit(HUE1,(375,525))
    DISPLAYSURF.blit(HUE1,(525,525))# Row 8

# The Whole Castle pieces.
def Castle1white(X,Y):
    Pointlist = ((X+22.5,Y+18.75),(X+30.0,Y+18.75),(X+30.0,Y+22.5),(X+33.75,Y+22.5),(X+33.75,Y+18.75),(X+41.25,Y+18.75),(X+41.25,Y+22.5),(X+45.0,Y+22.5),(X+45.0,Y+18.75),(X+52.5,Y+18.75),(X+52.5,Y+30.0),(X+48.75,Y+30.0),(X+48.75,Y+33.75),(X+45.0,Y+37.5),(X+45.0,Y+41.25),(X+48.75,Y+41.25),(X+48.75,Y+60.0),(X+56.25,Y+67.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+67.5),(X+26.25,Y+60.0),(X+26.25,Y+41.25),(X+30.0,Y+41.25),(X+30.0,Y+37.5),(X+26.25,Y+33.75),(X+26.25,Y+30.0),(X+22.5,Y+30.0))
    Castle = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Castle2white(X,Y):
    Pointlist = ((X+22.5,Y+18.75),(X+30.0,Y+18.75),(X+30.0,Y+22.5),(X+33.75,Y+22.5),(X+33.75,Y+18.75),(X+41.25,Y+18.75),(X+41.25,Y+22.5),(X+45.0,Y+22.5),(X+45.0,Y+18.75),(X+52.5,Y+18.75),(X+52.5,Y+30.0),(X+48.75,Y+30.0),(X+48.75,Y+33.75),(X+45.0,Y+37.5),(X+45.0,Y+41.25),(X+48.75,Y+41.25),(X+48.75,Y+60.0),(X+56.25,Y+67.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+67.5),(X+26.25,Y+60.0),(X+26.25,Y+41.25),(X+30.0,Y+41.25),(X+30.0,Y+37.5),(X+26.25,Y+33.75),(X+26.25,Y+30.0),(X+22.5,Y+30.0))
    Castle = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Castle1black(X,Y):
    Pointlist = ((X+22.5,Y+18.75),(X+30.0,Y+18.75),(X+30.0,Y+22.5),(X+33.75,Y+22.5),(X+33.75,Y+18.75),(X+41.25,Y+18.75),(X+41.25,Y+22.5),(X+45.0,Y+22.5),(X+45.0,Y+18.75),(X+52.5,Y+18.75),(X+52.5,Y+30.0),(X+48.75,Y+30.0),(X+48.75,Y+33.75),(X+45.0,Y+37.5),(X+45.0,Y+41.25),(X+48.75,Y+41.25),(X+48.75,Y+60.0),(X+56.25,Y+67.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+67.5),(X+26.25,Y+60.0),(X+26.25,Y+41.25),(X+30.0,Y+41.25),(X+30.0,Y+37.5),(X+26.25,Y+33.75),(X+26.25,Y+30.0),(X+22.5,Y+30.0))
    Castle = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

def Castle2black(X,Y):
    Pointlist = ((X+22.5,Y+18.75),(X+30.0,Y+18.75),(X+30.0,Y+22.5),(X+33.75,Y+22.5),(X+33.75,Y+18.75),(X+41.25,Y+18.75),(X+41.25,Y+22.5),(X+45.0,Y+22.5),(X+45.0,Y+18.75),(X+52.5,Y+18.75),(X+52.5,Y+30.0),(X+48.75,Y+30.0),(X+48.75,Y+33.75),(X+45.0,Y+37.5),(X+45.0,Y+41.25),(X+48.75,Y+41.25),(X+48.75,Y+60.0),(X+56.25,Y+67.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+67.5),(X+26.25,Y+60.0),(X+26.25,Y+41.25),(X+30.0,Y+41.25),(X+30.0,Y+37.5),(X+26.25,Y+33.75),(X+26.25,Y+30.0),(X+22.5,Y+30.0))
    Castle = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

# The Whole Knight pieces.
def Knight1white(X,Y):
    Pointlist = ((X+18.75,Y+31.875),(X+48.75,Y+11.5),(X+56.25,Y+18.75),(X+52.5,Y+30.125),(X+52.5,Y+52.5),(X+48.75,Y+63.8),(X+52.5,Y+63.8),(X+56.25,Y+67.55),(X+52.5,Y+71.25),(X+56.25,Y+71.25),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+71.25),(X+22.5,Y+71.25),(X+18.75,Y+67.55),(X+22.5,Y+63.8),(X+26.25,Y+63.8),(X+22.5,Y+60.0),(X+18.75,Y+60.0),(X+18.75,Y+52.5),(X+33.75,Y+45.0),(X+33.75,Y+37.5),(X+30.0,Y+45.0),(X+18.75,Y+45.0))
    Knight = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Knight2white(X,Y):
    Pointlist = ((X+18.75,Y+31.875),(X+48.75,Y+11.5),(X+56.25,Y+18.75),(X+52.5,Y+30.125),(X+52.5,Y+52.5),(X+48.75,Y+63.8),(X+52.5,Y+63.8),(X+56.25,Y+67.55),(X+52.5,Y+71.25),(X+56.25,Y+71.25),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+71.25),(X+22.5,Y+71.25),(X+18.75,Y+67.55),(X+22.5,Y+63.8),(X+26.25,Y+63.8),(X+22.5,Y+60.0),(X+18.75,Y+60.0),(X+18.75,Y+52.5),(X+33.75,Y+45.0),(X+33.75,Y+37.5),(X+30.0,Y+45.0),(X+18.75,Y+45.0))
    Knight = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Knight1black(X,Y):
    Pointlist = ((X+18.75,Y+31.875),(X+48.75,Y+11.5),(X+56.25,Y+18.75),(X+52.5,Y+30.125),(X+52.5,Y+52.5),(X+48.75,Y+63.8),(X+52.5,Y+63.8),(X+56.25,Y+67.55),(X+52.5,Y+71.25),(X+56.25,Y+71.25),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+71.25),(X+22.5,Y+71.25),(X+18.75,Y+67.55),(X+22.5,Y+63.8),(X+26.25,Y+63.8),(X+22.5,Y+60.0),(X+18.75,Y+60.0),(X+18.75,Y+52.5),(X+33.75,Y+45.0),(X+33.75,Y+37.5),(X+30.0,Y+45.0),(X+18.75,Y+45.0))
    Knight = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

def Knight2black(X,Y):
    Pointlist = ((X+18.75,Y+31.875),(X+48.75,Y+11.5),(X+56.25,Y+18.75),(X+52.5,Y+30.125),(X+52.5,Y+52.5),(X+48.75,Y+63.8),(X+52.5,Y+63.8),(X+56.25,Y+67.55),(X+52.5,Y+71.25),(X+56.25,Y+71.25),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+71.25),(X+22.5,Y+71.25),(X+18.75,Y+67.55),(X+22.5,Y+63.8),(X+26.25,Y+63.8),(X+22.5,Y+60.0),(X+18.75,Y+60.0),(X+18.75,Y+52.5),(X+33.75,Y+45.0),(X+33.75,Y+37.5),(X+30.0,Y+45.0),(X+18.75,Y+45.0))
    Knight = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

# The Whole Bishop pieces.
def Bishop1white(X,Y):
    Pointlist = ((X+33.75,Y+11.25),(X+37.5,Y+11.25),(X+37.5,Y+15.0),(X+33.75,Y+22.5),(X+41.25,Y+15.0),(X+44.5,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+28.25),(X+44.5,Y+30.0),(X+44.5,Y+41.25),(X+52.5,Y+48.75),(X+48.75,Y+48.75),(X+48.75,Y+60.0),(X+56.25,Y+63.75),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+63.75),(X+26.25,Y+60.0),(X+26.25,Y+48.75),(X+22.5,Y+48.75),(X+30.0,Y+41.25),(X+30.0,Y+30.0),(X+26.25,Y+26.25),(X+26.25,Y+18.75),(X+30.0,Y+15.0),(X+33.75,Y+15.0))
    Bishop = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Bishop2white(X,Y):
    Pointlist = ((X+33.75,Y+11.25),(X+37.5,Y+11.25),(X+37.5,Y+15.0),(X+33.75,Y+22.5),(X+41.25,Y+15.0),(X+44.5,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+28.25),(X+44.5,Y+30.0),(X+44.5,Y+41.25),(X+52.5,Y+48.75),(X+48.75,Y+48.75),(X+48.75,Y+60.0),(X+56.25,Y+63.75),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+63.75),(X+26.25,Y+60.0),(X+26.25,Y+48.75),(X+22.5,Y+48.75),(X+30.0,Y+41.25),(X+30.0,Y+30.0),(X+26.25,Y+26.25),(X+26.25,Y+18.75),(X+30.0,Y+15.0),(X+33.75,Y+15.0))
    Bishop = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Bishop1black(X,Y):
    Pointlist = ((X+33.75,Y+11.25),(X+37.5,Y+11.25),(X+37.5,Y+15.0),(X+33.75,Y+22.5),(X+41.25,Y+15.0),(X+44.5,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+28.25),(X+44.5,Y+30.0),(X+44.5,Y+41.25),(X+52.5,Y+48.75),(X+48.75,Y+48.75),(X+48.75,Y+60.0),(X+56.25,Y+63.75),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+63.75),(X+26.25,Y+60.0),(X+26.25,Y+48.75),(X+22.5,Y+48.75),(X+30.0,Y+41.25),(X+30.0,Y+30.0),(X+26.25,Y+26.25),(X+26.25,Y+18.75),(X+30.0,Y+15.0),(X+33.75,Y+15.0))
    Bishop = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

def Bishop2black(X,Y):
    Pointlist = ((X+33.75,Y+11.25),(X+37.5,Y+11.25),(X+37.5,Y+15.0),(X+33.75,Y+22.5),(X+41.25,Y+15.0),(X+44.5,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+28.25),(X+44.5,Y+30.0),(X+44.5,Y+41.25),(X+52.5,Y+48.75),(X+48.75,Y+48.75),(X+48.75,Y+60.0),(X+56.25,Y+63.75),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+63.75),(X+26.25,Y+60.0),(X+26.25,Y+48.75),(X+22.5,Y+48.75),(X+30.0,Y+41.25),(X+30.0,Y+30.0),(X+26.25,Y+26.25),(X+26.25,Y+18.75),(X+30.0,Y+15.0),(X+33.75,Y+15.0))
    Bishop = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

# The Whole Pawn pieces.
def Pawn1white(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Pawn2white(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Pawn3white(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Pawn4white(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Pawn5white(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Pawn6white(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Pawn7white(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Pawn8white(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Pawn1black(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

def Pawn2black(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

def Pawn3black(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

def Pawn4black(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

def Pawn5black(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

def Pawn6black(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

def Pawn7black(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

def Pawn8black(X,Y):
    Pointlist = ((X+30.0,Y+15.0),(X+45.0,Y+15.0),(X+48.75,Y+18.75),(X+48.75,Y+22.5),(X+45.0,Y+26.25),(X+45.0,Y+34.7),(X+46.875,Y+34.7),(X+48.75,Y+36.6),(X+48.75,Y+39.375),(X+46.875,Y+41.25),(X+45.0,Y+41.25),(X+45.0,Y+56.25),(X+56.25,Y+65.5),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+65.5),(X+30.0,Y+56.25),(X+30.0,Y+41.25),(X+28.125,Y+41.25),(X+26.25,Y+39.375),(X+26.25,Y+36.6),(X+28.125,Y+34.7),(X+30.0,Y+34.7),(X+30.0,Y+26.25),(X+26.25,Y+22.5),(X+26.25,Y+18.75))
    Pawn = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)

# The Whole King pieces.
def Kingwhite(X,Y):
    Pointlist = ((X+34.6875,Y+5.625),(X+40.3125,Y+5.625),(X+40.3125,Y+9.375),(X+44.0625,Y+9.375),(X+44.0625,Y+13.125),(X+40.3125,Y+13.125),(X+40.3125,Y+16.875),(X+48.75,Y+16.875),(X+48.75,Y+24.375),(X+45.0,Y+31.875),(X+45.0,Y+46.875),(X+46.875,Y+46.875),(X+46.875,Y+50.625),(X+56.25,Y+60.0),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+60.0),(X+28.125,Y+50.625),(X+28.125,Y+46.875),(X+30.0,Y+46.875),(X+30.0,Y+31.875),(X+26.25,Y+24.375),(X+26.25,Y+16.875),(X+34.6875,Y+16.875),(X+34.6875,Y+9.375))
    King = pygame.draw.polygon(DISPLAYSURF, Milk, Pointlist)

def Kingblack(X,Y):
    Pointlist = ((X+34.6875,Y+5.625),(X+40.3125,Y+5.625),(X+40.3125,Y+9.375),(X+44.0625,Y+9.375),(X+44.0625,Y+13.125),(X+40.3125,Y+13.125),(X+40.3125,Y+16.875),(X+48.75,Y+16.875),(X+48.75,Y+24.375),(X+45.0,Y+31.875),(X+45.0,Y+46.875),(X+46.875,Y+46.875),(X+46.875,Y+50.625),(X+56.25,Y+60.0),(X+56.25,Y+75.0),(X+18.75,Y+75.0),(X+18.75,Y+60.0),(X+28.125,Y+50.625),(X+28.125,Y+46.875),(X+30.0,Y+46.875),(X+30.0,Y+31.875),(X+26.25,Y+24.375),(X+26.25,Y+16.875),(X+34.6875,Y+16.875),(X+34.6875,Y+9.375))
    King = pygame.draw.polygon(DISPLAYSURF, Black, Pointlist)


def main():
    global conD 
    mouseClicked = False
    conD = False

    while not conD:
        disBoard()
        
        # Default Position of all pieces.
        Castle1white(0,525)
        Castle2white(525,525)
        Castle1black(0,0)
        Castle2black(525,0)
        Knight1white(75,525)
        Knight2white(450,525)
        Knight1black(450,0)
        Knight2black(75,0)
        Bishop1white(150,525)
        Bishop2white(375,525)
        Bishop1black(150,0)
        Bishop2black(375,0)
        Kingwhite(300, 525)
        Kingblack(300, 0)
        Pawn1white(0,450)
        Pawn2white(75,450)
        Pawn3white(150,450)
        Pawn4white(225,450)
        Pawn5white(300,450)
        Pawn6white(375,450)
        Pawn7white(450,450)
        Pawn8white(525,450)
        Pawn1black(0,75)
        Pawn2black(75,75)
        Pawn3black(150,75)
        Pawn4black(225,75)
        Pawn5black(300,75)
        Pawn6black(375,75)
        Pawn7black(450,75)
        Pawn8black(525,75)
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        if mouseClicked == True:
            if mousex in range(0,76):
                if mousey in range(0,76):
                    Castle1black(0,300)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
