
# Title: Module 8.2 MySQL test
# Author: Keegan Jones
# Date: 2/8/2021
# Description: MySQL test Python

# Import Statements
import mysql.connector
from mysql.connector import errorcode

# Database Config Object
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True 
}


try:
    # Try/Catch Block for Handling Potential MySQL Database Errors  
    
    db = mysql.connector.connect(**config) #Connect to the pysports Database
    
    #output the connection status
    print("\n Database user {} connected to MySqL on host {} with database{}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    # on error code
    
    if err.errno == errorcod.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)
    
finally:
    # Close the connection to MySQL
    
    db.close()