# This program is a calculator for the game Ligretto by Schmidt.

import random


def isnumber(s):
    if isinstance(s, int):
        return True
    try:
        int(s)
        return True
    except ValueError:
        return False


def results_printer(mydictionary):
    for u, v in mydictionary.items():
        print(u, v)


def round_drawer():
    r_num_str = input("How many rounds do you want (up to 100)? If you don't know, please write D to draw it. ")
    if r_num_str == "D":
        return random.randint(3, 40)
    elif r_num_str.isdigit() and 0 < int(r_num_str) < 101:
        return int(r_num_str)
    else:
        print("Try again. You've written wrong letter or wrong number.")
        return round_drawer()


def player_creator(player_num, dictionary):
    message = "Enter the name of player number {} : "
    person = input(message.format(player_num))
    if person.isspace() or len(person) == 0 or (person in dictionary.keys()):
        print("Wrong name format. Try again!")
        return player_creator(player_num, dictionary)
    else:
        return person


def pla_num():
    pl_num_str = input("What is the number of players? (between 2 and 12) ")
    if pl_num_str.isdigit() and 1 < int(pl_num_str) < 13:
        return int(pl_num_str)
    else:
        print("Wrong number or wrong format. Try again!")
        return pla_num()


def result_input(xxx, mydictionary):
    message1 = "Enter the result of player {} : "
    ms = input(message1.format(xxx))
    if ms == "P":
        results_printer(mydictionary)
        return result_input(xxx, mydictionary)
    elif isnumber(ms) and -21 < int(ms) < 41:
        return int(ms)
    else:
        print("Format incorrect or wrong number of points, try again.")
        return result_input(xxx, mydictionary)


print("Hi, it is LigrettoStop calculator.")
print("I am here to support your game by counting your results.")
print("Have a good game!")
print("If you write P letter during result's counting, I'll print results for you. <3")
print("Do you want to see results after each round? ")
d = input("If you want, please write letter T or t. If you don't want, please write anything else.")
if d == "T" or d == "t":
    q = True
else:
    q = False
players_number = pla_num()
i = 1
# dictionary
players = {}
while i < players_number + 1:
    player = player_creator(i, players)
    players[player] = 0
    i += 1
# now we start checking how many rounds we want
nmbr_of_rounds = round_drawer()
i = 0
while i < nmbr_of_rounds:
    print("Round ", i+1, ", please enter all results. ")
    for x in players.keys():
        players[x] = players[x] + result_input(x, players)
    if q and i < nmbr_of_rounds - 1:
        results_printer(players)
    i += 1
print("Final results: ")
results_printer(players)
maximum = max(players.values())
w = ""
for r in players:
    if players[r] == maximum:
        w = r
message3 = "The winner is {}  who has scored {} points."
print(message3.format(w, maximum))
