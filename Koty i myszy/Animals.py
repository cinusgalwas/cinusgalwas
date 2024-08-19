import random
import math


def distance(ax, ay, bx, by):
    p = [ax, ay]
    q = [bx, by]
    return math.dist(p, q)


def stringtoint(wer):
    derty = []
    q = 0
    while q < len(wer):
        derty.append(int(wer[q]))
        q += 1
    return derty


def creation(plik_wejsciowy, aanimal):
    cre = open(plik_wejsciowy, 'r')
    lista = []
    for line in cre:
        for word in line.split():
            lista.append(word)
    cre.close()
    i = 0
    lista_zwierzat = []
    lista = stringtoint(lista)
    while i < len(lista) - 1:
        lista_zwierzat.append(aanimal(lista[i], lista[i + 1]))
        i += 2
    return lista_zwierzat


class Animal:
    def __init__(self, basex, basey):  # współrzędne bazowe zwierząt i zmienne zapisu lokalizacji
        self.basex = basex
        self.basey = basey
        self.x = x = basex
        self.y = y = basey
        self.xlist = xlist = []
        self.ylist = ylist = []


class Mouse(Animal):
    def move(self, xmax, ymax):
        deltha_x = random.choice([-1, 0, 1])
        deltha_y = random.choice([-1, 0, 1])
        if self.x + deltha_x - 1 < xmax and self.x + deltha_x > -1:
            self.x += deltha_x
        else:
            pass
        if self.y + deltha_y - -1 < ymax and self.y + deltha_y > -1:
            self.y += deltha_y
        else:
            pass
        self.xlist.append(self.x)
        self.ylist.append(self.y)

    def ucieczka(self):
        self.x = self.basex
        self.y = self.basex
        self.xlist.append(self.x)
        self.ylist.append(self.y)


class Cat(Animal):
    def move(self, xmax, ymax):
        deltha_x = random.randint(-10, 10)
        deltha_y = random.randint(-10, 10)
        if self.x + deltha_x - 1 < xmax and self.x + deltha_x > -1:
            self.x += deltha_x
        if self.y + deltha_y - 1 < ymax and self.y + deltha_y > -1:
            self.y += deltha_y
        self.xlist.append(self.x)
        self.ylist.append(self.y)


class Lazycat(Cat):
    def __init__(self, basex, basey):  # współrzędne bazowe zwierząt i zmienne zapisu lokalizacji
        super().__init__(basex, basey)
        # n to ilość przegonień myszy
        self.n = 0


class Catty(Cat):
    def move(self, xmax, ymax):
        deltha_x = random.randint(-5, 5)
        deltha_y = random.randint(-5, 5)
        workdistance = distance(self.x + deltha_x, self.y + deltha_y, self.basex, self.basey)
        if self.x + deltha_x - 1 < xmax and self.x + deltha_x > -1 and workdistance < 100:
            self.x += deltha_x
        if self.y + deltha_y - 1 < ymax and self.y + deltha_y > -1 and workdistance < 100:
            self.y += deltha_y
        self.xlist.append(self.x)
        self.ylist.append(self.y)

    def ucieczka(self):
        self.x = self.basex
        self.y = self.basex
        self.xlist.append(self.x)
        self.ylist.append(self.y)
