import random

def Winner(towerx,towery,officerx,officery):
    winner = None

    #if the tower wins

    for i in range(8):
        if towerx == officerx and i == officery:
            winner = "P"
            break
        elif winner!= None and i ==officerx and towery == officery:
            winner ="P"
            break


#if the officer wins
mult=1
while officerx+mult<=7 and winner==None:
    try:
        if officery+mult == towery and officerx+mult == towerx:
             winner = "C"
             break
    finally:
     try:
             if pofficery-mult == towery and pfficerx+mult == towerx:
                 winner = "C"
                 break
     finally:
              mult+=1
    mult=1
    while officerx-mult>=0 and winner==None:
        try:
            if officery+mult == towery and officerx-mult == towerx:
                 winner = "C"
                 break
        finally:
             try:
                if officery-mult == towery and officerx-mult == towerx:
                    winner = "C"
                    break
             finally:
                 mult+=1

            return winner

#how many times dose every one wins
tower = 0
officer = 0

for i in range(100):
    #tower locations
    towerx = random.randint(0,7)
    towery = random.randint(0,7)

    #do not have their own locations
    winner = Winner(towerx,towery,officerx,officery)
    if winner == "P":
         tower += 1
    elif winner == "C":
         officer += 1

#the resultv
print("elias won :",tower," times")
print("bashar won :",officer," times")
