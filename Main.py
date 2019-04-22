import random
guysName = "Daniel"
print("hello? Have we been lost in space?")
print("Anybody? This is " + guysName)
print("What is your name?")
yourName = input().title()
print("Hello, " + yourName+"!")
enterMessage = "Press Enter to continue..."
input(enterMessage)
print("We need you," +  yourName+", I need you to help me get out of space!")
input(enterMessage)
weapons = ["lightsaber", "taser"]
choice = int(input("Pick a weapon (0 = Lightsaber 1 = taser "))
import time
input(enterMessage)
weapon = weapons[choice]
input ("F = attack E = special attack")
attack = 0
speed = 0
if weapon == "lightsaber":
    attack = 3
    speed = 5
if weapon == "taser":
    attack = 5
    speed = 1
print ("Your weapon does " + str(attack) + " damage")
print ("Your weapon also goes " + str(speed) + " miles per second")
input (enterMessage)
print ("Three...")
time.sleep(1)
print ("Two...")
time.sleep(1)
print ("One")
time.sleep(1)
print ("Go!")
time.sleep(1)
enemiesname = "Globber"
Globberdamage = 1
playerhealth = 30
enemiesleft = 3
while enemiesleft > 0:    
    print ("You've come against a " + enemiesname + "!") 
    Globberhealth = 10
    while Globberhealth > 0 and playerhealth > 0:
        waitTime = random.randint(1,3)
        time.sleep(waitTime)
        startTime = int(round(time.time() * 1000))
        attackletter = input("type attack letter: ")
        endTime = int(round(time.time() * 1000))
        elapsedTime = endTime - startTime
        if elapsedTime > 1000:
            playerhealth = playerhealth - Globberdamage
            print ("Ouch!")
            continue
        if attackletter == "E":
            Globberhealth = Globberhealth - 8
            print ("Globber: Oof.") 
        if attackletter == "F":
            Globberhealth = Globberhealth - attack
            print ("Globber: Oof.") 
        print("Globber heath" + str(Globberhealth))
    if playerhealth < 0:
        print ("*Dead*")
        exit()        
    enemiesleft = enemiesleft - 1  
print ("Good Job!")
print ("Btw go ahead of here and commit baklava idiot")