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
Globberhealth = 10
Globberdamage = 1
playerhealth = 30
enemiesleft = 3
while enemiesleft > 0:
     print ("You've come against a " + enemiesname + "!") 
     enemiesleft = enemiesleft - 1  
print ("Good Job!")
