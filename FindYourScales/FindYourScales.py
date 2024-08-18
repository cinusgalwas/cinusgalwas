# Find Your Today's Exercising Scale

import random

tryby = ["D", "M"]
dur = ["C-dur", "F-dur", "G-dur", "B-dur", "D-dur", "Es-dur", "A-dur", "As-dur",
       "E-dur", "Des-dur", "H-dur", "Ges-dur", "Fis-dur", "Ces-dur", "Cis-dur"]
moll = ["a-moll", "d-moll", "e-moll", "g-moll", "h-moll", "c-moll", "fis-moll",
        "f-moll", "cis-moll", "b-moll", "gis-moll", "es-moll", "dis-moll", "as-moll", "ais-moll"]
skladowe_dur = ["Ćwierćnuty", "Ósemki", "Tercje", "Rozłożona", "Kwarty", "Kwinty", "Trójdźwięk",
                "Trójdźwięk rozłożony", "D7", "D7 rozłożona", "Pentatonika", "Pentatonika rozłożona"]
skladowe_moll = ["Eolska ćwierćnuty", "Eolska ósemki", "Melodyczna ćwierćnuty", "Melodyczna ósemki",
                 "Harmoniczna Ćwierćnuty", "Harmoniczna Ósemki", "Harmoniczna Tercje", "Harmoniczna Kwarty",
                 "Harmoniczna Kwinty", "Harmoniczna Rozłożona", "trójdźwięk",
                 "trójdźwięk rozłożony", "D7", "D7 rozłożona", "Pentatonika", "Pentatonika rozłożona"]


def los_dur(x):
    gama = random.choice(dur[:2*x+1])
    return gama


def los_moll(x):
    gama = random.choice(moll[:2*x+1])
    return gama


# printer pozwala nam na druk wszystkich elementów do wyćwiczenia z rodzaju gamy (ale lista jest trochę niepełna)
def printer(result):
    print("Jeśli potrzebujesz znać zakres co możesz przegrać sobie ze znalezionej skali, to wpisz P. Jeśli nie, to N.")
    p = input("Wydrukuję Ci to! ")
    if p == "P":
        if result in moll:
            for x in skladowe_moll:
                print(x)
        elif result in dur:
            for x in skladowe_dur:
                print(x)
    elif p == "N":
        return
    else:
        print("Litera nieprawidłowa, spróbuj jeszcze raz!")
        printer(result)


def losowanie_gamy(x=7):
    gama = " "
    tryb = random.choice(tryby)
    if tryb == "D":
        gama = los_dur(x)
    elif tryb == "M":
        gama = los_moll(x)
    return gama


def wybor_trybu(x):
    check = input("Jeśli chcesz gamy durowe, wpisz D, jeśli mollowe, wpisz M: ")
    if check == "D":
        scale = los_dur(x)
    elif check == "M":
        scale = los_moll(x)
    else:
        print("Wpisany znak jest nieprawidłowy, spróbuj ponownie.")
        scale = wybor_trybu(x)
    return scale


def wybor_gamy(x=7):
    check = input("Jeśli chcesz wybrać tryb gamy wpisz T, jeśli nie wpisz N: ")
    if check == "T":
        gama = wybor_trybu(x)
    elif check == "N":
        gama = losowanie_gamy(x)
    else:
        print("Wpisany znak jest nieprawidłowy, spróbuj ponownie.")
        gama = wybor_gamy(x)
    return gama


def malo_znakow():
    i = input("Podaj maksymalną liczbę znaków przykluczowych (od 0 do 7): ")
    if i.isdigit() and -1 < int(i) < 8:
        result = wybor_gamy(int(i))
    else:
        print("Proszę podać cyfrę w zakresie od 0 do 7 !")
        result = malo_znakow()
    return result


def turbopowtorka():
    num = input("Napisz liczbę ile chcesz elementów gam powtórzyć? Minimum to 3, maksimum 20")
    if num.isdigit() and 2 < int(num) < 21:
        print("Poćwicz następujące elementy: ")
        num = int(num)
        i = 0
        while i < num:
            scale = losowanie_gamy()
            if scale in moll:
                ffff = random.choice(skladowe_moll)
                print(ffff, "z gamy", scale)
            elif scale in dur:
                ffff = random.choice(skladowe_dur)
                print(ffff, "z gamy", scale)
            i += 1
    else:
        turbopowtorka()
    return 0


def starting_function():
    i = input("W celu losowania skali z pełnej puli wpisz 1; w celu ograniczenia maksymalnej liczby znaków wybierz 2: ")
    if i == "1":
        result = wybor_gamy()
        print("Gama znaleziona na dzisiaj to ", result, "!")
        printer(result)
    elif i == "2":
        result = malo_znakow()
        print("Gama znaleziona na dzisiaj to ", result, "!")
        printer(result)
    elif i == "9":
        print("You are crazy!")
        print("Z założenia tutaj wybierasz tylko liczbę elementów, które chcesz poćwiczyć.")
        result = turbopowtorka()
    else:
        print("Podany znak jest nieprawidłowy! Spróbój jeszcze raz!")
        result = starting_function()
    return result


print("Dzień dobry, to jest program, który pomoże Ci wylosować skalę do ćwiczenia.")
print("Jest kilka trybów działania.")
print("Jeśli twierdzisz, że wszystko umiesz, to polecamy tryb turbopowtórki. W najbliższej możliwości wpisz 9.")
surprise = starting_function()
print("Miłego i owocnego ćwiczenia!")
