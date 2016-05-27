__author__ = 'Pindzia'
from Queue import Queue


def getnumber(tile):
        if(tile=='b' or tile =='c'or tile =='h' or tile =='i' or tile=='j' ):
            number = 0
        else:
            number = 1
        return number

def sasiad_drzwi(Mapa, Wymiar_X, Wymiar_Y, koord):
    wierzch_nt=[]
    wierzcholki = []
    for x in range(Wymiar_X):
        for y in range(Wymiar_Y):
            if getnumber(Mapa[y][x]) != 0:
                wierzcholki.append((x, y))
            else:
                wierzch_nt.append((x, y))
    kierunki = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    info_wierzch = []
    for kierunek in kierunki:
        sasiad = (koord[0]+kierunek[0], koord[1]+kierunek[1])
        if sasiad not in wierzch_nt and sasiad in wierzcholki:
            info_wierzch.append(sasiad)
    return info_wierzch

def sasiedzi(wierzcholek):
    kierunki = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    info_wierzch = []
    for kierunek in kierunki:
        sasiad = (wierzcholek[0]+kierunek[0], wierzcholek[1]+kierunek[1])
        if sasiad not in wierzch_nt:
            info_wierzch.append(sasiad)
    return info_wierzch

def pathfind(Mapa, Wymiar_X, Wymiar_Y , zmienna_x, zmienna_y, poz_x, poz_y):


    global wierzch_nt
    wierzch_nt=[]
    wierzcholki = []
    for x in range(Wymiar_X):
        for y in range(Wymiar_Y):
            if getnumber(Mapa[y][x]) != 0:
                wierzcholki.append((x, y))
            else:
                wierzch_nt.append((x, y))

    punkt_startowy = (poz_x, poz_y)
    kolejka = Queue()
    kolejka.put(punkt_startowy)
    poprzednik = {}
    poprzednik[punkt_startowy] = 0
    cel = (zmienna_x, zmienna_y)


    while not kolejka.empty():
        obecny = kolejka.get()
        if obecny == cel:
            break
        for wierzch_sas in sasiedzi(obecny):
            if wierzch_sas not in poprzednik:
                kolejka.put(wierzch_sas)
                poprzednik[wierzch_sas] = obecny

    if obecny == cel:
        path = []
        path.append(obecny)
        while obecny != punkt_startowy:
            obecny = poprzednik[obecny]
            path.append(obecny)

        return path
    else:
        path = [-1]
        return path