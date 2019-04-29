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

while True:
    print("To exit type [EXIT]")
    setting = input("Enter chances of roll[e.x: For, Against, Neutral]: ")
    if setting.upper() == "EXIT":
        exit()
    else:
        user = input("Enter what you want to roll[e.x: 2d8]: ")
        if setting.upper() == "FOR":
            favor(user)
        elif setting.upper() == "AGAINST":
            against(user)
        elif setting.upper() == "NEUTRAL":
            check(user)
        else:
            print("NOT VALID CHANCE TYPE!")