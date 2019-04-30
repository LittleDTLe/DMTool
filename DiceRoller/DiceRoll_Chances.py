import random

def rollDice(quant, type):
    total_roll = 0
    for roll in range(quant):
        total_roll += (random.randrange(type) + 1)
    print("You rolled: " + str(total_roll))

def check(user):
    sep = user.lower().index('d')
    try:
        quant = int(user[0:sep])
        type = int(user[sep+1:])
        if type in (4, 6, 8, 10, 12, 20, 100):
            rollDice(quant, type)
        else:
            print("Not valid dice type!")
    except:
        print("Invalid Input!")

def against(user):
    chance = random.random()
    chance = random.random()
    if chance < 0.85:
        sep = user.lower().index('d')
        try:
            quant = int(user[0:sep])
            type = int(user[sep + 1:])
            if type in (4, 6, 8, 10, 12, 20, 100):
                # Roll
                total_roll = 0
                for roll in range(quant):
                    total_roll += (random.randrange(type) + 1)
                if total_roll >= ((quant * type) / 3) * 2:
                    total_roll -= (type / 2)
                print("You rolled: " + str(int(total_roll)))
            else:
                print("Not valid dice type!")
        except:
            print("Invalid Input!")
    else:
        check(user)

def favor(user):
    chance = random.random()
    if chance > 0.25:
        #High Roll
        sep = user.lower().index('d')
        try:
            quant = int(user[0:sep])
            type = int(user[sep + 1:])
            if type in (4, 6, 8, 10, 12, 20, 100):
                #Roll
                total_roll = 0
                for roll in range(quant):
                    total_roll += (random.randrange(type) + 1)
                if total_roll < ((quant*type)/3) * 2:
                    total_roll += (type / 2)
                print("You rolled: " + str(int(total_roll)))
            else:
                print("Not valid dice type!")
        except:
            print("Invalid Input!")
    else:
        check(user)

def intro():
    print("1. Dice-Roller\n"
          "2. Settings\n"
          "3. Exit")

def settings_menu():
    print("1.FAVORABLE\n"
          "2. AGAINST\n"
          "3.NEUTRAL\n"
          "4. BACK")

def roll_chances(roll_type):
    file = open("rolltype.txt", "wt")
    file.write(roll_type)
    file.close()

while True:
    intro()
    option = input()
    if option == "1":
        file = open("rolltype.txt", "r")
        user = input("Enter what you want to roll[e.x: 2d8]: ")
        read = file.readline()
        if read == "1":
            print("Favor")
            favor(user)
        elif read == "2":
            print("AGAINST")
            against(user)
        elif read == "3": #or file.readline() == None:
            print("NEUTRAL")
            check(user)
        file.close()
    elif option == "2":
        settings_menu()
        roll_type = input()
        if roll_type != "4":
            roll_chances(roll_type)
    elif option == "3":
        print("EXITING PROGRAM...")
        exit()
