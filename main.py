import sys, random, time

firsttime = True
nuclearbombswitch = False
nuclearbombcountdown = 5
firstdraw = "None"

bothasace = False
playerhasace = False
checking = False

playerhasfacecard = False
playerfacecardname = "None"
bothasfacecard = False
botfacecardname = "None"

playercard = 0
botcard = 0

botpot = 0
playersetbet = 0

playerchips = 100
botchips = 100

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
    "King" : king,
    "Jack" : jack,
    "Queen" : queen,
    "Ace" : ace
}

facecardoptions = []
facecardoptions.append(ace)
facecardoptions.append(jack)
facecardoptions.append(king)
facecardoptions.append(queen)

def returnfacecards():
 for i, facecard in enumerate(facecardoptions):
     return(i+1, facecard.name)

playerfacecard = []
botfacecard = []

yesresponse = ["y","yes"]
noresponse = ["n","no"]

timer = [1, 2, 3]

def selfdestruct(nuclearbombswitch, nuclearbombcountdown):
    global timer
    begforyourlife = input("THE GAME IS ABOUT TO EXPLODE!!! \ndo you want to save your progress?")
    if begforyourlife != "Yes, please.":
     if nuclearbombswitch:
         print("Self destructing in..\n")
         time.sleep(1)
         for i in reversed(timer): 
              print(i, "...\n" )
              time.sleep(1)
              i += 1
              nuclearbombcountdown -= 1
         if nuclearbombcountdown == 0: 
             sys.exit()
    else:
        print("Rebooting...")
        time.sleep(3)
        start(True)


#politeness is manditory.

def start(firsttime):
    if firsttime:
        print("\nWelcome to a very cruddy game where you compare cards and see whose is higher.\nAnd you use imaginary chips, because you are boring, have no life, and are playing a crappy game made by someone who doesn't know how to code.")
        if input("\nWould you like to continue?: \n Y/N:").lower().strip() in yesresponse:
            firsttime = False
            playerplacebets(botchips, playerchips)
        else:
            print("Then why are you here?")
            time.sleep(1)
            selfdestruct(True,3)
    else:
     if input("Are you sure you want to play again? \n").lower().strip() in yesresponse:   
         playerplacebets(botchips, playerchips)
     else:
        print("Then get out!!!")
        selfdestruct(True, 3)

def playerplacebets(botchips, playerchips):
    global playersetbet
    print(f"You have {playerchips} chips!")
    time.sleep(1)
    if playerchips > 0:
     playersetbet = input("How much would you like to bet?\nPlease input an integer between and including 1 and the ammount of chips you currently hold!:")
     try:
         playersetbet = int(playersetbet)
     except ValueError:
         print("Please only input a valid integer!\n")
         time.sleep(1)
         playersetbets(botchips, playerchips)
     if playersetbet <= playerchips and playersetbet > 0:
         print(f"You have placed {playersetbet} chips in the pot!")
         time.sleep(1)
         playerchips = playerchips - playersetbet
         botsetbet(botchips)
     else:
         print("Try again doofus.")
         playerplacebets(botchips,playerchips)
    else:
        print("You're out of chips! \n GET OUT!!!")
        selfdestruct(True,3)  

def botsetbet(botchips):
    global botpot
    if botchips > 0:
        botpot = random.randint(0,botchips)
        botchips = botchips - botpot
        print(f"Your opponent has bet {botpot} chips!")
        time.sleep(1)
        carddrawsequence()
    else:
        replacement_linger = 3
        print("...")
        time.sleep(1)
        print("Your opponent has been excecuted, and will be replaced with another shortly. ")
        time.sleep(3)
        while replacement_linger > 0:
            print(".")
            time.sleep(1)
            replacement_linger = replacement_linger - 1
        botchips = 100

def carddrawsequence():
    global playercard, botcard, firstdraw
    firstdraw = input("Would you like to draw first? \n Y/N:").strip().lower()
    if firstdraw in noresponse:
        botcard = random.randint(1,13)
        playercard = random.randint(1,13)
        facecardcheck()
    if firstdraw in yesresponse:
        playercard = random.randint(1,13)
        botcard = random.randint(1,13)
        facecardcheck()

def acecheck():
    global botcard, playercard, playerhasace, bothasace
    botcard = botcard - 10
    playercard = playercard - 10
    if botcard == -9 or playercard == -9:
        if botcard == -9:
         bothasace = True
        else:
         playerhasace = True
         facecardcheck()

def facecardcheck():
    global botcard, playercard, playerfacecard, botfacecard, playerhasace, bothasace, checking
    checking = True
    bothasfacecard = False
    playerhasfacecard = False
    while checking == True:
        if bothasace or playerhasace:

            if bothasace:
                botfacecard = facecardoptions[0]
                bothasfacecard = True
            if playerhasace:
                playerfacecard = facecardoptions[0]
                playerhasfacecard = True   

        if playerhasace == False:
         if playercard <= len(facecardoptions):
              playerfacecard = facecardoptions[int(playercard)]
              playerhasfacecard = True
        elif bothasace == False:
              if botcard <= len(facecardoptions):
                 botfacecard = facecardoptions[int(botcard)] 
                 bothasfacecard = True
                 checking = False
                 break

    if checking == False:
        pulledcardstatements()


def pulledcardstatements():
    time.sleep(1)
    if bothasfacecard == True and playerhasfacecard == True:
        print(f"Your opponent has pulled a {botfacecardname}, you have a {playerfacecardname}.")
        cardcomparison()
    if bothasfacecard == True:
        print(f"Your opponent has a {botfacecardname}, you have a {playercard}!")
        cardcomparison()
    if playerhasfacecard == True:
        print(f"Your opponent has a {botcard}, you have a {playerfacecardname}")  
        cardcomparison()
    else:
        print(f"Your opponent has a {botcard}, you have a {playercard}")
        cardcomparison()

def cardcomparison():
 global botchips, botcard, playercard, playersetbet, botpot, botchips, playerchips
 time.sleep(1)
 if playercard == botcard:
     print("You have tied!")
     playagain()
 if playercard > botcard:
     print("Your card is higher! You Win!!!")
     playerchips = playerchips + botpot
     botchips = botchips - botpot
     playagain()
 if playercard < botcard:
     print("Your card is lower! You Lose!!!")
     botchips = botchips + playersetbet
     playerchips = playerchips - playersetbet
     playagain()

def playagain():
    time.sleep(1)
    restartrequest = input("Would you like to play again? \n Y/N:")
    if restartrequest in yesresponse:
        start(firsttime = False)
    if restartrequest in noresponse:
        selfdestruct(True, 3)

returnfacecards()
start(firsttime = True) 