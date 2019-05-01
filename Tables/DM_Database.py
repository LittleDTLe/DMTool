import mysql.connector
import os
import random

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Panosfaganas1",
    database="dm_database"
)

# my_cursor.execute("CREATE DATABASE dm_database")

# CREATE LOOT TABLE
def createLootTable():
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE TABLE loot (name VARCHAR(30), description MEDIUMTEXT, "
                      "id INTEGER(3) AUTO_INCREMENT PRIMARY KEY)")
    print("LOOT TABLE CREATED")

# CREATE ESTABLISHMENT TABLE
def createEstTable():
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE TABLE establishment (name VARCHAR(30), description MEDIUMTEXT, "
                      "id INTEGER(3) AUTO_INCREMENT PRIMARY KEY)")
    print("ESTABLISHMENT TABLE CREATED")

# CREATE ENCOUNTER TABLE
def createEncTable():
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE TABLE encounter (name VARCHAR(30), description MEDIUMTEXT, "
                      "id INTEGER(3) AUTO_INCREMENT PRIMARY KEY)")
    print("ENCOUNTER TABLE CREATED")

# Show the available Tables
def showTables():
    my_cursor = mydb.cursor()
    my_cursor.execute("SHOW TABLES")
    for table in my_cursor:
        print(table[0])

# Populate Loot Table
def popLoot():
    my_cursor = mydb.cursor()
    sql = "INSERT INTO loot (name, description) VALUES (%s, %s)"
    entries = int(input("Enter number of entries: "))
    records = []
    for row in range(entries):
        records.append([])
    for row in range(entries):
        for col in range(2):
            records[row].append(col)
            records[row][col] = 0
    for row in range(entries):
            for col in range(2):
                #records[row][col] = input("Field: " + str(col+1) + " Entry: " + str(row+1) + " : ")
                if col == 0:
                    records[row][col] = input("Enter name: ")
                else:
                    records[row][col] = input("Enter description: ")
    my_cursor.executemany(sql, records)
    mydb.commit()

# Populate Establishment Table
def popEst():
    my_cursor = mydb.cursor()
    sql = "INSERT INTO establishment (name, description) VALUES (%s, %s)"
    entries = int(input("Enter number of entries: "))
    records = []
    for row in range(entries):
        records.append([])
    for row in range(entries):
        for col in range(2):
            records[row].append(col)
            records[row][col] = 0
    for row in range(entries):
        for col in range(2):
            if col == 0:
                records[row][col] = input("Enter name: ")
            else:
                records[row][col] = input("Enter description: ")
    my_cursor.executemany(sql, records)
    mydb.commit()

# Populate Encounter Table
def popEnc():
    my_cursor = mydb.cursor()
    sql = "INSERT INTO encounter (name, description) VALUES (%s, %s)"
    entries = int(input("Enter number of entries: "))
    records = []
    for row in range(entries):
        records.append([])
    for row in range(entries):
        for col in range(2):
            records[row].append(col)
            records[row][col] = 0
    for row in range(entries):
        for col in range(2):
            if col == 0:
                records[row][col] = input("Enter name: ")
            else:
                records[row][col] = input("Enter description: ")
    my_cursor.executemany(sql, records)
    mydb.commit()

# Random Entry from Loot Table
def randomLoot():
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM loot")
    lines = my_cursor.fetchall()
    entries = 0
    for line in lines:
        entries += 1
    my_cursor.close()
    ran_entry = random.randint(1, entries)
    my_cursor = mydb.cursor()
    sql = "SELECT * FROM loot WHERE id = %s"
    id = (ran_entry,)
    my_cursor.execute(sql, id)
    entry = my_cursor.fetchone()
    print("Name: " + entry[0] + "\nDescription: " + entry[1])

# Random Entry from Establishment Table
def randomEst():
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM establishment")
    lines = my_cursor.fetchall()
    entries = 0
    for line in lines:
        entries += 1
    my_cursor.close()
    ran_entry = random.randint(1, entries)
    my_cursor = mydb.cursor()
    sql = "SELECT * FROM establishment WHERE id = %s"
    id = (ran_entry,)
    my_cursor.execute(sql, id)
    entry = my_cursor.fetchone()
    print("Name: " + entry[0] + "\nDescription: " + entry[1])

# DROP Loot
def dropLoot():
    my_cursor = mydb.cursor()
    my_cursor.execute("DROP TABLE IF EXISTS loot")
    print("Loot Table DROPPED...")

# DROP Establishment
def dropEst():
    my_cursor = mydb.cursor()
    my_cursor.execute("DROP TABLE IF EXISTS establishment")
    print("Establisment Table DROPPED...")

# DROP Encounter
def dropEnc():
    my_cursor = mydb.cursor()
    my_cursor.execute("DROP TABLE IF EXISTS encounter")
    print("Encounter Table DROPPED...")

# Modify Tables Content
def modTables():
    print("1. Populate\n"
          "2. Drop\n"
          "3. Modify Entries")

# Types of Tables to be Created
def tables():
    print("1. Loot\n"
          "2. Establishment\n"
          "3. Encounter")# Others to be added

while True:
    print("1. SHOW TABLES\n"
          "2. CHOOSE TABLE\n"
          "3. MODIFY TABLE\n"
          "4. CREATE TABLE\n"
          "5. EXIT")
    choice = int(input("Enter input: "))
    # Show Tables
    if choice == 1:
        showTables()
    # Random Table Value
    elif choice == 2:
        showTables()
        table_choice = input("Select Table: ")
        if table_choice.upper() == "LOOT":
            randomLoot()
            os.system('cls')
        else:
            randomEst()
            os.system('cls')
        # After choosing a table, a random entry of the table will show
    # Modify Table
    elif choice == 3:
        showTables()
        pop_choice = input("Select Table: ")
        os.system('cls')
        modTables()
        mod_choice = int(input())
        if pop_choice.upper() == "LOOT":
            if mod_choice == 1:
                popLoot()
                os.system('cls')
            elif mod_choice == 2:
                dropLoot()
                os.system('cls')
            # elif mod_choice == 3:
                # Modify Entries
        elif pop_choice.upper() == "ESTABLISHMENT":
            if mod_choice == 1:
                popEst()
                os.system('cls')
            elif mod_choice == 2:
                dropEst()
                os.system('cls')
            # elif mod_choice == 3:
                # Modify Entries
        elif pop_choice.upper() == "ENCOUNTER":
            if mod_choice == 1:
                popEnc()
                os.system('cls')
            elif mod_choice == 2:
                dropEnc()
                os.system('cls')
            # elif mod_choice == 3:
                # Modify Entries
        # After choosing a table, you can choose to Update, Drop or Generally modify the Table
    # Create Table
    elif choice == 4:
        # Choice of what type of table you want to create
        # Loot, Encounter, Establishment etc
        tables()
        table_choice = int(input("Enter type of table: "))
        if table_choice == 1:
            createLootTable()
            os.system('cls')
        elif table_choice == 2:
            createEstTable()
            os.system('cls')
        elif table_choice == 3:
            createEncTable()
            os.system('cls')
    #EXIT PROGRAM
    elif choice == 5:
        print("EXITING PROGRAM...")
        exit()