import mysql.connector
#import sys

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Panosfaganas1",
    database="dm_database"
)

#my_cursor.execute("CREATE DATABASE dm_database")

#CREATE LOOT TABLE
def createLootTable():
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE TABLE loot (name VARCHAR(30), description MEDIUMTEXT, "
                      "id INTEGER(3) AUTO_INCREMENT PRIMARY KEY)")
    print("LOOT TABLE CREATED")

#CREATE ESTABLISHMENT TABLE
def createEstTable():
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE TABLE establishment (name VARCHAR(30), description MEDIUMTEXT, "
                      "id INTEGER(3) AUTO_INCREMENT PRIMARY KEY)")
    print("ESTABLISHMENT TABLE CREATED")

#Show the available Tables
def showTables():
    my_cursor = mydb.cursor()
    my_cursor.execute("SHOW TABLES")
    for table in my_cursor:
        print(table[0])

#Populate Loot Table
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

#Populate Establishment Table
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

print("1. SHOW TABLES\n"
      "2. CHOOSE TABLE\n"
      "3. MODIFY TABLE\n"
      "4. CREATE TABLE\n")
choice = int(input("Enter input: "))


if choice == 1:
    showTables()
elif choice == 2:
    showTables()
    pop_choice = input("Select Table: ")
    if pop_choice.upper() == "LOOT":
        popLoot()
    else:
        popEst()
    #After choosing a table, a random entry of the table will show
elif choice == 3:
    showTables()
    table_choice = input("Select Table: ")
    popLoot()
    #After choosing a table, you can choose to Update, Drop or Generally modify the Table
elif choice == 4:
    #Choice of what type of table you want to create
    #Loot, Encounter, Establishment etc
    table_choice = input("Enter type of table: ")
    if table_choice.upper() == "LOOT":
        createLootTable()
    elif table_choice.upper() == "ESTABLISHMENT":
        createEstTable()