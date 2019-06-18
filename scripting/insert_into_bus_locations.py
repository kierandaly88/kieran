# This script connects to the dublinbus mySQL database and inserts the contents of busLocationsNoHeader.csv into the bus_locations table

import csv
import mysql.connector

cnx = mysql.connector.connect(user='root', password='*******',
                              host='localhost',
                              database='dublinbus')

cursor = cnx.cursor()

with open('busLocationsNoHeader.csv') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')

  

    for row in csv_data:


        cursor.execute('INSERT INTO bus_locations(stopid, displaystopid, shortname,  latitude, longitude) \
            VALUES(%s, %s, %s, %s, %s)', 
              row)
    
    cnx.commit()
    cursor.close()
print ("Done")