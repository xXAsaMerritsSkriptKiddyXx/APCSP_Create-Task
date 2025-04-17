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

playercard = 1
botcard = 1

playerfacecard = []
botfacecard = []

checking = False

bothasfacecard = False
playerhasfacecard = False

# playerfacecard = []
# if playercard == 1:
#      playerfacecard.append(ace)

bothasace = False
playerhasace = False
checking = False

def acecheck():
    global botcard, playercard, playerhasace, bothasace, checking
    botcard = botcard - 10
    playercard = playercard - 10
    if botcard == -9 or playercard == -9:
        if botcard == -9:
         bothasace = True
        else:
         playerhasace = True
         checking = True
         facecardassign()
    elif playercard >= 0 or botcard >= 0:
        if playercard >= 0:
         playerhasfacecard = True
         checking = True
         facecardassign()
        else: 
         bothasfacecard = True
         checking = True
         facecardassign()
    elif playercard >- 0  and botcard >= 0:
        playerhasfacecard = True
        bothasfacecard = True
        checking = True
        facecardassign()

def facecardassign():
    global botcard, playercard, playerfacecard, botfacecard, playerhasace, bothasace, checking, bothasfacecard, playerhasfacecard
    while checking == True:
        if bothasace or playerhasace:

            if bothasace:
                botfacecard = facecardoptions[0]
                print(f"Your opponent has an {botfacecard.name}")
                bothasfacecard = True
            else:
                playerfacecard = facecardoptions[0]
                print(f"You have an {playerfacecard.name} ")
                playerhasfacecard = True   

        elif playerhasfacecard or bothasfacecard:
         if playercard <= len(facecardoptions):
             playerfacecard = facecardoptions[int(playercard)]
             playerhasfacecard = True
         if botcard <= len(facecardoptions):
             botfacecard = facecardoptions[int(botcard)] 
             bothasfacecard = True
        else:
            bothasfacecard = False
            playerhasfacecard = False
            playerhasace = False
            bothasace = False
            checking = False


def facecardcomparison():
 global botcard, playercard, playerfacecard, botfacecard, playerhasace, bothasace, checking, bothasfacecard, playerhasfacecard
 if botcard > 0:
     bothasfacecard = True
 if playercard > 0:
     playerhasfacecard = True
     if playerhasfacecard and bothasfacecard:
        print(f"Your opponent has pulled a {botfacecard.name}, you have a {playerfacecard.name}.")
        cardcomparison()
     elif bothasfacecard == True:
         print(f"Your opponent has a {botfacecard.name}, you have a {playercard}!")
         cardcomparison()
     elif playerhasfacecard == True:
         print(f"Your opponent has a {botcard}, you have a {playerfacecard.name}")  
         cardcomparison()
 else:
     nofacecardcomarison()


def nofacecardcomarison():
 global botcard, playercard, playerfacecard, botfacecard, playerhasace, bothasace, checking, bothasfacecard, playerhasfacecard
 if playerhasfacecard == False and bothasfacecard == False:
     playercard = playercard + 10
     botcard = botcard + 10
     print(f"Your opponent has a {botcard}, you have a {playercard}")
     cardcomparison()


def cardcomparison():
 global botcard, playercard
 time.sleep(1)
 if playercard == botcard:
     print("You have tied!")
 if playercard > botcard:
     print("Your card is higher! You Win!!!")
 if playercard < botcard:
     print("Your card is lower! You Lose!!!")

# botfacecard = []
# if botcard == 11:
#      botfacecard.append(jack)

returnfacecards()
acecheck()