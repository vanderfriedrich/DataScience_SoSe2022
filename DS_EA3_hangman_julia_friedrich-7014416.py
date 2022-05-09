#hangman data science sommersemester 2022 julia friedrich
#todo für weiterentwicklung bereits geratene buchstaben notieren
#import einer datei mit vielen ratewörtern

import random

def my_willkommen():
    print("Willkommen zum Wörterraten")
    print("Es gibt maximal 8 Rateversuche")

def my_raten():
    erraten = False
    raten = []
    ratezaehler = 8
    limit = 1
    woerter = ["taube", "topf", "tetris", "maus", "herd"]
    ratewort = (random.choice(woerter))    
    
    while not erraten:
        for buchstabe in ratewort:
            if buchstabe.lower() in raten:                        
                print(buchstabe, end=" ")
            else:
                print("_", end=" ")              
        print("")
    
        print("Es bleiben noch", ratezaehler, "Rateversuche")  
        ratebuchstabe = input("Bitte Buchstabe eingeben: ")
        raten.append(ratebuchstabe.lower())
        if ratebuchstabe.lower() not in ratewort:
            ratezaehler -= 1
            if ratezaehler < limit:
                print("Zu viele falsche Versuche. Spiel wird beendet")
                break

        erraten = True

        for ratebuchstabe in ratewort:
            if ratebuchstabe.lower() not in raten:
                erraten = False
    if erraten:
        print("Das Wort: ",ratewort, "wurde erraten. Spiel gewonnen!")

def my_hangman():
    my_willkommen()
    my_raten()

my_hangman()