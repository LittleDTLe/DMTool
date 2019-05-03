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
            # records[row][col] = input("Field: " + str(col+1) + " Entry: " + str(row+1) + " : ")
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


# Radnom Entry from Encounter Table
def randomEnc():
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM encounter")
    lines = my_cursor.fetchall()
    entries = 0
    for line in lines:
        entries += 1
    my_cursor.close()
    ran_entry = random.randint(1, entries)
    my_cursor = mydb.cursor()
    sql = "SELECT * FROM encounter WHERE id = %s"
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
          "3. Encounter")  # Others to be added

# Print Loot Data
def printLoot():
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM loot")
    result = my_cursor.fetchall()
    for row in result:
        print("NAME\tDESCRIPTION\t\tID")
        print(row[0], row[1] + "\t\t", row[2])


# Print Establisment Data
def printEst():
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM establisment")
    result = my_cursor.fetchall()
    for row in result:
        print("NAME\tDESCRIPTION\t\tID")
        print(row[0], row[1] + "\t\t", row[2])


# Print Encounter Data
def printEnc():
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM encounter")
    result = my_cursor.fetchall()
    for row in result:
        print("NAME\tDESCRIPTION\t\tID")
        print(row[0], row[1] + "\t\t", row[2])


# Update Loot Data
def updateLoot(pos, key):
    my_cursor = mydb.cursor()
    if pos.upper() == "NAME":
        sql = "UPDATE loot SET name = %s WHERE id = %s"
        id = (key,)
        name = (input("Enter name: "))
        my_cursor.execute(sql, name, id)
        mydb.commit()
    elif pos.upper() == "DESCRIPTION":
        sql = "UPDATE loot SET description = %s WHERE id = %s"
        id = (key,)
        description = input("Enter description: ")
        my_cursor.execute(sql, description, id)
        mydb.commit()


# Update Establishment Data
def updateEst(pos, key):
    my_cursor = mydb.cursor()
    if pos.upper() == "NAME":
        sql = "UPDATE establishment SET name = %s WHERE id = %s"
        id = (key,)
        name = (input("Enter name: "))
        my_cursor.execute(sql, name, id)
        mydb.commit()
    elif pos.upper() == "DESCRIPTION":
        sql = "UPDATE establishment SET description = %s WHERE id = %s"
        id = (key,)
        description = input("Enter description: ")
        my_cursor.execute(sql, description, id)
        mydb.commit()


# Update Encounter Data
def updateEnc(pos, key):
    my_cursor = mydb.cursor()
    if pos.upper() == "NAME":
        sql = "UPDATE encounter SET name = %s WHERE id = %s"
        id = (key,)
        name = (input("Enter name: "))
        my_cursor.execute(sql, name, id)
        mydb.commit()
    elif pos.upper() == "DESCRIPTION":
        sql = "UPDATE encounter SET description = %s WHERE id = %s"
        id = (key,)
        description = input("Enter description: ")
        my_cursor.execute(sql, description, id)
        mydb.commit()

# Delete Entry from Loot
def deleteLootData(key):
    my_cursor = mydb.cursor()
    sql = "Delete from loot where id = %s"
    id = (key,)
    my_cursor.execute(sql, id)
    mydb.commit()

# Delete Entry from Establishment
def deleteEstData(key):
    my_cursor = mydb.cursor()
    sql = "Delete from establishment where id = %s"
    id = (key,)
    my_cursor.execute(sql, id)
    mydb.commit()

# Delete Entry from Loot
def deleteEncData(key):
    my_cursor = mydb.cursor()
    sql = "Delete from encounter where id = %s"
    id = (key,)
    my_cursor.execute(sql, id)
    mydb.commit()

# Modification Options
def modOption():
    print("1. Modify\n"
          "2. Delete")

# Program
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
        # After choosing a table, a random entry of the table will show
        showTables()
        table_choice = input("Select Table: ")
        if table_choice.upper() == "LOOT":
            randomLoot()
            os.system('cls')
        elif table_choice.upper() == "ESTABLISHMENT":
            randomEst()
            os.system('cls')
        elif table_choice.upper() == "ENCOUNTER":
            randomEnc()
            os.system('cls')
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
            elif mod_choice == 3:
                modOption()
                mod_option = int(input())
                if mod_option == 1:
                    printLoot()
                    key = int(input("Enter id: "))
                    pos = input("Enter field: ")
                    updateLoot(pos, key)
                elif mod_option == 2:
                    printLoot()
                    key = int(input("Enter id: "))
                    deleteLootData(key)
        elif pop_choice.upper() == "ESTABLISHMENT":
            if mod_choice == 1:
                popEst()
                os.system('cls')
            elif mod_choice == 2:
                dropEst()
                os.system('cls')
            elif mod_choice == 3:
                modOption()
                mod_option = int(input())
                if mod_option == 1:
                    printEst()
                    key = int(input("Enter id: "))
                    pos = input("Enter field: ")
                    updateEst(pos, key)
                elif mod_option == 2:
                    printEst()
                    key = int(input("Enter id: "))
                    deleteEstData(key)
        elif pop_choice.upper() == "ENCOUNTER":
            if mod_choice == 1:
                popEnc()
                os.system('cls')
            elif mod_choice == 2:
                dropEnc()
                os.system('cls')
            elif mod_choice == 3:
                modOption()
                mod_option = int(input())
                if mod_option == 1:
                    printEnc()
                    key = int(input("Enter id: "))
                    pos = input("Enter field: ")
                    updateEnc(pos, key)
                elif mod_option == 2:
                    printEnc()
                    key = int(input("Enter id: "))
                    deleteEncData(key)
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
    # EXIT PROGRAM
    elif choice == 5:
        print("EXITING PROGRAM...")
        exit()
