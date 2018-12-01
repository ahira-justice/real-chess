"""
    Real Chess
    By Ahira Justice, ADEFOKUN -> E-mail:justiceahira@gmail.com
    Student, Department of Computer Science, graduating class of 2017/2018,
    Faculty of Science, University of Ibadan, Ibadan.

    start July, 2014.
    end February, 2016.
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
#                 R    G    B
White =         (255, 255, 255)
Black =         (  0,   0,   0)
Purple =        (128,   0, 128)
ASH =           (128, 128, 128)
Ash =           ( 70,  70,  70)
Red =           (255,  50,  50)
Green =         ( 50, 200,  50)
CheckRed =      (255,   0,   0)
BrightBlue =    (  0, 150, 255)

BGCOLOR = Purple

WHITE = 'WHITE'
BLACK = 'BLACK'

WINDOWWIDTH, WINDOWHEIGHT = 600, 600
PRINTFONTSIZE = 35
SMALLFONTSIZE = 10
BASICFONTSIZE = 30
BIGFONTSIZE = 50
ALTFONTSIZE = 20
ALTFONT1SIZE = 16

YES = 'YES'
NO = 'NO'

# Loading all useful image files.

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

bsidelines = [(505, 100), (505, 150), (505, 200), (505, 250), (505, 300), (505, 350), (505, 400), (505, 450),
              (550, 100), (550, 150), (550, 200), (550, 250), (550, 300), (550, 350), (550, 400), (550, 450)]
wsidelines = [(45, 100), (45, 150), (45, 200), (45, 250), (45, 300), (45, 350), (45, 400), (45, 450),
              (0, 100), (0, 150), (0, 200), (0, 250), (0, 300), (0, 350), (0, 400), (0, 450)]


def main():
    global DISPLAYSURF, BASICFONT, BIGFONT, SMALLFONT, PRINTFONT, ALTFONT, ALTFONT1
    pygame.init()

    # Setting up the GUI window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('REAL CHESS')
    SMALLFONT = pygame.font.SysFont('calibri', SMALLFONTSIZE)
    BASICFONT = pygame.font.SysFont('calibri', BASICFONTSIZE)
    BIGFONT = pygame.font.SysFont('calibri', BIGFONTSIZE)
    PRINTFONT = pygame.font.SysFont('calibri', PRINTFONTSIZE)
    ALTFONT = pygame.font.Font('fonts/stroke_dimension.ttf', ALTFONTSIZE)
    ALTFONT1 = pygame.font.Font('fonts/stroke_dimension.ttf', ALTFONT1SIZE)

    #pygame.display.set_icon(pygame.image.load('images/gameicon.png'))
    
    iCECorpAnim()
    # Run the main game.
    while True:
        checkForQuit()
        if runGame() is False:
            break
    terminate()


def runGame():
    # Plays a single game of Chess each time this function is called.
    global Piecedrop, Select, bPieces, wPieces, posb, posw, Clicks, firstSelection, secondSelection
    global a1, a2, a3, a4, a5, a6, a7, a8, \
        b1, b2, b3, b4, b5, b6, b7, b8, \
        c1, c2, c3, c4, c5, c6, c7, c8, \
        d1, d2, d3, d4, d5, d6, d7, d8, \
        e1, e2, e3, e4, e5, e6, e7, e8, \
        f1, f2, f3, f4, f5, f6, f7, f8, \
        g1, g2, g3, g4, g5, g6, g7, g8, \
        h1, h2, h3, h4, h5, h6, h7, h8

    mousex, mousey = 0, 0
    highlight = False
    highlighted = None
    firstSelChosen = False
    firstSelection, secondSelection = None, None
    Clicks = [firstSelection, secondSelection]

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

    bindex, windex = 0, 0
    posb = [a1, b1, c1, d1, e1, f1, g1, h1,
            a2, b2, c2, d2, e2, f2, g2, h2]

    posw = [a8, b8, c8, d8, e8, f8, g8, h8,
            a7, b7, c7, d7, e7, f7, g7, h7]

    DISPLAYSURF.fill(BGCOLOR)
    dispBoard()
    playerPiece, computerPiece = enterPlayerPiece()

    if playerPiece is 'BLACK':
        played = True
    elif playerPiece is 'WHITE':
        played = False

    while True:  # The main game loop.
        cmousex, cmousey = 0, 0
        cHighlight = False
        cHighlighted = None
        cFirstSelChosen = False
        cFirstSelection, cSecondSelection = None, None
        cClicks = [cFirstSelection, cSecondSelection]

        checkForQuit()
        DISPLAYSURF.fill(BGCOLOR)
        dispBoard()
        OptionsRect = OptionsButton(ALTFONT1, 'OPTIONS', White, 530, 530)
        mouseClicked, mouseMotion = False, False
        Cursor = None

        if played is False:
            printMsg('WHITE\'S TURN', BASICFONT, White, WINDOWWIDTH / 2, 520)
        elif played is True:
            printMsg('BLACK\'S TURN', BASICFONT, Black, WINDOWWIDTH / 2, 50)

        while kingInCheck(played):  # Restricts the game and forces checked player to make a move to save his king
            checkForQuit()
            dispBoard()
            cOptionsRect = OptionsButton(ALTFONT1, 'OPTIONS', White, 530, 530)
            cMouseClicked, cMouseMotion = False, False
            cCursor = None

            game_over = gameover(played)
            while game_over:
                checkForQuit()

                if played is False:
                    printMsg('CHECKMATE', PRINTFONT, White, WINDOWWIDTH / 2 + 1, 521)
                    printMsg('CHECKMATE', PRINTFONT, CheckRed, WINDOWWIDTH / 2, 520)
                    drawHighlight(posw[4], CheckRed)
                elif played is True:
                    printMsg('CHECKMATE', PRINTFONT, White, WINDOWWIDTH / 2 + 1, 51)
                    printMsg('CHECKMATE', PRINTFONT, CheckRed, WINDOWWIDTH / 2, 50)
                    drawHighlight(posb[4], CheckRed)

                pieces()

                play_again = playAgain()
                if play_again is 'YES':
                    return True
                elif play_again is 'NO':
                    return False

            if played is False:
                printMsg('CHECK', PRINTFONT, White, WINDOWWIDTH / 2 + 1, 521)
                printMsg('CHECK', PRINTFONT, CheckRed, WINDOWWIDTH / 2, 520)
                drawHighlight(posw[4], CheckRed)
            elif played is True:
                printMsg('CHECK', PRINTFONT, White, WINDOWWIDTH / 2 + 1, 51)
                printMsg('CHECK', PRINTFONT, CheckRed, WINDOWWIDTH / 2, 50)
                drawHighlight(posb[4], CheckRed)

            if cHighlight:
                drawHighlight(cHighlighted, BrightBlue)

            # event handling loop
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()

                if event.type == MOUSEMOTION:
                    cmousex, cmousey = event.pos
                    cMouseMotion = True

                if event.type == MOUSEBUTTONUP:
                    cmousex, cmousey = event.pos  # cmousex & cmousey assigned when there is a click.
                    cMouseClicked = True

                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        terminate()
                    if event.key == K_r:
                        pieces()
                        if restart() is YES:
                            runGame()

            if cMouseMotion and not cMouseClicked:
                # Portion of code that highlights the pieces on the board when the mouse passes over.
                boxCrossed = boardLeftTopCoords(cmousex, cmousey)
                if cCursor is None:
                    cCursor = boxCrossed
                    if cCursor in posb:
                        cHighlighted = cCursor
                        cHighlight = True
                    elif cCursor in posw:
                        cHighlighted = cCursor
                        cHighlight = True
                    else:
                        cHighlighted = None
                        cHighlight = False

            if cMouseClicked and cOptionsRect.collidepoint(cmousex, cmousey):
                OptionsPage(BASICFONT)

            if cMouseClicked and not cOptionsRect.collidepoint(cmousex, cmousey):
                if cFirstSelection is None and played is False:
                    cFirstSelection = boardLeftTopCoords(cmousex, cmousey)
                    if cFirstSelection in posw:
                        cClicks[0] = cFirstSelection
                        cFirstSelChosen = True
                        Select.play()
                    else:
                        cFirstSelChosen = False
                        cFirstSelection = None
                elif cFirstSelection is None and played is True:
                    cFirstSelection = boardLeftTopCoords(cmousex, cmousey)
                    if cFirstSelection in posb:
                        cClicks[0] = cFirstSelection
                        cFirstSelChosen = True
                        Select.play()
                    else:
                        cFirstSelChosen = False
                        cFirstSelection = None
                elif cClicks[0] is not None and cFirstSelChosen:
                    cSecondSelection = boardLeftTopCoords(cmousex, cmousey)
                    cClicks[1] = cSecondSelection
                    Moves = isCheck_Mate(played, cClicks)
                    move = makeMove(cClicks, windex, bindex, Moves)
                    if cSecondSelection and move is not False and played is False:
                        played = True
                    elif cSecondSelection and move is not False and played is True:
                        played = False
                    if move is False:
                        Piecedrop.stop()
                    else:
                        Piecedrop.play()
                        if move[0] is True:
                            windex += 1
                        elif move[1] is True:
                            bindex += 1
                    cFirstSelection, cSecondSelection = None, None

            if cFirstSelection is not None:
                iMoves = isCheck_Mate(played, cClicks)
                Moves = removeInValidKingMoves(cClicks, iMoves)
                Remove, remIntercept = removeInValidPieceMoves(cClicks)
                if cClicks[0] in Remove:
                    Moves = InterceptPiece(remIntercept, Moves, cClicks, Remove)
                Moves.append(cClicks[0])
                for Move in Moves:
                    if Move != cClicks[0]:
                        color = BrightBlue
                    else:
                        color = Green
                    drawHighlight(Move, color)

            pieces()

            checkForQuit()
            pygame.display.update()
            FPSCLOCK.tick(FPS)

        if highlight:
            drawHighlight(highlighted, BrightBlue)

        # event handling loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                mouseMotion = True

            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos  # mousex & mousey assigned when there is a click.
                mouseClicked = True

            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_r:
                    pieces()
                    if restart() is YES:
                        runGame()

        if mouseMotion and not mouseClicked:
            # Portion of code that highlights the pieces on the board when the mouse passes over.
            boxCrossed = boardLeftTopCoords(mousex, mousey)
            if Cursor is None:
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

        if mouseClicked and OptionsRect.collidepoint(mousex, mousey):
            OptionsPage(BASICFONT)

        if mouseClicked and not OptionsRect.collidepoint(mousex, mousey):
            if firstSelection is None and played is False:
                firstSelection = boardLeftTopCoords(mousex, mousey)
                if firstSelection in posw:
                    Clicks[0] = firstSelection
                    firstSelChosen = True
                    Select.play()
                else:
                    firstSelChosen = False
                    firstSelection = None
            elif firstSelection is None and played is True:
                firstSelection = boardLeftTopCoords(mousex, mousey)
                if firstSelection in posb:
                    Clicks[0] = firstSelection
                    firstSelChosen = True
                    Select.play()
                else:
                    firstSelChosen = False
                    firstSelection = None
            elif Clicks[0] is not None and firstSelChosen:
                secondSelection = boardLeftTopCoords(mousex, mousey)
                Clicks[1] = secondSelection
                Moves = calculatePosMoves(Clicks)
                move = makeMove(Clicks, windex, bindex, Moves)
                if secondSelection and move is not False and played is False:
                    played = True
                elif secondSelection and move is not False and played is True:
                    played = False
                if move is False:
                    Piecedrop.stop()
                else:
                    Piecedrop.play()
                    if move[0] is True:
                        windex += 1
                    elif move[1] is True:
                        bindex += 1
                firstSelection, secondSelection = None, None

        if firstSelection is not None:
            afterClick(Clicks)

        pieces()

        checkForQuit()
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


def enterPlayerPiece():
    # Draws the text and handles the mouse click events for letting
    # the player choose which color they want to be.  Returns
    # [WHITE, BLACK] if the player chooses to be White,
    # [BLACK, WHITE] if Black.

    # Create the text.
    xSurf = ALTFONT.render('white', True, White, ASH)
    xRect = xSurf.get_rect()
    xRect.center = (int(WINDOWWIDTH / 2) - 40, int(WINDOWHEIGHT / 2))

    oSurf = ALTFONT.render('black', True, Black, ASH)
    oRect = oSurf.get_rect()
    oRect.center = (int(WINDOWWIDTH / 2) + 40, int(WINDOWHEIGHT / 2))

    while True:
        # Keep looping until the player has clicked on a color.
        checkForQuit()

        # event handling loop
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if xRect.collidepoint((mousex, mousey)):
                    return [WHITE, BLACK]
                elif oRect.collidepoint((mousex, mousey)):
                    return [BLACK, WHITE]

        # Draw the screen.
        DISPLAYSURF.blit(xSurf, xRect)
        DISPLAYSURF.blit(oSurf, oRect)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def drawHighlight(pos, color):
    pygame.draw.rect(DISPLAYSURF, color, (pos[0] + 2, pos[1] + 2, 46, 46))


def makeText(text, FONT, color, centerx, top):
    # create the Surface and Rect objects for some text.
    textSurf = FONT.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.midtop = (centerx, top)
    return textSurf, textRect


def printMsg(msg, FONT, color, centerx, top):
    textSurf, textRect = makeText(msg, FONT, color, centerx, top)
    DISPLAYSURF.blit(textSurf, textRect)


def OptionsButton(FONT, text, color, left, top):
    OptionsSurf = FONT.render(text, True, color, Ash)
    OptionsRect = OptionsSurf.get_rect()
    OptionsRect.topleft = (left, top)
    DISPLAYSURF.blit(OptionsSurf, OptionsRect)
    return OptionsRect


def OptionsPage(FONT):
    m = 1
    while checkForKeyPress() is None:
        checkForQuit()
        DISPLAYSURF.fill(BGCOLOR)

        textSurfa = FONT.render('REAL CHESS', True, White)
        textRecta = textSurfa.get_rect()
        textRecta.center = (WINDOWWIDTH / 2, 40)

        textSurfb = FONT.render('REAL CHESS', True, ASH)
        textRectb = textSurfb.get_rect()
        textRectb.center = (WINDOWWIDTH / 2 + m, 40 + m)

        DISPLAYSURF.blit(textSurfb, textRectb)
        DISPLAYSURF.blit(textSurfa, textRecta)

        printMsg('Press a key to continue.', SMALLFONT, ASH, 535 + m, 580 + m)
        printMsg('Press a key to continue.', SMALLFONT, White, 535, 580)

        pygame.display.update()
        FPSCLOCK.tick(FPS)
    dispBoard()


def iCECorpAnim():
    a, b, c = 128, 0, 128
    d, e, f = 128, 0, 128

    p, q, r = 128, 0, 128
    s, t, u = 128, 0, 128
    FinTime = time.time()
    IniTime = time.time()
    FiniTime = time.time()
    InitTime = time.time()
    startAnim = False
    while checkForKeyPress() is None:
        DISPLAYSURF.fill(BGCOLOR)
        checkForQuit()
        COLOR = (a, b, c)
        color = (d, e, f)

        sCOLOR = (p, q, r)
        scolor = (s, t, u)
        if FinTime - IniTime >= 1:
            checkForQuit()
            printMsg('\'iCE CORP', BIGFONT, color, 302, 202)
            printMsg('\'iCE CORP', BIGFONT, COLOR, 300, 200)

            printMsg('Press a key to play.', SMALLFONT, color, 551, 581)
            printMsg('Press a key to play.', SMALLFONT, COLOR, 550, 580)
            startAnim = True
        if a < 255 and startAnim:
            a += 1
            c += 1
            if b <= 255:
                b += 2
        if e < 128 and startAnim:
            e += 1
        if FiniTime - InitTime >= 2.5:
            checkForQuit()
            printMsg('REAL CHESS', PRINTFONT, scolor, 302, 352)
            printMsg('REAL CHESS', PRINTFONT, sCOLOR, 300, 350)
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
        FPSCLOCK.tick(FPS)
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


def calculatePieceChosen(clicks, POS):
    # Meant to reduce the bulk of the calculatePosMoves() and as its name implies, calculates the chosen piece.
    PIECE = ['rook1', 'knight1', 'bishop1', 'queen', 'king', 'bishop2', 'knight2', 'rook2', 'pawn1', 'pawn2', 'pawn3',
             'pawn4', 'pawn5', 'pawn6', 'pawn7', 'pawn8']
    index = 0
    if clicks[0] in POS[0]:
        POSIT = POS[0], 'black'
    elif clicks[0] in POS[1]:
        POSIT = POS[1], 'white'
    for pos in POSIT[0]:
        if clicks[0] == pos:
            pieceChosen = PIECE[index]
            break
        index += 1
    return pieceChosen, POSIT


def calIndexOrder(testList, Direction):
    # Used to calculate the min and max values in a given testList. Used in the removeInValidMoves().
    index = None
    if len(testList) > 0:
        if Direction in ('Up', 'Left'):
            Num = max(testList)
            index = testList.index(Num)
        elif Direction in ('Down', 'Right'):
            Num = min(testList)
            index = testList.index(Num)
    return index


def restart():
    # Draws the text and handles the mouse click events for letting
    # the player choose which if they want to play again.  Returns
    # YES if the player chooses to play again,
    # NO if not.

    # Create the text.
    textSurf = ALTFONT.render('restart?', True, White, ASH)
    textRect = textSurf.get_rect()
    textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))

    xSurf = ALTFONT.render('Yes', True, White, ASH)
    xRect = xSurf.get_rect()
    xRect.center = (int(WINDOWWIDTH / 2) - 30, int(WINDOWHEIGHT / 2) + 40)

    oSurf = ALTFONT.render(' No ', True, White, ASH)
    oRect = oSurf.get_rect()
    oRect.center = (int(WINDOWWIDTH / 2) + 30, int(WINDOWHEIGHT / 2) + 40)

    while True:
        # Keep looping until the player has clicked on an option.
        checkForQuit()
        for event in pygame.event.get():  # event handling loop
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if xRect.collidepoint((mousex, mousey)):
                    return YES
                elif oRect.collidepoint((mousex, mousey)):
                    return NO

        # Draw the screen.
        DISPLAYSURF.blit(textSurf, textRect)
        DISPLAYSURF.blit(xSurf, xRect)
        DISPLAYSURF.blit(oSurf, oRect)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def playAgain():
    # Draws the text and handles the mouse click events for letting
    # the player choose which if they want to play again.  Returns
    # 'YES' if the player chooses to play again,
    # 'NO' if not.

    # Create the text.
    textSurf = ALTFONT.render('play again?', True, White, ASH)
    textRect = textSurf.get_rect()
    textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))

    xSurf = ALTFONT.render('Yes', True, Black, ASH)
    xRect = xSurf.get_rect()
    xRect.center = (int(WINDOWWIDTH / 2) - 30, int(WINDOWHEIGHT / 2) + 40)

    oSurf = ALTFONT.render(' No ', True, Black, ASH)
    oRect = oSurf.get_rect()
    oRect.center = (int(WINDOWWIDTH / 2) + 30, int(WINDOWHEIGHT / 2) + 40)

    CheckMate = pygame.mixer.Sound('sound/voicecheckmate.ogg')
    CheckMate.play()

    while True:
        # Keep looping until the player has clicked on an option.
        checkForQuit()

        # event handling loop
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if xRect.collidepoint((mousex, mousey)):
                    return 'YES'
                elif oRect.collidepoint((mousex, mousey)):
                    return 'NO'

        # Draw the screen.
        DISPLAYSURF.blit(textSurf, textRect)
        DISPLAYSURF.blit(xSurf, xRect)
        DISPLAYSURF.blit(oSurf, oRect)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def oppPosiCaptures(pos, ThreatPiece=None):
    # Computes the argument's sides possible captures based
    # on the current location of every piece on that side.
    oppSideMoves = []
    PawnCaptures = []
    if ThreatPiece is None:
        for i in range(0, 8):
            fList = [pos[i], None]
            iValidMoves = calculatePosMoves(fList)
            oppSideMoves.append(iValidMoves)

        for i in range(8, 16):
            if pos == posb:
                CoordOfPawn = pos[i]
                pawnCaptures = (CoordOfPawn[0] - 50, CoordOfPawn[1] + 50), (CoordOfPawn[0] + 50, CoordOfPawn[1] + 50)
                PawnCaptures.append(pawnCaptures)
            elif pos == posw:
                CoordOfPawn = pos[i]
                pawnCaptures = (CoordOfPawn[0] - 50, CoordOfPawn[1] - 50), (CoordOfPawn[0] + 50, CoordOfPawn[1] - 50)
                PawnCaptures.append(pawnCaptures)

    else:
        if ThreatPiece[0] != []:
            for i in ThreatPiece[0]:
                fList = [i, None]
                iValidMoves = calculatePosMoves(fList)
                oppSideMoves.append(iValidMoves)

        elif ThreatPiece[1] != []:
            for i in ThreatPiece[1]:
                if pos == posb:
                    CoordOfPawn = i
                    pawnCaptures = (CoordOfPawn[0] - 50, CoordOfPawn[1] + 50), (
                        CoordOfPawn[0] + 50, CoordOfPawn[1] + 50)
                    PawnCaptures.append(pawnCaptures)
                elif pos == posw:
                    CoordOfPawn = i
                    pawnCaptures = (CoordOfPawn[0] - 50, CoordOfPawn[1] - 50), (
                        CoordOfPawn[0] + 50, CoordOfPawn[1] - 50)
                    PawnCaptures.append(pawnCaptures)

    return oppSideMoves, PawnCaptures


def kingInCheck(played):
    if played is True:  # Black.
        KingPos = posb[4]
        oppSideMoves, PawnCaptures = oppPosiCaptures(posw)
        for i in range(len(oppSideMoves)):
            if KingPos in oppSideMoves[i]:
                return True

        for i in range(len(PawnCaptures)):
            if KingPos in PawnCaptures[i]:
                return True

    elif played is False:  # White.
        KingPos = posw[4]
        oppSideMoves, PawnCaptures = oppPosiCaptures(posb)
        for i in range(len(oppSideMoves)):
            if KingPos in oppSideMoves[i]:
                return True

        for i in range(len(PawnCaptures)):
            if KingPos in PawnCaptures[i]:
                return True

    return False


def isCheck_Mate(played, clicks):
    checkForQuit()
    ThreatPiece, pThreatPiece = [], []
    intercept = []
    xintervals, yintervals = [], []
    Moves = []
    iposMoves = calculatePosMoves(clicks)
    currentMoves = removeInValidKingMoves(clicks, iposMoves)

    if kingInCheck(played):
        if played is True:  # Black.
            oppSideMoves, PawnCaptures = oppPosiCaptures(posw)
            for i in range(len(oppSideMoves)):
                for j in oppSideMoves[i]:
                    if j == posb[4]:
                        ThreatPiece.append(posw[i])
            for i in range(len(PawnCaptures)):
                for j in PawnCaptures[i]:
                    if j == posb[4]:
                        pThreatPiece.append(posw[i + 7])

            # The King may move to a square which is not being attacked by an enemy piece
            if clicks[0] == posb[4]:
                if currentMoves != []:
                    for i in currentMoves:
                        Moves.append(i)

            # The piece that is threatening the King can be captured.
            if ThreatPiece != []:
                for i in currentMoves:
                    if i in ThreatPiece:
                        Moves.append(i)
            elif pThreatPiece != []:
                for i in currentMoves:
                    if i in pThreatPiece:
                        Moves.append(i)

            # A piece may be moved in between the black King and the attacking white piece to block the check.
            if ThreatPiece != []:
                king = posb[4]
                Piece = ThreatPiece[0]
                threateningPiece, POSIT = calculatePieceChosen([Piece, None], [posb, posw])
                if threateningPiece in ['rook1', 'rook2']:
                    if Piece[0] == king[0]:
                        lowLimit = min([Piece[1], king[1]])
                        upLimit = max([Piece[1], king[1]])
                        for i in range(lowLimit, upLimit, 50):
                            intercept.append((king[0], i))
                    elif Piece[1] == king[1]:
                        lowLimit = min([Piece[0], king[0]])
                        upLimit = max([Piece[0], king[0]])
                        for i in range(lowLimit, upLimit, 50):
                            intercept.append((i, king[1]))

                elif threateningPiece in ['bishop1', 'bishop2']:
                    xlowLimit = min([Piece[0], king[0]])
                    xupLimit = max([Piece[0], king[0]])
                    ylowLimit = min([Piece[1], king[1]])
                    yupLimit = max([Piece[1], king[1]])

                    for i in range(xlowLimit, xupLimit + 50, 50):
                        xintervals.append(i)
                    for i in range(ylowLimit, yupLimit + 50, 50):
                        yintervals.append(i)

                    if king[0] > Piece[0] and king[1] < Piece[1]:
                        yintervals.reverse()
                    elif king[0] < Piece[0] and king[1] > Piece[1]:
                        yintervals.reverse()

                    for i in range(len(xintervals)):
                        intercept.append((xintervals[i], yintervals[i]))

                elif threateningPiece == 'queen':
                    if Piece[0] == king[0]:
                        lowLimit = min([Piece[1], king[1]])
                        upLimit = max([Piece[1], king[1]])
                        for i in range(lowLimit, upLimit, 50):
                            intercept.append((king[0], i))
                    elif Piece[1] == king[1]:
                        lowLimit = min([Piece[0], king[0]])
                        upLimit = max([Piece[0], king[0]])
                        for i in range(lowLimit, upLimit, 50):
                            intercept.append((i, king[1]))
                    else:
                        xlowLimit = min([Piece[0], king[0]])
                        xupLimit = max([Piece[0], king[0]])
                        ylowLimit = min([Piece[1], king[1]])
                        yupLimit = max([Piece[1], king[1]])

                        for i in range(xlowLimit, xupLimit + 50, 50):
                            xintervals.append(i)
                        for i in range(ylowLimit, yupLimit + 50, 50):
                            yintervals.append(i)

                        if king[0] > Piece[0] and king[1] < Piece[1]:
                            yintervals.reverse()
                        elif king[0] < Piece[0] and king[1] > Piece[1]:
                            yintervals.reverse()

                        for i in range(len(xintervals)):
                            intercept.append((xintervals[i], yintervals[i]))

                for i in intercept:
                    if i == Piece or i == king:
                        intercept.remove(i)

                currentMoves = calculatePosMoves(clicks)
                if clicks[0] != posb[4]:
                    for i in intercept:
                        for j in currentMoves:
                            if j == i:
                                Moves.append(j)

        elif played is False:  # White.
            oppSideMoves, PawnCaptures = oppPosiCaptures(posb)
            for i in range(len(oppSideMoves)):
                for j in oppSideMoves[i]:
                    if j == posw[4]:
                        ThreatPiece.append(posb[i])
            for i in range(len(PawnCaptures)):
                for j in PawnCaptures[i]:
                    if j == posw[4]:
                        pThreatPiece.append(posb[i + 7])

            # The King may move to a square which is not being attacked by an enemy piece
            if clicks[0] == posw[4]:
                if currentMoves != []:
                    for i in currentMoves:
                        Moves.append(i)

            # The piece that is threatening the King can be captured.
            if ThreatPiece != []:
                for i in currentMoves:
                    if i in ThreatPiece:
                        Moves.append(i)
            elif pThreatPiece != []:
                for i in currentMoves:
                    if i in pThreatPiece:
                        Moves.append(i)

            # A piece may be moved in between the black King and the attacking white piece to block the check.
            if ThreatPiece != []:
                king = posw[4]
                Piece = ThreatPiece[0]
                threateningPiece, POSIT = calculatePieceChosen([Piece, None], [posb, posw])
                if threateningPiece in ['rook1', 'rook2']:
                    if Piece[0] == king[0]:
                        lowLimit = min([Piece[1], king[1]])
                        upLimit = max([Piece[1], king[1]])
                        for i in range(lowLimit, upLimit, 50):
                            intercept.append((king[0], i))
                    elif Piece[1] == king[1]:
                        lowLimit = min([Piece[0], king[0]])
                        upLimit = max([Piece[0], king[0]])
                        for i in range(lowLimit, upLimit, 50):
                            intercept.append((i, king[1]))

                elif threateningPiece in ['bishop1', 'bishop2']:
                    xlowLimit = min([Piece[0], king[0]])
                    xupLimit = max([Piece[0], king[0]])
                    ylowLimit = min([Piece[1], king[1]])
                    yupLimit = max([Piece[1], king[1]])

                    for i in range(xlowLimit, xupLimit + 50, 50):
                        xintervals.append(i)
                    for i in range(ylowLimit, yupLimit + 50, 50):
                        yintervals.append(i)

                    if king[0] > Piece[0] and king[1] < Piece[1]:
                        yintervals.reverse()
                    elif king[0] < Piece[0] and king[1] > Piece[1]:
                        yintervals.reverse()

                    for i in range(len(xintervals)):
                        intercept.append((xintervals[i], yintervals[i]))

                elif threateningPiece == 'queen':
                    if Piece[0] == king[0]:
                        lowLimit = min([Piece[1], king[1]])
                        upLimit = max([Piece[1], king[1]])
                        for i in range(lowLimit, upLimit, 50):
                            intercept.append((king[0], i))
                    elif Piece[1] == king[1]:
                        lowLimit = min([Piece[0], king[0]])
                        upLimit = max([Piece[0], king[0]])
                        for i in range(lowLimit, upLimit, 50):
                            intercept.append((i, king[1]))
                    else:
                        xlowLimit = min([Piece[0], king[0]])
                        xupLimit = max([Piece[0], king[0]])
                        ylowLimit = min([Piece[1], king[1]])
                        yupLimit = max([Piece[1], king[1]])

                        for i in range(xlowLimit, xupLimit + 50, 50):
                            xintervals.append(i)
                        for i in range(ylowLimit, yupLimit + 50, 50):
                            yintervals.append(i)

                        if king[0] > Piece[0] and king[1] < Piece[1]:
                            yintervals.reverse()
                        elif king[0] < Piece[0] and king[1] > Piece[1]:
                            yintervals.reverse()

                        for i in range(len(xintervals)):
                            intercept.append((xintervals[i], yintervals[i]))

                for i in intercept:
                    if i == Piece or i == king:
                        intercept.remove(i)

                currentMoves = calculatePosMoves(clicks)
                if clicks[0] != posw[4]:
                    for i in intercept:
                        for j in currentMoves:
                            if j == i:
                                Moves.append(j)
        return Moves


def gameover(played):
    Moves = []
    counter = []
    if played is True:
        pos = posb
    elif played is False:
        pos = posw

    for i in pos:
        if (i[0] < 100 or i[0] > 450) or (i[1] < 100 or i[1] > 450):  # Out of bounds.
            Moves.append([])
        else:
            fList = [i, None]
            iMoves = isCheck_Mate(played, fList)
            Moves.append(iMoves)

    for i in Moves:
        if i == []:
            counter.append(0)
        elif i != []:
            counter.append(1)
    if 1 in counter:
        return False
    else:
        return True


def potentialThreats(clicks):
    checkForQuit()
    startx, starty = 0, 0
    pieceChosen, POSIT = calculatePieceChosen(clicks, [posb, posw])
    possibleMoves = []
    newpossibleMoves = []
    positions = [[a1, b1, c1, d1, e1, f1, g1, h1],
                 [a2, b2, c2, d2, e2, f2, g2, h2],
                 [a3, b3, c3, d3, e3, f3, g3, h3],
                 [a4, b4, c4, d4, e4, f4, g4, h4],
                 [a5, b5, c5, d5, e5, f5, g5, h5],
                 [a6, b6, c6, d6, e6, f6, g6, h6],
                 [a7, b7, c7, d7, e7, f7, g7, h7],
                 [a8, b8, c8, d8, e8, f8, g8, h8]]

    fClick = clicks[0]
    for x in range(len(positions)):
        for y in range(len(positions[x])):
            if positions[x][y] == fClick:
                startx, starty = x, y
                break

    if pieceChosen in ['rook1', 'rook2']:  # Rook has been chosen.
        for i in range(8):
            possibleMoves.append(positions[startx][i])
            possibleMoves.append(positions[i][starty])

    elif pieceChosen in ['bishop1', 'bishop2']:  # Bishop has been chosen.
        for i in range(8):
            if (startx - i) >= 0 and (starty - i) >= 0:
                possibleMoves.append(positions[startx - i][starty - i])
            if (startx - i) >= 0 and (starty + i) <= 7:
                possibleMoves.append(positions[startx - i][starty + i])
            if (startx + i) <= 7 and (starty - i) >= 0:
                possibleMoves.append(positions[startx + i][starty - i])
            if (startx + i) <= 7 and (starty + i) <= 7:
                possibleMoves.append(positions[startx + i][starty + i])

    elif pieceChosen == 'queen':  # Queen has been chosen(This is a reimplementation of rook and bishop possibleMoves code).
        for i in range(8):
            possibleMoves.append(positions[startx][i])
            possibleMoves.append(positions[i][starty])
        for i in range(8):
            if (startx - i) >= 0 and (starty - i) >= 0:
                possibleMoves.append(positions[startx - i][starty - i])
            if (startx - i) >= 0 and (starty + i) <= 7:
                possibleMoves.append(positions[startx - i][starty + i])
            if (startx + i) <= 7 and (starty - i) >= 0:
                possibleMoves.append(positions[startx + i][starty - i])
            if (startx + i) <= 7 and (starty + i) <= 7:
                possibleMoves.append(positions[startx + i][starty + i])

    for i in possibleMoves:
        if i not in newpossibleMoves:
            newpossibleMoves.append(i)

    possibleMoves = newpossibleMoves
    if positions[startx][starty] in possibleMoves:
        possibleMoves.remove(positions[startx][starty])

    return possibleMoves


def Intercept(Piece, king, pos):
    checkForQuit()
    intercept = []
    xintervals, yintervals = [], []
    if Piece in [pos[0], pos[7]]:  # Rooks.
        if Piece[0] == king[0]:
            lowLimit = min([Piece[1], king[1]])
            upLimit = max([Piece[1], king[1]])
            for i in range(lowLimit, upLimit, 50):
                intercept.append((king[0], i))
        elif Piece[1] == king[1]:
            lowLimit = min([Piece[0], king[0]])
            upLimit = max([Piece[0], king[0]])
            for i in range(lowLimit, upLimit, 50):
                intercept.append((i, king[1]))
    elif Piece in [pos[2], pos[5]]:  # Bishops.
        xlowLimit = min([Piece[0], king[0]])
        xupLimit = max([Piece[0], king[0]])
        ylowLimit = min([Piece[1], king[1]])
        yupLimit = max([Piece[1], king[1]])

        for i in range(xlowLimit, xupLimit + 50, 50):
            xintervals.append(i)
        for i in range(ylowLimit, yupLimit + 50, 50):
            yintervals.append(i)

        if king[0] > Piece[0] and king[1] < Piece[1]:
            yintervals.reverse()
        elif king[0] < Piece[0] and king[1] > Piece[1]:
            yintervals.reverse()

        for i in range(len(xintervals)):
            intercept.append((xintervals[i], yintervals[i]))

    elif Piece == pos[3]:  # Queen.
        if Piece[0] == king[0]:
            lowLimit = min([Piece[1], king[1]])
            upLimit = max([Piece[1], king[1]])
            for i in range(lowLimit, upLimit, 50):
                intercept.append((king[0], i))
        elif Piece[1] == king[1]:
            lowLimit = min([Piece[0], king[0]])
            upLimit = max([Piece[0], king[0]])
            for i in range(lowLimit, upLimit, 50):
                intercept.append((i, king[1]))
        else:
            xlowLimit = min([Piece[0], king[0]])
            xupLimit = max([Piece[0], king[0]])
            ylowLimit = min([Piece[1], king[1]])
            yupLimit = max([Piece[1], king[1]])

            for i in range(xlowLimit, xupLimit + 50, 50):
                xintervals.append(i)
            for i in range(ylowLimit, yupLimit + 50, 50):
                yintervals.append(i)

            if king[0] > Piece[0] and king[1] < Piece[1]:
                yintervals.reverse()
            elif king[0] < Piece[0] and king[1] > Piece[1]:
                yintervals.reverse()

            for i in range(len(xintervals)):
                intercept.append((xintervals[i], yintervals[i]))

    return intercept


def InterceptPiece(Intercept, iMoves, clicks, Remove):
    Moves = []
    for i in range(len(Remove)):
        for j in Intercept:
            if clicks[0] == Remove[i] and Remove[i] in j:
                remIntercept = j
    for i in iMoves:
        if i in remIntercept:
            Moves.append(i)
    return Moves


def removeInValidPieceMoves(clicks):
    checkForQuit()
    potentialThreatsMoves = []
    potentialThreatPieces = []
    intercept = []
    Remove = []
    remIntercept = []
    if clicks[0] in posb:  # Black.
        loopList = [0, 2, 3, 5, 7]
        king = posb[4]

        for i in loopList:
            fList = [posw[i], None]
            iThreatMoves = potentialThreats(fList)
            potentialThreatsMoves.append(iThreatMoves)

        for i in range(len(potentialThreatsMoves)):
            for j in potentialThreatsMoves[i]:
                if j == king:
                    potentialThreatPieces.append(posw[loopList[i]])

        for i in range(len(potentialThreatPieces) - 1, -1, -1):
            Piece = potentialThreatPieces[i]
            if (Piece[0] < 100 or Piece[0] > 450) or (Piece[1] < 100 or Piece[1] > 450):  # Out of bounds.
                continue

            intercept = Intercept(Piece, king, posw)

            for i in intercept:
                if i == Piece or i == king:
                    intercept.remove(i)

            index = 0
            for i in posb:
                if i in intercept:
                    index += 1
            if index >= 2:
                potentialThreatPieces.remove(Piece)

            for i in posw:
                if i in intercept and Piece in potentialThreatPieces:
                    potentialThreatPieces.remove(Piece)

            intercept = []

        if potentialThreatPieces != []:
            for i in range(len(potentialThreatPieces) - 1, -1, -1):
                Piece = potentialThreatPieces[i]
                if (Piece[0] < 100 or Piece[0] > 450) or (Piece[1] < 100 or Piece[1] > 450):  # Out of bounds.
                    continue
                intercept = Intercept(Piece, king, posw)
                for i in posb:
                    if i in intercept:
                        Remove.append(i)
                        remIntercept.append(intercept)
            for i in range(len(Remove) - 1, -1, -1):
                if Remove[i] == king:
                    del Remove[i]

    elif clicks[0] in posw:  # White.
        loopList = [0, 2, 3, 5, 7]
        king = posw[4]

        for i in loopList:
            fList = [posb[i], None]
            iThreatMoves = potentialThreats(fList)
            potentialThreatsMoves.append(iThreatMoves)

        for i in range(len(potentialThreatsMoves)):
            for j in potentialThreatsMoves[i]:
                if j == king:
                    potentialThreatPieces.append(posb[loopList[i]])

        for i in range(len(potentialThreatPieces) - 1, -1, -1):
            Piece = potentialThreatPieces[i]
            if (Piece[0] < 100 or Piece[0] > 450) or (Piece[1] < 100 or Piece[1] > 450):  # Out of bounds.
                continue
            intercept = Intercept(Piece, king, posb)

            for i in intercept:
                if i == Piece or i == king:
                    intercept.remove(i)

            index = 0
            for i in posw:
                if i in intercept:
                    index += 1
            if index >= 2:
                potentialThreatPieces.remove(Piece)

            for i in posb:
                if i in intercept and Piece in potentialThreatPieces:
                    potentialThreatPieces.remove(Piece)

            intercept = []

        if potentialThreatPieces != []:
            for Piece in potentialThreatPieces:
                if (Piece[0] < 100 or Piece[0] > 450) or (Piece[1] < 100 or Piece[1] > 450):  # Out of bounds.
                    continue
                intercept = Intercept(Piece, king, posb)
                for i in posw:
                    if i in intercept:
                        Remove.append(i)
                        remIntercept.append(intercept)
            for i in range(len(Remove) - 1, -1, -1):
                if Remove[i] == king:
                    del Remove[i]

    return Remove, remIntercept


def removeInValidMoves(PossibleMoves, clicks, POS, startx, starty, positions, pawnState):
    checkForQuit()
    # Empty lists used to store tuples corresponding to each name.

    Up, Down, Left, Right = [], [], [], []  # Four lists used to calculate the first obstructions encountered by rook pieces and removal of the PossibleMoves behind them.

    UpLeft, UpRight, DownLeft, DownRight = [], [], [], []  # Four lists used to calculate the first obstructions encountered by bishop and queen pieces and removal of the PossibleMoves behind them.

    posTaken = []  # List used to store all PossibleMoves that occur on occupied squares.
    Remove = []  # List used to store moves to be removed from PossibleMoves.
    pieceChosen, POSIT = calculatePieceChosen(clicks, POS)
    for pos in PossibleMoves:
        if pos in POS[0]:
            posTaken.append(pos)
    for pos in PossibleMoves:
        if pos in POS[1]:
            posTaken.append(pos)
    for pos in posTaken:
        if pos == positions[startx][starty]:
            posTaken.remove(pos)

    if pieceChosen in ['rook1', 'rook2']:  # Rook has been chosen.

        for pos in posTaken:
            if pos[0] == positions[startx][starty][0] and pos[1] < positions[startx][starty][1]:
                Up.append(pos)
            elif pos[0] == positions[startx][starty][0] and pos[1] > positions[startx][starty][1]:
                Down.append(pos)
            elif pos[0] < positions[startx][starty][0] and pos[1] == positions[startx][starty][1]:
                Left.append(pos)
            elif pos[0] > positions[startx][starty][0] and pos[1] == positions[startx][starty][1]:
                Right.append(pos)

        if len(Up) > 0:
            index = calIndexOrder(Up, 'Up')
            Obstruc = Up[index]
            for pos in PossibleMoves:
                if Obstruc[0] == pos[0] and Obstruc[1] > pos[1]:
                    Remove.append(pos)
        if len(Down) > 0:
            index = calIndexOrder(Down, 'Down')
            Obstruc = Down[index]
            for pos in PossibleMoves:
                if Obstruc[0] == pos[0] and Obstruc[1] < pos[1]:
                    Remove.append(pos)
        if len(Left) > 0:
            index = calIndexOrder(Left, 'Left')
            Obstruc = Left[index]
            for pos in PossibleMoves:
                if Obstruc[0] > pos[0] and Obstruc[1] == pos[1]:
                    Remove.append(pos)
        if len(Right) > 0:
            index = calIndexOrder(Right, 'Right')
            Obstruc = Right[index]
            for pos in PossibleMoves:
                if Obstruc[0] < pos[0] and Obstruc[1] == pos[1]:
                    Remove.append(pos)

    elif pieceChosen in ['bishop1', 'bishop2']:  # Bishop has been chosen.

        for pos in posTaken:
            if pos[0] < positions[startx][starty][0] and pos[1] < positions[startx][starty][1]:
                UpLeft.append(pos)
            elif pos[0] > positions[startx][starty][0] and pos[1] < positions[startx][starty][1]:
                UpRight.append(pos)
            elif pos[0] < positions[startx][starty][0] and pos[1] > positions[startx][starty][1]:
                DownLeft.append(pos)
            elif pos[0] > positions[startx][starty][0] and pos[1] > positions[startx][starty][1]:
                DownRight.append(pos)

        if len(UpLeft) > 0:
            index = calIndexOrder(UpLeft, 'Left')
            ObstrucLeft = UpLeft[index]
            index = calIndexOrder(UpLeft, 'Up')
            ObstrucUp = UpLeft[index]
            Obstruc = (ObstrucLeft[0], ObstrucUp[1])
            for pos in PossibleMoves:
                if Obstruc[0] > pos[0] and Obstruc[1] > pos[1]:
                    Remove.append(pos)
        if len(UpRight) > 0:
            index = calIndexOrder(UpRight, 'Right')
            Obstruc = UpRight[index]
            for pos in PossibleMoves:
                if Obstruc[0] < pos[0] and Obstruc[1] > pos[1]:
                    Remove.append(pos)
        if len(DownLeft) > 0:
            index = calIndexOrder(DownLeft, 'Left')
            Obstruc = DownLeft[index]
            for pos in PossibleMoves:
                if Obstruc[0] > pos[0] and Obstruc[1] < pos[1]:
                    Remove.append(pos)
        if len(DownRight) > 0:
            index = calIndexOrder(DownRight, 'Right')
            ObstrucRight = DownRight[index]
            index = calIndexOrder(DownRight, 'Down')
            ObstrucDown = DownRight[index]
            Obstruc = (ObstrucRight[0], ObstrucDown[1])
            for pos in PossibleMoves:
                if Obstruc[0] < pos[0] and Obstruc[1] < pos[1]:
                    Remove.append(pos)

    elif pieceChosen == 'queen':  # Queen has been chosen(This code is just a reimplementation of rook and bishop removal code).

        for pos in posTaken:
            if pos[0] == positions[startx][starty][0] and pos[1] < positions[startx][starty][1]:
                Up.append(pos)
            elif pos[0] == positions[startx][starty][0] and pos[1] > positions[startx][starty][1]:
                Down.append(pos)
            elif pos[0] < positions[startx][starty][0] and pos[1] == positions[startx][starty][1]:
                Left.append(pos)
            elif pos[0] > positions[startx][starty][0] and pos[1] == positions[startx][starty][1]:
                Right.append(pos)
            elif pos[0] < positions[startx][starty][0] and pos[1] < positions[startx][starty][1]:
                UpLeft.append(pos)
            elif pos[0] > positions[startx][starty][0] and pos[1] < positions[startx][starty][1]:
                UpRight.append(pos)
            elif pos[0] < positions[startx][starty][0] and pos[1] > positions[startx][starty][1]:
                DownLeft.append(pos)
            elif pos[0] > positions[startx][starty][0] and pos[1] > positions[startx][starty][1]:
                DownRight.append(pos)

        if len(Up) > 0:
            index = calIndexOrder(Up, 'Up')
            Obstruc = Up[index]
            for pos in PossibleMoves:
                if Obstruc[0] == pos[0] and Obstruc[1] > pos[1]:
                    Remove.append(pos)
        if len(Down) > 0:
            index = calIndexOrder(Down, 'Down')
            Obstruc = Down[index]
            for pos in PossibleMoves:
                if Obstruc[0] == pos[0] and Obstruc[1] < pos[1]:
                    Remove.append(pos)
        if len(Left) > 0:
            index = calIndexOrder(Left, 'Left')
            Obstruc = Left[index]
            for pos in PossibleMoves:
                if Obstruc[0] > pos[0] and Obstruc[1] == pos[1]:
                    Remove.append(pos)
        if len(Right) > 0:
            index = calIndexOrder(Right, 'Right')
            Obstruc = Right[index]
            for pos in PossibleMoves:
                if Obstruc[0] < pos[0] and Obstruc[1] == pos[1]:
                    Remove.append(pos)
        if len(UpLeft) > 0:
            index = calIndexOrder(UpLeft, 'Left')
            ObstrucLeft = UpLeft[index]
            index = calIndexOrder(UpLeft, 'Up')
            ObstrucUp = UpLeft[index]
            Obstruc = (ObstrucLeft[0], ObstrucUp[1])
            for pos in PossibleMoves:
                if Obstruc[0] > pos[0] and Obstruc[1] > pos[1]:
                    Remove.append(pos)
        if len(UpRight) > 0:
            index = calIndexOrder(UpRight, 'Right')
            Obstruc = UpRight[index]
            for pos in PossibleMoves:
                if Obstruc[0] < pos[0] and Obstruc[1] > pos[1]:
                    Remove.append(pos)
        if len(DownLeft) > 0:
            index = calIndexOrder(DownLeft, 'Left')
            Obstruc = DownLeft[index]
            for pos in PossibleMoves:
                if Obstruc[0] > pos[0] and Obstruc[1] < pos[1]:
                    Remove.append(pos)
        if len(DownRight) > 0:
            index = calIndexOrder(DownRight, 'Right')
            ObstrucRight = DownRight[index]
            index = calIndexOrder(DownRight, 'Down')
            ObstrucDown = DownRight[index]
            Obstruc = (ObstrucRight[0], ObstrucDown[1])
            for pos in PossibleMoves:
                if Obstruc[0] < pos[0] and Obstruc[1] < pos[1]:
                    Remove.append(pos)

    elif pieceChosen in ['pawn1', 'pawn2', 'pawn3', 'pawn4', 'pawn5', 'pawn6', 'pawn7',
                         'pawn8']:  # Pawn has been chosen.
        # There's no need to code in the above manner because, although it was necessary to find the Up, Right, etc,
        # lists for rook, bishop and Queen, we only need a distinction between black and white to determine
        # what's Up or Down in the case of Pawns.
        if POSIT[1] == 'black':
            CoordOfPawn = positions[startx][starty]
            if len(posTaken) > 0:
                if pawnState == 2:
                    inValid = [(CoordOfPawn[0], CoordOfPawn[1] + 50), (CoordOfPawn[0], CoordOfPawn[1] + 100)]
                    for pos in posTaken:
                        if pos == inValid[1]:
                            Remove.append(pos)
                            break
                        elif pos == inValid[0]:
                            Remove.append(pos)
                            Remove.append(inValid[1])
                            break
                elif pawnState == 1:
                    inValid = (CoordOfPawn[0], CoordOfPawn[1] + 50)
                    for pos in posTaken:
                        if pos == inValid:
                            Remove.append(pos)
                            break

        elif POSIT[1] == 'white':
            CoordOfPawn = positions[startx][starty]
            if len(posTaken) > 0:
                if pawnState == 2:
                    inValid = [(CoordOfPawn[0], CoordOfPawn[1] - 50), (CoordOfPawn[0], CoordOfPawn[1] - 100)]
                    for pos in posTaken:
                        if pos == inValid[1]:
                            Remove.append(pos)
                            break
                        elif pos == inValid[0]:
                            Remove.append(pos)
                            Remove.append(inValid[1])
                            break
                elif pawnState == 1:
                    inValid = (CoordOfPawn[0], CoordOfPawn[1] - 50)
                    for pos in posTaken:
                        if pos == inValid:
                            Remove.append(pos)
                            break

    # The Knight is left out of this function because of the nature of its moves(it doesn't need Move Removal) .
    # The King's moves are dealt with in the check function because of infinite regress in this function.
    for pos in Remove:
        PossibleMoves.remove(pos)
    return PossibleMoves


def removeInValidKingMoves(clicks, PossibleMoves):
    checkForQuit()
    # Function that removes possible but illegal king moves into opposing piece's capturable squares.
    Remove = []
    newRemove = []
    oppSideMoves = []
    PawnCaptures = []
    pieceChosen, POSIT = calculatePieceChosen(clicks, [posb, posw])
    if pieceChosen in 'king':  # King has been chosen.
        if POSIT[1] == 'black':
            # Iterates through the current capture moves of opposing white pieces and sifts through
            # the ones coincedental to black king's possible moves.
            oppSideMoves, PawnCaptures = oppPosiCaptures(posw)
            for i in range(len(oppSideMoves)):
                for j in oppSideMoves[i]:
                    if j in PossibleMoves:
                        Remove.append(j)

            for i in range(len(PawnCaptures)):
                for j in PawnCaptures[i]:
                    if j in PossibleMoves:
                        Remove.append(j)

            # Removes the square of the threatening piece(s) from the 'Remove' list,
            # thereby allowing the king to capture the threatening piece if in range.
            for i in posw:
                if i in Remove:
                    Remove.remove(i)

            # Prohibits any capture move(s) a king can make that lands in a danger square.
            for i in PossibleMoves:
                if i in posw:
                    for j in range(len(oppSideMoves)):
                        if i in oppSideMoves[j]:
                            Remove.append(i)
                    for j in range(len(PawnCaptures)):
                        if i in PawnCaptures[j]:
                            Remove.append(i)

        elif POSIT[1] == 'white':
            # Iterates through the current capture moves of opposing black pieces and sifts through
            # the ones coincedental to white king's possible moves.
            oppSideMoves, PawnCaptures = oppPosiCaptures(posb)
            for i in range(len(oppSideMoves)):
                for j in oppSideMoves[i]:
                    if j in PossibleMoves:
                        Remove.append(j)

            for i in range(len(PawnCaptures)):
                for j in PawnCaptures[i]:
                    if j in PossibleMoves:
                        Remove.append(j)

            # Removes the square of the threatening piece(s) from the 'Remove' list,
            # thereby allowing the king to capture the threatening piece if in range.
            for i in posb:
                if i in Remove:
                    Remove.remove(i)

            # Prohibits any capture move(s) a king can make that lands in a danger square.
            for i in PossibleMoves:
                if i in posb:
                    for j in range(len(oppSideMoves)):
                        if i in oppSideMoves[j]:
                            Remove.append(i)
                    for j in range(len(PawnCaptures)):
                        if i in PawnCaptures[j]:
                            Remove.append(i)

        # Removes duplicate items from the 'Remove' list and puts them in a new list.
        for i in Remove:
            if i not in newRemove:
                newRemove.append(i)

        # Removal of invalid king moves.
        for pos in newRemove:
            PossibleMoves.remove(pos)
    return PossibleMoves


def calculatePosMoves(clicks):
    checkForQuit()
    pawnState = None
    startx, starty = 0, 0
    pieceChosen, POSIT = calculatePieceChosen(clicks, [posb, posw])
    possibleMoves = []
    positions = [[a1, b1, c1, d1, e1, f1, g1, h1],
                 [a2, b2, c2, d2, e2, f2, g2, h2],
                 [a3, b3, c3, d3, e3, f3, g3, h3],
                 [a4, b4, c4, d4, e4, f4, g4, h4],
                 [a5, b5, c5, d5, e5, f5, g5, h5],
                 [a6, b6, c6, d6, e6, f6, g6, h6],
                 [a7, b7, c7, d7, e7, f7, g7, h7],
                 [a8, b8, c8, d8, e8, f8, g8, h8]]

    fClick = clicks[0]
    for x in range(len(positions)):
        for y in range(len(positions[x])):
            if positions[x][y] == fClick:
                startx, starty = x, y
                break

    if pieceChosen in ['rook1', 'rook2']:  # Rook has been chosen.
        for i in range(8):
            possibleMoves.append(positions[startx][i])
            possibleMoves.append(positions[i][starty])

    elif pieceChosen in ['knight1', 'knight2']:  # Knight has been chosen.
        if (startx + 2) <= 7 and (starty + 1) <= 7:
            possibleMoves.append(positions[startx + 2][starty + 1])
        if (startx + 2) <= 7 and (starty - 1) >= 0:
            possibleMoves.append(positions[startx + 2][starty - 1])
        if (startx - 2) >= 0 and (starty + 1) <= 7:
            possibleMoves.append(positions[startx - 2][starty + 1])
        if (startx - 2) >= 0 and (starty - 1) >= 0:
            possibleMoves.append(positions[startx - 2][starty - 1])
        if (startx + 1) <= 7 and (starty + 2) <= 7:
            possibleMoves.append(positions[startx + 1][starty + 2])
        if (startx + 1) <= 7 and (starty - 2) >= 0:
            possibleMoves.append(positions[startx + 1][starty - 2])
        if (startx - 1) >= 0 and (starty + 2) <= 7:
            possibleMoves.append(positions[startx - 1][starty + 2])
        if (startx - 1) >= 0 and (starty - 2) >= 0:
            possibleMoves.append(positions[startx - 1][starty - 2])

    elif pieceChosen in ['bishop1', 'bishop2']:  # Bishop has been chosen.
        for i in range(8):
            if (startx - i) >= 0 and (starty - i) >= 0:
                possibleMoves.append(positions[startx - i][starty - i])
            if (startx - i) >= 0 and (starty + i) <= 7:
                possibleMoves.append(positions[startx - i][starty + i])
            if (startx + i) <= 7 and (starty - i) >= 0:
                possibleMoves.append(positions[startx + i][starty - i])
            if (startx + i) <= 7 and (starty + i) <= 7:
                possibleMoves.append(positions[startx + i][starty + i])

    elif pieceChosen == 'queen':  # Queen has been chosen(This code is just a reimplementation of rook and bishop possibleMoves code).
        for i in range(8):
            possibleMoves.append(positions[startx][i])
            possibleMoves.append(positions[i][starty])
        for i in range(8):
            if (startx - i) >= 0 and (starty - i) >= 0:
                possibleMoves.append(positions[startx - i][starty - i])
            if (startx - i) >= 0 and (starty + i) <= 7:
                possibleMoves.append(positions[startx - i][starty + i])
            if (startx + i) <= 7 and (starty - i) >= 0:
                possibleMoves.append(positions[startx + i][starty - i])
            if (startx + i) <= 7 and (starty + i) <= 7:
                possibleMoves.append(positions[startx + i][starty + i])

    elif pieceChosen == 'king':  # King has been chosen.
        if (startx - 1) >= 0 and (starty - 1) >= 0:
            possibleMoves.append(positions[startx - 1][starty - 1])
        if (startx - 1) >= 0 and (starty + 1) <= 7:
            possibleMoves.append(positions[startx - 1][starty + 1])
        if (startx + 1) <= 7 and (starty - 1) >= 0:
            possibleMoves.append(positions[startx + 1][starty - 1])
        if (startx + 1) <= 7 and (starty + 1) <= 7:
            possibleMoves.append(positions[startx + 1][starty + 1])
        if (starty + 1) <= 7:
            possibleMoves.append(positions[startx][starty + 1])
        if (starty - 1) >= 0:
            possibleMoves.append(positions[startx][starty - 1])
        if (startx + 1) <= 7:
            possibleMoves.append(positions[startx + 1][starty])
        if (startx - 1) >= 0:
            possibleMoves.append(positions[startx - 1][starty])

    elif pieceChosen in ['pawn1', 'pawn2', 'pawn3', 'pawn4', 'pawn5', 'pawn6', 'pawn7',
                         'pawn8']:  # Pawn has been chosen.
        var = []
        if POSIT[1] == 'black':
            if fClick[1] == 150:
                var = [0, 1, 2]
                pawnState = 2
            else:
                var = [0, 1]
                pawnState = 1
            for i in var:
                if startx + i <= 7:
                    possibleMoves.append(positions[startx + i][starty])
        elif POSIT[1] == 'white':
            if fClick[1] == 400:
                var = [0, 1, 2]
                pawnState = 2
            else:
                var = [0, 1]
                pawnState = 1
            for i in var:
                if startx - i >= 0:
                    possibleMoves.append(positions[startx - i][starty])

    # This is an addition of the one diagonal step capture for pawns.
    if pieceChosen in ['pawn1', 'pawn2', 'pawn3', 'pawn4', 'pawn5', 'pawn6', 'pawn7', 'pawn8']:
        if POSIT[1] == 'black':
            CoordOfPawn = positions[startx][starty]
            captures = (CoordOfPawn[0] - 50, CoordOfPawn[1] + 50), (CoordOfPawn[0] + 50, CoordOfPawn[1] + 50)
            if captures[0] in posw and captures[1] in posw:
                possibleMoves.append(captures[0])
                possibleMoves.append(captures[1])
            elif captures[0] in posw:
                possibleMoves.append(captures[0])
            elif captures[1] in posw:
                possibleMoves.append(captures[1])

        elif POSIT[1] == 'white':
            CoordOfPawn = positions[startx][starty]
            captures = (CoordOfPawn[0] - 50, CoordOfPawn[1] - 50), (CoordOfPawn[0] + 50, CoordOfPawn[1] - 50)
            if captures[0] in posb and captures[1] in posb:
                possibleMoves.append(captures[0])
                possibleMoves.append(captures[1])
            elif captures[0] in posb:
                possibleMoves.append(captures[0])
            elif captures[1] in posb:
                possibleMoves.append(captures[1])

    # This is where any plausible but impossible moves are removed from possibleMoves.
    ValidMoves = removeInValidMoves(possibleMoves, clicks, [posb, posw], startx, starty, positions, pawnState)

    # Removes possibleMoves occurring on pieces of the same colour as the selected piece.
    for i in range(len(ValidMoves) - 1, -1, -1):
        if ValidMoves[i] in POSIT[0]:
            del ValidMoves[i]

    return ValidMoves


def afterClick(clicks):
    checkForQuit()
    iValidMoves = calculatePosMoves(clicks)
    ValidMoves = removeInValidKingMoves(clicks, iValidMoves)
    Remove, remIntercept = removeInValidPieceMoves(clicks)
    if clicks[0] in Remove:
        ValidMoves = InterceptPiece(remIntercept, ValidMoves, clicks, Remove)
    ValidMoves.append(clicks[0])
    for i in range(len(ValidMoves)):
        pos = ValidMoves[i]
        if pos != clicks[0]:
            color = BrightBlue
        elif pos == clicks[0]:
            color = Green

        if clicks[0] in posb:
            if pos in posw:
                color = Red
        elif clicks[0] in posw:
            if pos in posb:
                color = Red

        if clicks[0] in posb:
            if pos == posw[4]:
                color = CheckRed
        elif clicks[0] in posw:
            if pos == posb[4]:
                color = CheckRed

        drawHighlight(pos, color)


def makeMove(clicks, windex, bindex, iMoves):
    checkForQuit()
    wcaptured, bcaptured = False, False
    Moves = removeInValidKingMoves(clicks, iMoves)
    Remove, remIntercept = removeInValidPieceMoves(clicks)
    if clicks[0] in Remove:
        Moves = InterceptPiece(remIntercept, Moves, clicks, Remove)
    Moves.append(clicks[0])

    if clicks[1] not in Moves:
        return False

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
        # Iterates for a black capture (white's piece taken).
        elif (clicks[0] in posb and clicks[1] in posw) and not (clicks[0] in posw and clicks[1] in posb):
            if clicks[1] == posw[4]:  # Prevents king capture.
                return False
            for i in range(len(posb)):
                if clicks[0] == posb[i]:
                    for j in range(len(posw)):
                        if clicks[1] == posw[j]:
                            posb[i] = posw[j]
                            posw[j] = wsidelines[windex]
                            wcaptured = True

        # Iterates for a white capture (black's piece taken).
        elif (clicks[0] in posw and clicks[1] in posb) and not (clicks[0] in posb and clicks[1] in posw):
            if clicks[1] == posb[4]:  # Prevents king capture.
                return False
            for i in range(len(posw)):
                if clicks[0] == posw[i]:
                    for j in range(len(posb)):
                        if clicks[1] == posb[j]:
                            posw[i] = posb[j]
                            posb[j] = bsidelines[bindex]
                            bcaptured = True
    return [wcaptured, bcaptured]


def boardLeftTopCoords(X, Y):
    # This function is lengthy, but is the easiet way to see if a square has been clicked and which square it is.
    # Most of it is just copy and paste anyway.
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


def dispBoard():  # Blits imported image to create game board
    DISPLAYSURF.fill(BGCOLOR)
    pygame.draw.rect(DISPLAYSURF, Black, (95, 95, 410, 410), 10)

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
