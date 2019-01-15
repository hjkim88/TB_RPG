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
import codes.GlobalVar as gv

### a function to connect to a database with given parameters
def db_connect(id, pwd, host, db):
    cnx = None
    try:
        cnx = con.connect(user=id, password=pwd,
                          host=host,
                          database=db)
    except con.Error as err:
        if err.errno == con.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == con.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("DB connected")
        
    return cnx


###
def start():
    print("DBControl.py")
    cnx = db_connect(id=gv.db_id, pwd=gv.db_pwd, host=gv.host, db=gv.db_name)
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM user")
    print(cursor.fetchall())
    cursor.close()
    cnx.close()


start()
