import requests
import json
import time
import os
from dotenv import load_dotenv
import mysql.connector

class Heat:
    def getAllDataFromTable1():

        mydb = mysql.connector.connect(
            host=os.getenv('DATABASE_URL'),
            port=os.getenv('DATABASE_PORT'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            database=os.getenv('DATABASE_NAME')
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM heats")

        myresult = mycursor.fetchall()
        return myresult
    
    def getAllDataFromTable2():

        mydb = mysql.connector.connect(
            host=os.getenv('DATABASE_URL'),
            port=os.getenv('DATABASE_PORT'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            database=os.getenv('DATABASE_NAME')
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM tbl_DatosDengue")

        myresult = mycursor.fetchall()
        return myresult
    
    def getDataFromBothTables():
        result = ""
        result = "tabla 1 = " + str(getAllDataFromTable1())
        result = result + "tabla 2 = " + str(getAllDataFromTable2())
