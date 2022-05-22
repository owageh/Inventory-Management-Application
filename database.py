

import sqlite3
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS data_table")
query = """ CREATE TABLE "data_table" (
            "id" INTEGER NOT NULL,
            "item_name" VARCHAR(30) NOT NULL,
            "track_num" VARCHAR(20) NOT NULL,
            "quantity" INTEGER(5),
            "warehouse" VARCHAR(20) NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
		); """
cursor.execute(query)
print("ITEM Table is Ready")

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO data_table(
   ITEM_NAME, TRACK_NUM, QUANTITY, WAREHOUSE) VALUES 
   ('Shoe', 'A123', 20, 'Mississauga')''')
cursor.execute('''INSERT INTO data_table(
   ITEM_NAME, TRACK_NUM, QUANTITY, WAREHOUSE) VALUES 
   ('Car', 'C102', 30, 'Toronto')''')
cursor.execute('''INSERT INTO data_table(
   ITEM_NAME, TRACK_NUM, QUANTITY, WAREHOUSE) VALUES 
   ('Table', 'T1201', 10, 'Ottawa')''')


# Commit your changes in the database
conn.commit()
print("ITEM TABLE Records inserted........")

# Table Warehouse
cursor.execute("DROP TABLE IF EXISTS WAREHOUSE")
query = """ CREATE TABLE "warehouse" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(20) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
		); """
cursor.execute(query)
print("Warehouse Table is Ready")

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO Warehouse(NAME) VALUES ('Mississauga')''')
cursor.execute('''INSERT INTO Warehouse(NAME) VALUES ('Toronto')''')
cursor.execute('''INSERT INTO Warehouse(NAME) VALUES ('Ottawa')''')
conn.commit()
print("Warehouse Records inserted........")

# Closing the connection
conn.close()