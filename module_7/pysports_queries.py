
# Title: pysports_queries.py
# Author: Keegan Jones
# Date: 2/14/2021
#  Description: Test Program for Executing Queries Against the pysports Database

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
    # try/catch block for handling potential MySQL database errors 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

    # Select Query from Team Table
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # Get the results from cursor object
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")
    
    # Loop to iterate over the teams data set and display the results 
    for team in teams: 
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # Select Query for the Player Table 
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # Results from the Cursor Object 
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    # Loop to Iterate over the Players Data and Display the Results
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    # handle errors 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    #close the connection to MySQL    
    db.close()
