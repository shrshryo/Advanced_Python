# Importing library
import sqlite3
"""The purpose of this program is in order create a database for Taltech diner information. There are two tables CANTEEN and PROVIDER.
CANTEEN consists information of ID, provider ID, name, location, time opening, and time closing. ID is the primary key and Provider ID 
holds integer values which is a foreign key referencing to PROVIDER table. PROVIDER table consists of ID and provider name. ID is the 
primary key. Diner in IT college is inserted into CANTEEN table using a separate statement from diners in the main building."""

# Creation of database connection
con = sqlite3.connect('DINERS.db')
# Creation of a cursor object
cur = con.cursor()
# Creation of table CANTEEN and PROVIDER
cur.execute('''CREATE TABLE CANTEEN (ID INTEGER PRIMARY KEY, ProviderID INTEGER, Name text, Location text, time_open time, time_closed time, foreign key (ProviderID) references PROVIDER (ID))''')
cur.execute('''CREATE TABLE PROVIDER (ID INTEGER PRIMARY KEY, ProviderName text)''')
# Insertin of data into table PROVIDER
cur.execute("INSERT INTO PROVIDER (ProviderName) VALUES ('Rahva Toit'), ('Baltic Restaurants \nEstonia AS'), ('TTÜ Sport OÜ'), ('bitStop Kohvik OÜ')")
# Insertin of data into table CANTEEN
cur.execute("INSERT INTO CANTEEN (ProviderID,Name,Location,time_open,time_closed) VALUES ('1', 'Economics- and social science \nbuilding canteen', 'Akadeemia tee 3 SOC- building', '08:30', '18:30'), ('1', 'Library canteen', 'Akadeemia tee 1/Ehitajate tee 7', '08:30', '19:00'), ('2', 'Main building Deli cafe', 'Ehitajate tee 5 U01 building', '9:00', '16:30'), ('2', 'Main building Daily lunch restaurant', 'Ehitajate tee 5 U01 building', '09:00', '16:30'), ('1', 'U06 building canteen', '', '09:00', '16:00'), ('2', 'Natural Science building canteen', 'Akadeemia tee 15 SCI building', '09:00', '16:00'), ('2', 'ICT building canteen', 'Raja 15/Mäepealse 1', '09:00', '16:00'), ('3', 'Sports building canteen', 'Männiliiva 7 S01 building', '11:00', '20:00')")
# Insertion for IT College canteen data by separate statement
cur.execute("INSERT INTO CANTEEN (ProviderID,Name,Location,time_open,time_closed) VALUES ('4', 'bitStop KOHVIK', 'IT College, Raja 4c', '9:30', '16:00')")
# Query for printing out canteens that are open between 16:15 and 18:00
print("\nCreate query for canteens which are open 16.15-18.00")
for row in cur.execute("SELECT Name,Location,time_open,time_closed FROM CANTEEN WHERE time_open <= '16:15' AND time_closed >= '18:00'"):
    print(row)
# Query for printing out canteens that are serviced by Rahva Toit
print("\nCreate query for canteens which are serviced by Rahva Toit. NB! Create query by string \"Rahva Toit\" not by direct ID!.")
for row in cur.execute("SELECT Name,Location,time_open,time_closed FROM CANTEEN INNER JOIN PROVIDER ON CANTEEN.ProviderID=PROVIDER.ID WHERE ProviderName = 'Rahva Toit'"):
    print(row)
# Commits the current transaction
con.commit()
# Cursor connection close
cur.close()
# Database connection close
con.close()
