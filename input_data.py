import sqlite3

# Connect to the database (or create it if it doesn't exist)
dbase = sqlite3.connect('Our_data.db')
print('Database opened')

# Drop the existing table if it exists (optional)
dbase.execute('''DROP TABLE IF EXISTS employee_records''')
print('Existing table dropped')

# Create a new table with the correct schema
dbase.execute('''CREATE TABLE employee_records(
       ID INT PRIMARY KEY NOT NULL,
       NAME TEXT NOT NULL,
       DIVISION TEXT NOT NULL,
       STARS INT NOT NULL)''')
print('Table created')

# Get user input
id_input = int(input("Enter ID: "))
name_input = input("Enter Name: ")
division_input = input("Enter Division: ")
stars_input = int(input("Enter Stars: "))

# Insert the user's data into the database
dbase.execute('''INSERT INTO employee_records(ID, NAME, DIVISION, STARS) 
                 VALUES(?, ?, ?, ?)''', (id_input, name_input, division_input, stars_input))

dbase.commit()

dbase.close()
print('Database closed')
