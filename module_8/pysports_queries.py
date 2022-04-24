""" 
    Title: pysports_queries.py
    Author: Tristan Boetcher
    Date: 4/23/22
    Description: Test program for executing queries against the pysports database. 
"""

#Imports
import mysql.connector
from mysql.connector import errorcode

#Configures connection profile
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


#Catch any potential errors
try:
    #connect to the pysports database 
    db = mysql.connector.connect(**config) 
    cursor = db.cursor()

    #output the connection status 
    print("\n\tUser {} is connected to {} MySQL database on host {}".format(config["user"], config["database"], config["host"]))
    input("\n\n\tPress any key to continue...")


    #SELECT query for team table
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    #store results in teams variable
    teams = cursor.fetchall()
    #SELECT query for player table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    #store results in players variable
    players = cursor.fetchall()


    #display results
    print(" --- Team Records --- ")
    for team in teams:
        print("\tTeam ID: {}\n\tTeam Name: {}\n\tMascot: {}\n".format(team[0], team[1], team[2]))
    print(" --- Player Records --- ")
    for player in players:
        print("\tPlayer ID: {}\n\tFirst Name: {}\n\tLast Name: {}\n\tTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n\tPress any key to continue... ")

#Error Handling
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\tThe supplied username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\tThe specified database does not exist")
    else:
        print(err)

#Close database connection
finally:
    db.close()
