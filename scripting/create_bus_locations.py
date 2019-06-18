# This script connects to the dublinbus mySQL database and creates a bus_locations table

import csv
import mysql.connector

cnx = mysql.connector.connect(user='root', password='*******',
                              host='localhost',
                              database='dublinbus')

cursor = cnx.cursor()
cursor.execute("""
 
CREATE TABLE IF NOT EXISTS bus_locations (

stopid INT, 
displaystopid INT,
shortname VARCHAR(255), 
latitude FLOAT, 
longitude FLOAT, 
PRIMARY KEY (stopid)
)  ENGINE=INNODB;

""")


cnx.close()

