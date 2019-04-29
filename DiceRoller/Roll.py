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

while True:
    print("To exit type [EXIT]")
    user = input("Enter what you want to roll[e.x: 2d8]: ")
    if user.upper() == "EXIT":
        exit()
    else:
        check(user)