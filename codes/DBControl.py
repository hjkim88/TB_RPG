###
#   File name : DBControl.py
#   Author    : Hyunjin Kim
#   Date      : Jan 13, 2019
#   Email     : firadazer@gmail.com
#   Purpose   : Manages database connection
#
#   Instruction
#               1. import DBControl
#               2. Run the function DBControl.start() - specify the inputs
#               3. It will help you to connect to the database
###

### import modules
import mysql.connector as con


### a function to connect to a database with given parameters
def db_connect(id, pwd, host, db):
    cnx = con.connect(user=id, password=pwd,
                      host=host,
                      database=db)
    return cnx


### a function to close a given db connection
def db_close(cnx):
    cnx.close()


###
def start():
    print("DBControl.py")
    db_connect()



