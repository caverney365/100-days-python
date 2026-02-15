print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your misson is to find the treasure.")
print("==========================================================================")

print("You're at a crossroad. Where do you want to go?")
player_choice = input('Type "left" or "right": ').lower()

if player_choice == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    player_choice = input('Type "wait" to wait for a boat, or type "swim" to swim accross: ').lower()
    if player_choice == "wait":
        print("You arrived at the island unharmed. There is a house with 3 doors: red, yellow, and blue.")
        player_choice = input("Which colour do you choose? ").lower()
        if player_choice == "yellow":
            print("You Win?")
        elif player_choice == "red":
            print("You're burned by fire and dead. Game Over!")
        elif player_choice == "blue":
            print("You're eaten by beasts. Game Over!")
        else:
            print("Game Over!")
    else:
        print("You're attacked by a trout. Game Over!")
else:
    print("You fell into a hole. Game Over!")