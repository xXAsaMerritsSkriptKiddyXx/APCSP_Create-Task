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
        cardcompare()
    elif firstdraw in yesresponse:
        playercard = random.randint(1,13)
        botcard = random.randint(1,13)
        cardcompare()
    else:
        print("Try again.")
        carddrawsequence()

def cardcompare():
    global playercard, playerhasfacecard, playercheck, botcard, bothasfacecard, botcheck, playerchips, botchips, playersetbet, botpot, playerfacecard, botfacecard
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
             print(f"Loser! you have: a {playerfacecard.name}! Your enemy has a {botfacecard.name}")
             botchips = botchips + playersetbet
             playerchips = playerchips + botpot
             playagain()
         elif botcard == playercard:
             print(f"uhhhh. you both got {playerfacecard.name} and {botfacecard.name}")
             playagain()
         else:
             print(f"Winner! you have: a {playerfacecard.name}! Your enemy has a {botfacecard.name}")
             playerchips = playerchips + botpot
             botchip = botchips - botpot
             playagain()
     elif bothasfacecard and not playerhasfacecard:
         if botcard > playercard:
             print(f"Loser you have: a {playercard}! Your enemy has a {botfacecard.name}")
             botchips = botchips + playersetbet
             playerchips = playerchips + botpot
             playagain()
         else:
             print(f"Winner! you have: a {playercard}! Your enemy has an {botfacecard.name}")
             playerchips = playerchips + botpot
             botchip = botchips - botpot
             playagain()
     elif playerhasfacecard and not bothasfacecard:
        if playercard > botcard:
         print(f"Winner! you have: a {playerfacecard.name}! Your enemy has a {botcard}")
         playerchips = playerchips + botpot
         botchip = botchips - botpot
         playagain()
        else:
         print(f"Loser! you have: an {playerfacecard.name}! Your enemy has a {botcard}")
         botchips = botchips + playersetbet
         playerchips = playerchips + botpot
         playagain()
     else:
        if playercard > botcard:
            print(f"You win! You pulled a {playercard} and your enemy pulled a {botcard}")
            playerchips = playerchips + botpot
            botchip = botchips - botpot
            playagain()
        elif botcard < playercard:
            print(f"You lose! You pulled a {playercard} and your enemy pulled a {botcard}")
            botchips = botchips + playersetbet
            playerchips = playerchips + botpot
            playagain()
        else:
            print(f"uhhhh. you both got a {playercard} and a {botcard}")
            playagain()
    

def playagain():
    time.sleep(1)
    playerfacecard = []
    botfacecard = []
    restartrequest = input("Would you like to play again? \n Y/N:")
    if restartrequest in yesresponse:
        start(firsttime = False)
    if restartrequest in noresponse:
        selfdestruct(True, 3)

returnfacecards()
start(firsttime = True) 
