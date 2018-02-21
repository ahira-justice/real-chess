"""
    By Justice Ahira -> E-mail:justiceahira@gmail.com
    Student, Department of Computer Science, graduating class of 2017/2018,
    Faculty of Science, University of Ibadan, Ibadan.

    start June, 2014.
    end July, 2014.
"""
import os
import pygame
import sys
import time

from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # Centre game window.

FPS = 30  # Frames per sec.
FPSCLOCK = pygame.time.Clock()

# Defining constant variables for color
#          R   G   B
White = (255, 255, 255)
Black = (0, 0, 0)
Ash = (128, 128, 128)
Purple = (128, 0, 128)
PURPLE = (120, 0, 120)

BrightBlue = (0, 128, 255)

WINDOWWIDTH, WINDOWHEIGTH = 600, 600

PRINTFONTSIZE = 35
SMALLFONTSIZE = 10
BASICFONTSIZE = 30
BIGFONTSIZE = 50
ALTFONTSIZE = 16

# Loading all useful image files from C:\justicedev\python\Real_Chess.
'''default directory on my computer for the project development.'''

HUE1 = pygame.image.load('images/White.png')
HUE2 = pygame.image.load('images/Ash.png')

wking = pygame.image.load('images/wking.png')
bking = pygame.image.load('images/bking.png')
wpawn = pygame.image.load('images/wpawn.png')
bpawn = pygame.image.load('images/bpawn.png')
wrook = pygame.image.load('images/wrook.png')
brook = pygame.image.load('images/brook.png')
wbishop = pygame.image.load('images/wbishop.png')
bbishop = pygame.image.load('images/bbishop.png')
wknight = pygame.image.load('images/wknight.png')
bknight = pygame.image.load('images/bknight.png')
wqueen = pygame.image.load('images/wqueen.png')
bqueen = pygame.image.load('images/bqueen.png')

bsidelines = [(550, 100), (550, 150), (550, 200), (550, 250), (550, 300), (550, 350), (550, 400), (550, 450),
              (505, 100), (505, 150), (505, 200), (505, 250), (505, 300), (505, 350), (505, 400), (505, 450)]
wsidelines = [(0, 100), (0, 150), (0, 200), (0, 250), (0, 300), (0, 350), (0, 400), (0, 450),
              (45, 100), (45, 150), (45, 200), (45, 250), (45, 300), (45, 350), (45, 400), (45, 450)]


def main():
    global DISPLAYSURF, BASICFONT, BIGFONT, SMALLFONTa, PRINTFONTa, SMALLFONTb, PRINTFONTb, Piecedrop, Select, bPieces, wPieces, posb, posw, Clicks, firstSelection, secondSelection, a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7, c8, d1, d2, d3, d4, d5, d6, d7, d8, e1, e2, e3, e4, e5, e6, e7, e8, f1, f2, f3, f4, f5, f6, f7, f8, g1, g2, g3, g4, g5, g6, g7, g8, h1, h2, h3, h4, h5, h6, h7, h8
    mousex, mousey = 0, 0
    firstSelection, secondSelection = None, None
    Clicks = [firstSelection, secondSelection]

    highlight = False
    highlighted = None
    firstSelChosen = False

    pygame.init()

    list_of_fonts = pygame.font.get_fonts()
    if 'strokedimension' in list_of_fonts:
        Alternate_font = 'stroke_dimension'
    else:
        Alternate_font = 'calibri'

    # Setting up the GUI window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGTH))
    pygame.display.set_caption('REAL CHESS')
    SMALLFONTa = pygame.font.SysFont('calibri', SMALLFONTSIZE)
    SMALLFONTb = pygame.font.SysFont(Alternate_font, SMALLFONTSIZE)
    BASICFONT = pygame.font.SysFont('calibri', BASICFONTSIZE)
    BIGFONT = pygame.font.SysFont('calibri', BIGFONTSIZE)
    PRINTFONTa = pygame.font.SysFont('calibri', PRINTFONTSIZE)
    PRINTFONTb = pygame.font.SysFont(Alternate_font, PRINTFONTSIZE)
    ALTFONT = pygame.font.Font('fonts/stroke_dimension.ttf', ALTFONTSIZE)
    pygame.display.set_icon(pygame.image.load('images/gameicon.png'))

    a1, a2, a3, a4, a5, a6, a7, a8 = (100, 100), (100, 150), (100, 200), (100, 250), (100, 300), (100, 350), (100, 400), (100, 450)
    b1, b2, b3, b4, b5, b6, b7, b8 = (150, 100), (150, 150), (150, 200), (150, 250), (150, 300), (150, 350), (150, 400), (150, 450)
    c1, c2, c3, c4, c5, c6, c7, c8 = (200, 100), (200, 150), (200, 200), (200, 250), (200, 300), (200, 350), (200, 400), (200, 450)
    d1, d2, d3, d4, d5, d6, d7, d8 = (250, 100), (250, 150), (250, 200), (250, 250), (250, 300), (250, 350), (250, 400), (250, 450)
    e1, e2, e3, e4, e5, e6, e7, e8 = (300, 100), (300, 150), (300, 200), (300, 250), (300, 300), (300, 350), (300, 400), (300, 450)
    f1, f2, f3, f4, f5, f6, f7, f8 = (350, 100), (350, 150), (350, 200), (350, 250), (350, 300), (350, 350), (350, 400), (350, 450)
    g1, g2, g3, g4, g5, g6, g7, g8 = (400, 100), (400, 150), (400, 200), (400, 250), (400, 300), (400, 350), (400, 400), (400, 450)
    h1, h2, h3, h4, h5, h6, h7, h8 = (450, 100), (450, 150), (450, 200), (450, 250), (450, 300), (450, 350), (450, 400), (450, 450)

    Piecedrop = pygame.mixer.Sound('sound/piecedrop.ogg')
    Select = pygame.mixer.Sound('sound/select.ogg')

    posb = [a1, b1, c1, d1, e1, f1, g1, h1, a2, b2, c2, d2, e2, f2, g2, h2]
    posw = [a8, b8, c8, d8, e8, f8, g8, h8, a7, b7, c7, d7, e7, f7, g7, h7]
    DISPLAYSURF.fill(Purple)
    iCECorp()
    while True:  # The main game loop.
        disBoard()
        InfoButton(ALTFONT, 'SETTINGS', Ash, 531, 531)
        InfoRect = InfoButton(ALTFONT, 'SETTINGS', White, 530, 530)
        mouseClicked, mouseMotion = False, False
        Cursor = None

        if highlight:
            drawHighlight(highlighted)

        checkForQuit()
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                mouseMotion = True
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos  # mousex & mousey assigned when there is a click.
                mouseClicked = True

        if mouseMotion and not mouseClicked:  # Portion of code that highlights the pieces on the board
            # when the mouse passes over.
            boxCrossed = boardLeftTopCoords(mousex, mousey)
            if Cursor == None:
                Cursor = boxCrossed
                if Cursor in posb:
                    highlighted = Cursor
                    highlight = True
                elif Cursor in posw:
                    highlighted = Cursor
                    highlight = True
                else:
                    highlighted = None
                    highlight = False

        pieces()

        if mouseClicked and InfoRect.collidepoint(mousex, mousey):
            InfoPage(BASICFONT, White, 20)

        elif mouseClicked and not InfoRect.collidepoint(mousex, mousey):
            if firstSelection == None:
                firstSelection = boardLeftTopCoords(mousex, mousey)
                if firstSelection in posb or firstSelection in posw:
                    Clicks[0] = firstSelection
                    firstSelChosen = True
                    Select.play()
                else:
                    firstSelChosen = False
                    firstSelection = None
            elif Clicks[0] != None and firstSelChosen:
                secondSelection = boardLeftTopCoords(mousex, mousey)
                Clicks[1] = secondSelection
                move = makeMove(Clicks)
                if move == False:
                    Piecedrop.stop()
                else:
                    Piecedrop.play()
                firstSelection, secondSelection = None, None

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back


def checkForKeyPress():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    checkForQuit()

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None


def drawHighlight(pos):
    pygame.draw.rect(DISPLAYSURF, BrightBlue, (pos[0], pos[1], 50, 50), 4)


def makeText(text, color, FONT, centerx, top):
    # create the Surface and Rect objects for some text.
    textSurf = FONT.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.midtop = (centerx, top)
    return (textSurf, textRect)


def printMsg(msg, FONT, color, centerx, top):
    textSurf, textRect = makeText(msg, color, FONT, centerx, top)
    DISPLAYSURF.blit(textSurf, textRect)


def InfoButton(FONT, text, color, left, top):
    InfoSurf = FONT.render(text, True, color, PURPLE)
    InfoRect = InfoSurf.get_rect()
    InfoRect.topleft = (left, top)
    DISPLAYSURF.blit(InfoSurf, InfoRect)
    return InfoRect


def InfoPage(FONT, color, left):
    m = 1
    while checkForKeyPress() == None:
        DISPLAYSURF.fill(Purple)

        textSurfa = FONT.render('REAL CHESS', True, color)
        textRecta = textSurfa.get_rect()
        textRecta.center = (WINDOWWIDTH / 2, 40)

        textSurfb = FONT.render('REAL CHESS', True, Ash)
        textRectb = textSurfb.get_rect()
        textRectb.center = (WINDOWWIDTH / 2 + m, 40 + m)

        DISPLAYSURF.blit(textSurfb, textRectb)
        DISPLAYSURF.blit(textSurfa, textRecta)

        printMsg('Press a key to continue.', SMALLFONTa, Ash, 535 + m, 580 + m)
        printMsg('Press a key to continue.', SMALLFONTa, White, 535, 580)

        pygame.display.update()
        FPSCLOCK.tick(30)


def iCECorp():
    a, b, c = 128, 0, 128
    d, e, f = 128, 0, 128

    p, q, r = 128, 0, 128
    s, t, u = 128, 0, 128
    FinTime = 0
    IniTime = time.time()
    FiniTime = 0
    InitTime = time.time()
    startAnim = False
    while checkForKeyPress() == None:
        DISPLAYSURF.fill(Purple)
        checkForQuit()
        COLOR = (a, b, c)
        color = (d, e, f)

        sCOLOR = (p, q, r)
        scolor = (s, t, u)
        if FinTime - IniTime >= 1:
            checkForQuit()
            printMsg('\'ICE CORP', BIGFONT, color, 302, 202)
            printMsg('\'ICE CORP', BIGFONT, COLOR, 300, 200)

            printMsg('Press a key to play.', SMALLFONTa, color, 551, 581)
            printMsg('Press a key to play.', SMALLFONTa, COLOR, 550, 580)
            startAnim = True
        if a < 255 and startAnim:
            a += 1
            c += 1
            if b <= 255:
                b += 2
        if e < 128 and startAnim:
            e += 1
        if FiniTime - InitTime >= 3.5:
            checkForQuit()
            printMsg('REAL CHESS', PRINTFONTa, scolor, 302, 352)
            printMsg('REAL CHESS', PRINTFONTa, sCOLOR, 300, 350)
            if p < 255 and startAnim:
                p += 1
                r += 1
                if q <= 255:
                    q += 2
            if t < 128 and startAnim:
                t += 1
        FiniTime = time.time()
        FinTime = time.time()
        pygame.display.update()
        FPSCLOCK.tick(45)
    return


def pieces():
    # Defining the Constant Positions of Pieces which is suject to change
    # as the posb[x] and posw[x] list is modified in the following code, where (0 <= x < 16).
    bRook1(posb[0])
    bKnight1(posb[1])
    bBishop1(posb[2])
    bQueen(posb[3])
    bKing(posb[4])
    bBishop2(posb[5])
    bKnight2(posb[6])
    bRook2(posb[7])

    bPawn1(posb[8])
    bPawn2(posb[9])
    bPawn3(posb[10])
    bPawn4(posb[11])
    bPawn5(posb[12])
    bPawn6(posb[13])
    bPawn7(posb[14])
    bPawn8(posb[15])

    wRook1(posw[0])
    wKnight1(posw[1])
    wBishop1(posw[2])
    wQueen(posw[3])
    wKing(posw[4])
    wBishop2(posw[5])
    wKnight2(posw[6])
    wRook2(posw[7])

    wPawn1(posw[8])
    wPawn2(posw[9])
    wPawn3(posw[10])
    wPawn4(posw[11])
    wPawn5(posw[12])
    wPawn6(posw[13])
    wPawn7(posw[14])
    wPawn8(posw[15])
    return


def makeMove(clicks):
    if clicks[0] == clicks[1]:
        return False

    elif (clicks[0] in posw and clicks[1] in posw) or (clicks[0] in posb and clicks[1] in posb):
        return False

    elif clicks[0] != clicks[1]:
        # Iterates when no capture is attempted.    
        if (clicks[0] in posb and clicks[1] not in posw) or (clicks[0] in posw and clicks[1] not in posb):
            if clicks[0] in posb:
                for i in range(len(posb)):
                    if clicks[0] == posb[i]:
                        posb[i] = clicks[1]
                        break
            elif clicks[0] in posw:
                for i in range(len(posw)):
                    if clicks[0] == posw[i]:
                        posw[i] = clicks[1]
                        break
        # Iterates for a black capture.
        elif (clicks[0] in posb and clicks[1] in posw) and not (clicks[0] in posw and clicks[1] in posb):
            if clicks[1] == posw[4]:  # Prevents king capture.
                return False
            for i in range(len(posb)):
                if clicks[0] == posb[i]:
                    for j in range(len(posw)):
                        if clicks[1] == posw[j]:
                            posb[i] = posw[j]
                            posw[j] = wsidelines[j]

        # Iterates for a white capture.
        elif (clicks[0] in posw and clicks[1] in posb) and not (clicks[0] in posb and clicks[1] in posw):
            if clicks[1] == posb[4]:  # Prevents king capture.
                return False
            for i in range(len(posw)):
                if clicks[0] == posw[i]:
                    for j in range(len(posb)):
                        if clicks[1] == posb[j]:
                            posw[i] = posb[j]
                            posb[j] = bsidelines[j]


def boardLeftTopCoords(X,
                       Y):  # This function is lengthy, but is the easiet way to see if a square has been clicked and which square it is.
    if X in range(100, 500) and Y in range(100, 500):
        if X in range(100, 150) and Y in range(100, 150):
            return a1
        elif X in range(150, 200) and Y in range(100, 150):
            return b1
        elif X in range(200, 250) and Y in range(100, 150):
            return c1
        elif X in range(250, 300) and Y in range(100, 150):
            return d1
        elif X in range(300, 350) and Y in range(100, 150):
            return e1
        elif X in range(350, 400) and Y in range(100, 150):
            return f1
        elif X in range(400, 450) and Y in range(100, 150):
            return g1
        elif X in range(450, 500) and Y in range(100, 150):
            return h1

        elif X in range(100, 150) and Y in range(150, 200):
            return a2
        elif X in range(150, 200) and Y in range(150, 200):
            return b2
        elif X in range(200, 250) and Y in range(150, 200):
            return c2
        elif X in range(250, 300) and Y in range(150, 200):
            return d2
        elif X in range(300, 350) and Y in range(150, 200):
            return e2
        elif X in range(350, 400) and Y in range(150, 200):
            return f2
        elif X in range(400, 450) and Y in range(150, 200):
            return g2
        elif X in range(450, 500) and Y in range(150, 200):
            return h2

        elif X in range(100, 150) and Y in range(200, 250):
            return a3
        elif X in range(150, 200) and Y in range(200, 250):
            return b3
        elif X in range(200, 250) and Y in range(200, 250):
            return c3
        elif X in range(250, 300) and Y in range(200, 250):
            return d3
        elif X in range(300, 350) and Y in range(200, 250):
            return e3
        elif X in range(350, 400) and Y in range(200, 250):
            return f3
        elif X in range(400, 450) and Y in range(200, 250):
            return g3
        elif X in range(450, 500) and Y in range(200, 250):
            return h3

        elif X in range(100, 150) and Y in range(250, 300):
            return a4
        elif X in range(150, 200) and Y in range(250, 300):
            return b4
        elif X in range(200, 250) and Y in range(250, 300):
            return c4
        elif X in range(250, 300) and Y in range(250, 300):
            return d4
        elif X in range(300, 350) and Y in range(250, 300):
            return e4
        elif X in range(350, 400) and Y in range(250, 300):
            return f4
        elif X in range(400, 450) and Y in range(250, 300):
            return g4
        elif X in range(450, 500) and Y in range(250, 300):
            return h4

        elif X in range(100, 150) and Y in range(300, 350):
            return a5
        elif X in range(150, 200) and Y in range(300, 350):
            return b5
        elif X in range(200, 250) and Y in range(300, 350):
            return c5
        elif X in range(250, 300) and Y in range(300, 350):
            return d5
        elif X in range(300, 350) and Y in range(300, 350):
            return e5
        elif X in range(350, 400) and Y in range(300, 350):
            return f5
        elif X in range(400, 450) and Y in range(300, 350):
            return g5
        elif X in range(450, 500) and Y in range(300, 350):
            return h5

        elif X in range(100, 150) and Y in range(350, 400):
            return a6
        elif X in range(150, 200) and Y in range(350, 400):
            return b6
        elif X in range(200, 250) and Y in range(350, 400):
            return c6
        elif X in range(250, 300) and Y in range(350, 400):
            return d6
        elif X in range(300, 350) and Y in range(350, 400):
            return e6
        elif X in range(350, 400) and Y in range(350, 400):
            return f6
        elif X in range(400, 450) and Y in range(350, 400):
            return g6
        elif X in range(450, 500) and Y in range(350, 400):
            return h6

        elif X in range(100, 150) and Y in range(400, 450):
            return a7
        elif X in range(150, 200) and Y in range(400, 450):
            return b7
        elif X in range(200, 250) and Y in range(400, 450):
            return c7
        elif X in range(250, 300) and Y in range(400, 450):
            return d7
        elif X in range(300, 350) and Y in range(400, 450):
            return e7
        elif X in range(350, 400) and Y in range(400, 450):
            return f7
        elif X in range(400, 450) and Y in range(400, 450):
            return g7
        elif X in range(450, 500) and Y in range(400, 450):
            return h7

        elif X in range(100, 150) and Y in range(450, 500):
            return a8
        elif X in range(150, 200) and Y in range(450, 500):
            return b8
        elif X in range(200, 250) and Y in range(450, 500):
            return c8
        elif X in range(250, 300) and Y in range(450, 500):
            return d8
        elif X in range(300, 350) and Y in range(450, 500):
            return e8
        elif X in range(350, 400) and Y in range(450, 500):
            return f8
        elif X in range(400, 450) and Y in range(450, 500):
            return g8
        elif X in range(450, 500) and Y in range(450, 500):
            return h8
    else:
        return None


def disBoard():  # Blits imported image to create game board
    DISPLAYSURF.fill(Purple)
    pygame.draw.rect(DISPLAYSURF, Black, (95, 95, 410, 410), 15)

    # White tiles.
    DISPLAYSURF.blit(HUE1, (100, 100))
    DISPLAYSURF.blit(HUE1, (200, 100))
    DISPLAYSURF.blit(HUE1, (300, 100))
    DISPLAYSURF.blit(HUE1, (400, 100))  # Row 1

    DISPLAYSURF.blit(HUE1, (150, 150))
    DISPLAYSURF.blit(HUE1, (250, 150))
    DISPLAYSURF.blit(HUE1, (350, 150))
    DISPLAYSURF.blit(HUE1, (450, 150))  # Row 2

    DISPLAYSURF.blit(HUE1, (100, 200))
    DISPLAYSURF.blit(HUE1, (200, 200))
    DISPLAYSURF.blit(HUE1, (300, 200))
    DISPLAYSURF.blit(HUE1, (400, 200))  # Row 3

    DISPLAYSURF.blit(HUE1, (150, 250))
    DISPLAYSURF.blit(HUE1, (250, 250))
    DISPLAYSURF.blit(HUE1, (350, 250))
    DISPLAYSURF.blit(HUE1, (450, 250))  # Row 4

    DISPLAYSURF.blit(HUE1, (100, 300))
    DISPLAYSURF.blit(HUE1, (200, 300))
    DISPLAYSURF.blit(HUE1, (300, 300))
    DISPLAYSURF.blit(HUE1, (400, 300))  # Row 5

    DISPLAYSURF.blit(HUE1, (150, 350))
    DISPLAYSURF.blit(HUE1, (250, 350))
    DISPLAYSURF.blit(HUE1, (350, 350))
    DISPLAYSURF.blit(HUE1, (450, 350))  # Row 6

    DISPLAYSURF.blit(HUE1, (100, 400))
    DISPLAYSURF.blit(HUE1, (200, 400))
    DISPLAYSURF.blit(HUE1, (300, 400))
    DISPLAYSURF.blit(HUE1, (400, 400))  # Row 7

    DISPLAYSURF.blit(HUE1, (150, 450))
    DISPLAYSURF.blit(HUE1, (250, 450))
    DISPLAYSURF.blit(HUE1, (350, 450))
    DISPLAYSURF.blit(HUE1, (450, 450))  # Row 8

    # Ash tiles.
    DISPLAYSURF.blit(HUE2, (150, 100))
    DISPLAYSURF.blit(HUE2, (250, 100))
    DISPLAYSURF.blit(HUE2, (350, 100))
    DISPLAYSURF.blit(HUE2, (450, 100))  # Row 1

    DISPLAYSURF.blit(HUE2, (100, 150))
    DISPLAYSURF.blit(HUE2, (200, 150))
    DISPLAYSURF.blit(HUE2, (300, 150))
    DISPLAYSURF.blit(HUE2, (400, 150))  # Row 2

    DISPLAYSURF.blit(HUE2, (150, 200))
    DISPLAYSURF.blit(HUE2, (250, 200))
    DISPLAYSURF.blit(HUE2, (350, 200))
    DISPLAYSURF.blit(HUE2, (450, 200))  # Row 3

    DISPLAYSURF.blit(HUE2, (100, 250))
    DISPLAYSURF.blit(HUE2, (200, 250))
    DISPLAYSURF.blit(HUE2, (300, 250))
    DISPLAYSURF.blit(HUE2, (400, 250))  # Row 4

    DISPLAYSURF.blit(HUE2, (150, 300))
    DISPLAYSURF.blit(HUE2, (250, 300))
    DISPLAYSURF.blit(HUE2, (350, 300))
    DISPLAYSURF.blit(HUE2, (450, 300))  # Row 5

    DISPLAYSURF.blit(HUE2, (100, 350))
    DISPLAYSURF.blit(HUE2, (200, 350))
    DISPLAYSURF.blit(HUE2, (300, 350))
    DISPLAYSURF.blit(HUE2, (400, 350))  # Row 6

    DISPLAYSURF.blit(HUE2, (150, 400))
    DISPLAYSURF.blit(HUE2, (250, 400))
    DISPLAYSURF.blit(HUE2, (350, 400))
    DISPLAYSURF.blit(HUE2, (450, 400))  # Row 7

    DISPLAYSURF.blit(HUE2, (100, 450))
    DISPLAYSURF.blit(HUE2, (200, 450))
    DISPLAYSURF.blit(HUE2, (300, 450))
    DISPLAYSURF.blit(HUE2, (400, 450))  # Row 8


# Creating each pieces and giving a 'coord' parameter to place it on a square.
def wPawn1(coord):
    DISPLAYSURF.blit(wpawn, coord)


def wPawn2(coord):
    DISPLAYSURF.blit(wpawn, coord)


def wPawn3(coord):
    DISPLAYSURF.blit(wpawn, coord)


def wPawn4(coord):
    DISPLAYSURF.blit(wpawn, coord)


def wPawn5(coord):
    DISPLAYSURF.blit(wpawn, coord)


def wPawn6(coord):
    DISPLAYSURF.blit(wpawn, coord)


def wPawn7(coord):
    DISPLAYSURF.blit(wpawn, coord)


def wPawn8(coord):
    DISPLAYSURF.blit(wpawn, coord)


def bPawn1(coord):
    DISPLAYSURF.blit(bpawn, coord)


def bPawn2(coord):
    DISPLAYSURF.blit(bpawn, coord)


def bPawn3(coord):
    DISPLAYSURF.blit(bpawn, coord)


def bPawn4(coord):
    DISPLAYSURF.blit(bpawn, coord)


def bPawn5(coord):
    DISPLAYSURF.blit(bpawn, coord)


def bPawn6(coord):
    DISPLAYSURF.blit(bpawn, coord)


def bPawn7(coord):
    DISPLAYSURF.blit(bpawn, coord)


def bPawn8(coord):
    DISPLAYSURF.blit(bpawn, coord)


def wRook1(coord):
    DISPLAYSURF.blit(wrook, coord)


def wRook2(coord):
    DISPLAYSURF.blit(wrook, coord)


def bRook1(coord):
    DISPLAYSURF.blit(brook, coord)


def bRook2(coord):
    DISPLAYSURF.blit(brook, coord)


def wBishop1(coord):
    DISPLAYSURF.blit(wbishop, coord)


def wBishop2(coord):
    DISPLAYSURF.blit(wbishop, coord)


def bBishop1(coord):
    DISPLAYSURF.blit(bbishop, coord)


def bBishop2(coord):
    DISPLAYSURF.blit(bbishop, coord)


def wKnight1(coord):
    DISPLAYSURF.blit(wknight, coord)


def wKnight2(coord):
    DISPLAYSURF.blit(wknight, coord)


def bKnight1(coord):
    DISPLAYSURF.blit(bknight, coord)


def bKnight2(coord):
    DISPLAYSURF.blit(bknight, coord)


def wQueen(coord):
    DISPLAYSURF.blit(wqueen, coord)


def bQueen(coord):
    DISPLAYSURF.blit(bqueen, coord)


def wKing(coord):
    DISPLAYSURF.blit(wking, coord)


def bKing(coord):
    DISPLAYSURF.blit(bking, coord)


if __name__ == '__main__':
    main()
