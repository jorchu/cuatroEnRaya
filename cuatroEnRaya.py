import pygame as py
import random as rn
import sys

py.init()

inMenu = True
runing = False
endMenssage = False
ia = False
local = False

def createMap(f, c):
    map = []
    for i in range(f):
        map.append([])
        for j in range(c):
            map[i].append(2)

    return map

filas = 10
columnas = 16

map = createMap(filas, columnas)

tableroSize = 800, 400
size = tableroSize[0], tableroSize[1]+40


space =  tableroSize[0] // columnas, tableroSize[1] // filas
screen = py.display.set_mode(size)
font = py.font.SysFont('Arial', 30)


propBPlay = (tableroSize[0]//2-75, 10, 150, 80, (0,0,0))
propBLocal = (propBPlay[0], propBPlay[1]+100, 150, 80, (0,0,0))
propBExit = (propBPlay[0], propBLocal[1]+100, 150, 80, (0,0,0))

propBReanude = (propBPlay[0], 10, 160, 80, (0,0,0))
propBMainMenu = (tableroSize[0]//2-85, propBReanude[1]+100, 190, 80, (0,0,0))

mensWinProp = (300, tableroSize[1]//2-60, 240, 70, (0,0,0))
mensEmpateProp = (350, tableroSize[1]//2-60, 150, 70, (0,0,0))

replayProp = (350, mensWinProp[1]+100, 150, 70, (0,0,0))

player1Prop = (5, tableroSize[1]+10, (70, 70, 255), 'PLAYER_1', tableroSize[0]//2-20, tableroSize[1]+10)
player2Prop = (tableroSize[0]-120, tableroSize[1]+10, (255, 70, 70), 'PLAYER_2', tableroSize[0]//2+20, tableroSize[1]+10)




def replay():
    global endMenssage, runing, map
    map = createMap(filas, columnas)
    table.ficha = 0

    runing = True
    endMenssage = False
    play()

def menssageWin(menss):
    global endMenssage, inMenu

    while endMenssage:
        pos = py.mouse.get_pos()
        if menss == 'EMPATE':
            mensEmpate.draw(pos, menss, 1)
        else:
            mensWin.draw(pos, menss, 1)
        buttReplay.draw(pos, 'REPLAY')

        for e in py.event.get():
            if e.type == py.QUIT:
                sys.exit()
            if e.type == py.MOUSEBUTTONDOWN:
                buttReplay.click(pos, replay)

            if e.type == py.KEYDOWN:
                if e.key == py.K_ESCAPE:
                    inMenu = True
                    endMenssage = False
                    mainMenu() 


        py.display.update()


class player:
    def __init__(self, prop):
        self.xName = prop[0]
        self.yName = prop [1]
        self.color = prop[2]
        self.name = prop[3]
        self.xMark = prop[4]
        self.yMark = prop[5]
        self.sizeFont = 22
        self.mark = 0

    def drawName(self):
        playerFont = py.font.SysFont('Arial', self.sizeFont)
        text = playerFont.render(self.name, 1, self.color)
        screen.blit(text, (self.xName, self.yName))

    def drawMark(self):
        markFont = py.font.SysFont('Arial', self.sizeFont)
        text = markFont.render(str(self.mark),1 , self.color)
        screen.blit(text,(self.xMark, self.yMark))



class tablero:
    def __init__(self):
        self.long = 90
        self.ficha = 0

    def tableroDraw(self):
        for i in range(1, columnas):
            py.draw.line(screen, (0,0,0), (space[0]*i, 0), (space[0]*i, tableroSize[1]))

        for i in range(1, filas+1):
            py.draw.line(screen, (0,0,0), (0, space[1]*i), (tableroSize[0], space[1]*i))


    def drawO(self, f, c, col):
        py.draw.circle(screen, col, (space[0]*f+space[0]//2, space[1]*c+space[1]//2), space[1] // 2-2)
        py.draw.circle(screen, (255,255,255), (space[0]*f+space[0]//2, space[1]*c+space[1]//2), space[1] // 2-6)

    def tap(self, pos):
        map[pos[1]][pos[0]] = self.ficha #Posiblemente haya que cambiarlo
        if self.ficha == 0:
            self.ficha = 1
        else:
            self.ficha = 0 
    
    def empity(self, pos):
        empity = True
        if map[pos[1]][pos[0]] != 2:
            empity = False
        return empity
    
    def win(self):
        global runing, endMenssage

        empate = True

        def matchFila(f, c, ficha):
            global runing, endMenssage
            if map[f][c:c+4] == [ficha,ficha,ficha,ficha]:
                runing = False
                endMenssage = True
                if ficha == 1:
                    player2.mark += 1
                    menssageWin('PLAYER_2 WIN')
                else:
                    player1.mark += 1
                    menssageWin('PLAYER_1 WIN')
    
        def matchColumna(f, c, ficha):
            global runing, endMenssage
            if map[f][c] == ficha and map[f+1][c] == ficha and map[f+2][c] == ficha and map[f+3][c] == ficha: # <--- Revisar
                runing = False
                endMenssage = True
                if ficha == 0:
                    player1.mark += 1
                    menssageWin('PLAYER_1 WIN')
                else:
                    player2.mark += 1
                    menssageWin('PLAYER_2 WIN')

        def matchDiagonal(f, c, ficha):
            global runing, endMenssage
            if map[f][c] == ficha and map[f+1][c+1] == ficha and map[f+2][c+2] == ficha and map[f+3][c+3] == ficha:
                runing = False
                endMenssage = True
                if ficha == 0:
                    player1.mark += 1
                    menssageWin('PLAYER_1 WIN')
                else:
                    player2.mark += 1
                    menssageWin('PLAYER_2 WIN')

            elif map[f+3][c] == ficha and map[f+2][c+1] == ficha and map[f+1][c+2] == ficha and map[f][c+3] == ficha:
                runing = False
                endMenssage = True
                if ficha == 0:
                    player1.mark += 1
                    menssageWin('PLAYER_1 WIN')
                else:
                    player2.mark += 1
                    menssageWin('PLAYER_2 WIN')


        for i in range(filas):
            for j in range(columnas):

                if i < filas-3:
                    matchColumna(i, j, 0)
                    matchColumna(i, j, 1)

                if i < filas-3 and j < columnas - 3:
                    matchDiagonal(i, j, 0)
                    matchDiagonal(i, j, 1)

                if j < columnas - 3:
                    matchFila(i, j, 0)
                    matchFila(i, j, 1)

                if 2 in map[i]:
                    empate = False

        if empate:
            runing = False
            endMenssage = True
            menssageWin('EMPATE')

def playLocal():
    global inMenu, runing, local
    local = True
    inMenu = False
    runing = True
    replay()

class button:
    def __init__(self, propieties):
        self.width = propieties[2] 
        self.height = propieties[3]
        self.x = propieties[0]
        self.y = propieties[1]
        self.color = propieties[4]
        self.size = (self.x, self.y, self.width, self.height)
        
    def draw(self, pos, text, do =0):
        if not(pos[0] in range(self.x, self.x + self.width) and pos[1] in range(self.y, self.y +self. height)):
            py.draw.rect(screen, self.color, self.size)
            text_button = font.render(text, 0, (255,255,255))
            screen.blit(text_button, (self.x+10, self.y+30))
        elif do:
            py.draw.rect(screen, self.color, self.size)
            text_button = font.render(text, 0, (255,255,255))
            screen.blit(text_button, (self.x+10, self.y+30))
        else:
            py.draw.rect(screen, (50,50,50), self.size)
            text_button = font.render(text, 0, (255,255,255))
            screen.blit(text_button, (self.x+10, self.y+30))

    def click(self, pos, func=''):
        if pos[0] in range(self.x, self.x + self.width) and pos[1] in range(self.y, self.y +self. height):
            if func:
                func()


buttPlay = button(propBPlay)
buttLocal = button(propBLocal)
buttExit = button(propBExit)
buttReanude = button(propBReanude)
buttMainMenu = button(propBMainMenu)
buttReplay = button(replayProp)

mensWin = button(mensWinProp)
mensEmpate = button(mensEmpateProp)

player1 = player(player1Prop)
player2 = player(player2Prop)

table = tablero()

def playIA():
    global runing, inMenu, ia
    ia = True
    runing = True
    inMenu = False
    replay()

def mainMenu(gameMenu=False):
    global inMenu, ia, local
    local = False
    ia = False

    screen.fill((255,255,255))
    py.display.set_caption('TRES EN RAYA')
    while inMenu:
        pos = py.mouse.get_pos()
        if gameMenu:
            buttReanude.draw(pos, "REANUDE")
            buttMainMenu.draw(pos, "MAIN MENU")
            buttExit.draw(pos, "EXIT")

        else:
            player1.mark = 0
            player2.mark = 0
            buttPlay.draw(pos, "PLAY")
            buttLocal.draw(pos, "LOCAL")
            buttExit.draw(pos, "EXIT")

        for e in py.event.get():
            if e.type == py.QUIT:
                sys.exit()
            if e.type == py.MOUSEBUTTONDOWN:
                if gameMenu:
                    buttPlay.click(pos, playLocal)
                    buttLocal.click(pos, mainMenu)
                    buttExit.click(pos, sys.exit)
                else:
                    buttPlay.click(pos, playIA)
                    buttLocal.click(pos, playLocal)
                    buttExit.click(pos, sys.exit)

            if e.type == py.KEYDOWN:
                if e.type == py.K_ESCAPE:
                    inMenu = False
                    sys.exit()

        py.display.update()



def play():
    global runing, inMenu, ia, local

    while runing: #Empieza con False
        screen.fill((255,255,255))

        posPlayer = [py.mouse.get_pos()[0] // space[0], py.mouse.get_pos()[1] // space[1]]

        table.tableroDraw()
        player1.drawName()
        player2.drawName()
        player1.drawMark()
        player2.drawMark()

        if table.ficha == 0:
            player2.color = (255, 70, 70)
            player1.color = (0,0,255)
        else:
            player1.color = (70, 70, 255)
            player2.color = (255, 0, 0)

        for e in py.event.get():
            if e.type == py.QUIT:
                sys.exit()
            ##MODO

            if e.type == py.MOUSEBUTTONDOWN:
                if posPlayer[1] < filas and local:
                    if table.empity(posPlayer):
                        table.tap(posPlayer)
                elif posPlayer[1] < filas and table.ficha == 0:
                    if table.empity(posPlayer):
                        table.tap(posPlayer)
  

            if e.type == py.KEYDOWN:
                if e.key == py.K_ESCAPE:
                    inMenu = True
                    runing = False
                    mainMenu(1)


        if ia and table.ficha == 1:
            pos = [rn.randint(0, columnas-1), rn.randint(0, filas-1)]
            print(799 // space[0], 399 // space[1])
            while map[pos[1]][pos[0]] != 2:
                print("ENRTRO")
    
                if pos[1] == filas-1 and pos[0] == len(map[0])-1:
                    pos[0] = 0
                    pos[1] = 0
                elif pos[0] == columnas-1:
                    pos[0] = 0
                    pos[1] += 1
                else:
                    pos[0] += 1
                print(pos)

            else:
                print(pos)
                table.tap(pos)
                

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 0:
                    table.drawO(j, i, (50,50,255))
                elif map[i][j] == 1:
                    table.drawO(j, i, (255,50,50))
        table.win()
        py.display.update()



mainMenu()
