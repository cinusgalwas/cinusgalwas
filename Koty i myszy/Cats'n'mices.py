import math
import matplotlib.pyplot as plt
import random
import Animals

#  kreujemy koty
lista_kotow = Animals.creation('Kot.txt', Animals.Cat)
# kreacja Kociki
lista_kocikow = Animals.creation('Kotek.txt', Animals.Catty)
# kreacja koty lenie
lista_lenkotow = Animals.creation('Kot_leniuch.txt', Animals.Lazycat)
# kreujemy myszy
lista_myszy = Animals.creation('Mysz.txt', Animals.Mouse)
# garden definition and day length
iterationnumber = 400
garden_end_x = 100
garden_end_y = 100
# day happenes
moment = 0
while moment < iterationnumber:
    # przemieszczamy zwierzęta
    for myszka in lista_myszy:
        myszka.move(garden_end_x, garden_end_y)
    for kotek in lista_kotow:
        kotek.move(garden_end_x, garden_end_y)
    for kocik in lista_kocikow:
        kocik.move(garden_end_x, garden_end_y)
    for kot in lista_lenkotow:
        kot.move(garden_end_x, garden_end_y)
    # sprawdzamy kolizje znaczące
    for myszka in lista_myszy:
        for kotek in lista_kotow:
            if Animals.distance(myszka.x, myszka.y, kotek.x, kotek.y) < 4:
                myszka.ucieczka()
        for kocik in lista_kocikow:
            if Animals.distance(myszka.x, myszka.y, kocik.x, kocik.y) < 4:
                if Animals.distance(kocik.x, kocik.y, kocik.basex, kocik.basey) < 50:
                    myszka.ucieczka()
                else:
                    kocik.ucieczka()
        for kot in lista_lenkotow:
            w4w = 1/(1 + math.pow(math.exp(1), -kot.n/10))
            if random.choices([True, False], [w4w, 1 - w4w]):
                myszka.ucieczka()
                kot.n += 1
    moment += 1
# here we plot where our animals walked during the day
for zwierz in lista_myszy:
    plt.plot(zwierz.xlist, zwierz.ylist, label="mysz", marker='o', c="red")
for zwierz in lista_kotow:
    plt.plot(zwierz.xlist, zwierz.ylist, label="kot", marker='o', c="blue")
for zwierz in lista_kocikow:
    plt.plot(zwierz.xlist, zwierz.ylist, label="kotek", marker='o', c="pink")
for zwierz in lista_lenkotow:
    plt.plot(zwierz.xlist, zwierz.ylist, label="leniwy_kot", marker='o', c="purple")
plt.xlabel("x")
plt.ylabel("y")
