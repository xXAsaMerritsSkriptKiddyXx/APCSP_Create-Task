import random, sys, time, os

class Facecard():
    def __init__(self,
    name = "Ace",
    value = 1
    ):
        self.name = name
        self.value = value
# Jack= 11, King = 12 , Queen = 13 , Ace = 1

ace = Facecard("Ace", 1)
jack = Facecard("Jack", 11)
king = Facecard("King", 12)
queen = Facecard("Queen", 13)


options = {
    "Ace" : ace,
    "King" : king,
    "Jack" : jack,
    "Queen" : queen
}

facecardoptions = []
facecardoptions.append(ace)
facecardoptions.append(jack)
facecardoptions.append(king)
facecardoptions.append(queen)

def returnfacecards():
 for i, facecard in enumerate(facecardoptions):
     return(i+1, facecard.name)

playercard = random.randint(1,13)
botcard = random.randint(1,13)

playerfacecard = ()
botfacecard = ()

checking = False

botcheck = False
playercheck = False

bothasfacecard = False
playerhasfacecard = False

bothasace = False
playerhasace = False
checking = False


def test():
    global playercard, playerhasfacecard, playercheck, botcard, bothasfacecard, botcheck
    playercheck = True

    while playercheck:
        if playercard == 1:
         playerfacecard = facecardoptions[0]
         playerhasfacecard = True
         botcheck = True
         playercheck = False
        elif playercard > 10:
         playerfacecard = facecardoptions[int(playercard) - 10]
         playerhasfacecard = True
         botcheck = True
         playercheck = False
        else:
         botcheck = True
         playercheck = False

    while botcheck:
        if botcard == 1:
         botfacecard = facecardoptions[0]
         bothasfacecard = True
         botcheck = False
        elif botcard > 10:
         botfacecard = facecardoptions[int(botcard) - 10]
         bothasfacecard = True
         botcheck = False
        else:
         botcheck = False

    while not botcheck and not playercheck:
     if bothasfacecard and playerhasfacecard:
         if botcard > playercard:
             print(f"Loser! you have: {playerfacecard.name}! Your enemy has {botfacecard.name}")
             break
         elif botcard == playercard:
             print(f"uhhhh. you both got {playerfacecard.name} and {botfacecard.name}")
             break
         else:
             print(f"Winner! you have: {playerfacecard.name}! Your enemy has {botfacecard.name}")
             break
     elif bothasfacecard and not playerhasfacecard:
         if botcard > playercard:
             print(f"Loser you have: {playercard}! Your enemy has {botfacecard.name}")
             break
         else:
             print(f"Winner! you have: {playercard}! Your enemy has {botfacecard.name}")
             break
     elif playerhasfacecard and not bothasfacecard:
        if playercard > botcard:
         print(f"Winner! you have: {playerfacecard.name}! Your enemy has {botcard}")
         break
        else:
         print(f"Loser! you have: {playerfacecard.name}! Your enemy has {botcard}")
         break
     else:
        if playercard > botcard:
            print(f"You win! You pulled a {playercard} and your enemy pulled a {botcard}")
            break
        elif botcard < playercard:
            print(f"You lose! You pulled a {playercard} and your enemy pulled a {botcard}")
            break
        else:
            print(f"uhhhh. you both got {playercard} and {botcard}")
            break
    
test()